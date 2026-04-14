/**

* @file commands.c

* @author Orso Bruno

* @brief eCTF command handlers

* @date 2026

*

* @copyright Copyright (c) 2026 Università degli Studi di Trento

*/

  

#include "host_messaging.h"

#include "commands.h"

#include "filesystem.h"

#include "monocypher.h"

#include "monocypher-ed25519.h"

#include "random.h"

#include "secrets.h"

  

/* IMPORTANT COMPONENTS FROM HSM.c */

// extern file_t hsm_status[MAX_FILE_COUNT];

static file_t current_file;

  

/**

* @brief Symbol to reference FLASH files.

*/

extern const volatile files_t files;

  

/**********************************************************

******************** HELPER FUNCTIONS ********************

**********************************************************/

  

/** @brief List out the files on the system.

* To be utilized by list and interrogate

*

* @param file_list A pointer to the list_response_t variable in

* which to store the results

*/

void generate_list_files(list_response_t *file_list) {

file_list->n_files = 0;

  

// Loop through all files on the system

for (uint8_t i = 0; i < MAX_FILE_COUNT; i++) {

// Check if the file is in use

if (is_slot_in_use(i)) {

file_hdr_t hdrs = files.hdrs[i];

  

file_list->metadata[file_list->n_files].slot = i;

file_list->metadata[file_list->n_files].group_id = hdrs.group_id;

strncpy(file_list->metadata[file_list->n_files].name, (char *)&hdrs.name, MAX_NAME_SIZE);

file_list->n_files++;

  

crypto_wipe((void *)&hdrs, sizeof(file_hdr_t));

}

}

}

  

//todo find a better place for this :)

//* mayeb this one is oke

// Find the permission entry corresponding to a given group ID

// Used to retrieve the receive keys associated with that group

static const group_permission_t* find_group_perm(uint16_t gid) {

for (uint8_t i = 0; i < MAX_PERMS; i++) {

if (global_permissions[i].group_id == gid) {

return &global_permissions[i];

}

}

return NULL;

}

  
  
  

/**********************************************************

******************** COMMAND HANDLERS ********************

**********************************************************/

  

/** @brief Perform the list operation

*

* @param pkt_len The length of the incoming packet

* @param buf A pointer the incoming message buffer

*

* @return 0 upon success. A negative value on error.

*/

int list(uint16_t pkt_len, uint8_t *buf) {

list_command_t *command = (list_command_t*)buf;

  

// TODO: implement pin rate limiting

if (!check_pin(command->pin)) {

crypto_wipe((void *) command->pin, PIN_LENGTH);

print_error("Invalid pin");

return -1;

}

crypto_wipe((void *) command->pin, PIN_LENGTH);

  

list_response_t file_list;

memset(&file_list, 0, sizeof(file_list));

  

// copy relevant fields into the final struct

generate_list_files(&file_list);

  

// write success packet with list

pkt_len_t length = LIST_PKT_LEN(file_list.n_files);

write_packet(CONTROL_INTERFACE, LIST_MSG, &file_list, length);

crypto_wipe((void *) &file_list, sizeof(list_response_t));

return 0;

}

  
  

/** @brief Perform the read operation

*

* @param pkt_len The length of the incoming packet

* @param buf A pointer the incoming message buffer

*

* @return 0 upon success. A negative value on error.

*/

int read(uint16_t pkt_len, uint8_t *buf) {

read_command_t *command = (read_command_t*)buf;

read_response_t file_info;

file_t curr_file;

file_hdr_t hdr;

size_t len;

  

if (!check_pin(command->pin)) {

print_error("Invalid pin");

return -1;

}

  

// TODO: ensure wiping

// zeroizing memory is a pretty good practice

memset(&file_info, 0, sizeof(read_response_t));

  

if (read_file(command->slot, &len, &curr_file, &hdr) < 0) {

print_error("Failed to read file");

return -1;

}

// copy structure of the persistent file

memcpy(file_info.name, &hdr.name, strlen(hdr.name));

memcpy(file_info.contents, &curr_file.contents, len);

  

if (!validate_permission(hdr.group_id, PERM_READ)) {

print_error("Invalid permission");

return -1;

}

  

// write a success message with the file information

pkt_len_t length = MAX_NAME_SIZE + len;

write_packet(CONTROL_INTERFACE, READ_MSG, &file_info, length);

return 0;

}

  
  

/** @brief Perform the write operation

*

* @param pkt_len The length of the incoming packet

* @param buf A pointer the incoming message buffer

*

* @return 0 upon success. A negative value on error.

*/

int write(uint16_t pkt_len, uint8_t *buf) {

write_command_t *command = (write_command_t*)buf;

int ret;

file_t curr_file;

file_hdr_t hdr;

  

if (!check_pin(command->pin)) {

print_error("Invalid pin");

return -1;

}

  

if (!validate_permission(command->group_id, PERM_WRITE)) {

print_error("Invalid permission");

return -1;

}

  

create_file(

&hdr,

&curr_file,

command->group_id,

command->name,

command->contents_len,

command->contents

);

  

// Store the file persistently

if (write_file(command->slot, command->contents_len, &curr_file, &hdr, command->uuid) < 0) {

print_error("Error storing file");

return -1;

}

  

// Success message with an empty body

write_packet(CONTROL_INTERFACE, WRITE_MSG, NULL, 0);

return 0;

}

  
  

/** @brief Perform the receive operation

*

* @param pkt_len The length of the incoming packet

* @param buf A pointer the incoming message buffer

*

* @return 0 upon success. A negative value on error.

*/

int receive(uint16_t pkt_len, uint8_t *buf) {

receive_command_t *command = (receive_command_t *)buf;

receive_request_t request;

receive_response_t recv_resp;

msg_type_t cmd;

uint16_t len_recv_msg;

int ret;

  

if (!check_pin(command->pin)) {

print_error("Invalid pin");

return -1;

}

  

// zeroize the buffers we will use

memset(&recv_resp, 0, sizeof(recv_resp));

memset(&request, 0, sizeof(request));

  

// prep request to neighbor

request.slot = command->read_slot;

memcpy(&request.permissions, &global_permissions, sizeof(group_permission_t) * MAX_PERMS);

  

// request the file from the neighboring device

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, (void *)&request, sizeof(receive_request_t));

  

// set essentially no limit to the receive message size

len_recv_msg = 0xffff;

  

// recieve the response message

read_packet(TRANSFER_INTERFACE, &cmd, &recv_resp, &len_recv_msg);

if (cmd != RECEIVE_MSG) {

print_error("Opcode mismatch");

return -1;

}

  

// write that file into the file system

if (write_file(command->write_slot, recv_resp.len, &recv_resp.file, &recv_resp.hdr, recv_resp.uuid) < 0) {

print_error("Writing received file failed");

return -1;

}

// empty success message

write_packet(CONTROL_INTERFACE, RECEIVE_MSG, NULL, 0);

return 0;

}

  

/** @brief Perform the interrogate operation

*

* @param pkt_len The length of the incoming packet

* @param buf A pointer to the incoming message buffer

*

* @return 0 upon success. A negative value on error.

*/

  

#define SIG_SIZE 64 //todo find a better place for this too :))

  

int interrogate(uint16_t pkt_len, uint8_t *buf) {

  
  

interrogate_command_t *command = (interrogate_command_t *)buf;

  

// Step 0:

// verify pin and wipe it from memory as soon as possible

// Local copy of PIN (used later for signed requests)

uint8_t pin_local[PIN_LENGTH];

memcpy(pin_local, command->pin, PIN_LENGTH);

crypto_wipe((void *) command->pin, PIN_LENGTH);

  

if (!check_pin(pin_local)) {

crypto_wipe((void *) pin_local, PIN_LENGTH);

print_error("Invalid pin");

return -1;

}

//crypto_wipe((void *) command->pin, PIN_LENGTH);

  

// Step 1:

// Compute group IDs for which the HSM has receive permissions

uint8_t recv_groups_num = 0;

uint16_t recv_groups[MAX_PERMS] = {0};

for (uint8_t i = 0; i < MAX_PERMS; i++) {

if (global_permissions[i].receive) {

recv_groups[recv_groups_num++] = global_permissions[i].group_id;

}

}

if (recv_groups_num == 0) {

crypto_wipe(pin_local, PIN_LENGTH);

print_error("No receive permissions available");

return -1;

}

  

// Step 2:

// Generate ephemeral X25519 key pair for the interrogating side:

// A_priv = gen_key()

// A_pub = x25519_public_key(A_priv)

uint8_t private_key[PRIV_X25519_SIZE] = {0};

true_random((uint8_t*)private_key, PRIV_X25519_SIZE);

  

uint8_t public_key[PUB_X25519_SIZE] = {0};

crypto_x25519_public_key(public_key, private_key);

  

// Step 3:

// Message 1 = A_pub (32B) || n_groups (1B) || group_id_1 (2B) || ... || group_id_n (2B each)

// group_id_i is included iff the HSM has receive permissions for that group

{

size_t offset = 0;

const pkt_len_t buf_size = PUB_X25519_SIZE + sizeof(uint8_t) + MAX_PERMS * sizeof(uint16_t);

  

// Creating send buffer

uint8_t send_buf[buf_size] = {0};

memcpy(send_buf + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(send_buf + offset, &recv_groups_num, sizeof(uint8_t));

offset += sizeof(uint8_t);

memcpy(send_buf + offset, recv_groups, MAX_PERMS * sizeof(uint16_t));

  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, buf_size);

}

  

// Step 4:

// Message 2 = B_pubk (32B) || BoardID_remote (4B) || MAC_remote (16B)

// Where MAC_remote is computed by the neighbor over the transcript using enc_key

uint32_t recv_board_id = 0;

uint8_t recv_public_key[PUB_X25519_SIZE] = {0}; // B_pub

uint8_t recv_mac[POLY1305_SIZE] = {0}; // MAC_remote

  

{

size_t offset = 0;

const pkt_len_t buf_size = PUB_X25519_SIZE + BOARD_ID_LEN + POLY1305_SIZE;

  

// Create receive buffer

uint8_t recv_buf[buf_size] = {0};

  

msg_type_t cmd;

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &buf_size);

if (cmd != INTERROGATE_MSG) {

print_error("Opcode mismatch");

return -1;

}

  

// Parsing response

memcpy(recv_public_key, recv_buf + offset, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(&recv_board_id, recv_buf + offset, BOARD_ID_LEN);

offset += BOARD_ID_LEN;

memcpy(recv_mac, recv_buf + offset, POLY1305_SIZE);

}

  

// Step 5:

// Computing shared_secret

// shared_secret = X25519(A_priv, B_pub) and wipe A_priv

uint8_t shared_secret[KEY_SIZE] // shared_secret = X25519(A_priv, B_pub) and wipe A_priv

= {0};

crypto_x25519(shared_secret, private_key, recv_public_key);

crypto_wipe(private_key, PRIV_X25519_SIZE);

  

// Step 6:

// Computing encryption key

// Derive enc_key = H(K_session, recv_groups || recv_board_id || A_pub || B_pub || shared_secret)

uint8_t enc_key[KEY_SIZE] = {0};

  

{

crypto_blake2b_ctx blake_ctx;

  

crypto_blake2b_keyed_init(&blake_ctx, HASH_SIZE, K_SESSION, KEY_SIZE);

//crypto_blake2b_update(&blake_ctx, &recv_groups[0], sizeof(group_id_t));

// 4 every group id in recv_groups, update the hash with it

for (uint8_t i = 0; i < recv_groups_num; i++) {

crypto_blake2b_update(&blake_ctx, &recv_groups[i], sizeof(uint16_t));

}

crypto_blake2b_update(&blake_ctx, &recv_board_id, BOARD_ID_LEN);

crypto_blake2b_update(&blake_ctx, public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, shared_secret, KEY_SIZE);

crypto_blake2b_final(&blake_ctx, enc_key);

crypto_wipe(shared_secret, KEY_SIZE); // wipe shared secret from memory as soon as possible

}

  

// Step 7:

// Compute mac

// mac = Poly1305(enc_key, 1 || recv_groups || recv_board_id || A_pub || B_pub)

uint8_t mac[POLY1305_SIZE] = {0};

uint32_t board_id = DL_FactoryRegion_getTraceID();

  

{

const uint8_t one = 1;

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &one, sizeof(uint8_t));

for (uint8_t i = 0; i < recv_groups_num; i++) {

crypto_poly1305_update(&poly_ctx, &recv_groups[i], sizeof(uint16_t));

}

crypto_poly1305_update(&poly_ctx, &recv_board_id, BOARD_ID_LEN); // ? recv_board_id or board_id?

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, mac);

}

  

// TODO: implement constant time comparison

if (crypto_verify16(mac, recv_mac) != 0) {

// On failure: wipe secrets and abort.

crypto_wipe(enc_key, KEY_SIZE);

return -1;

}

// Step 8:

// key_established_mac = MAC(enc_key, 0 || recv_groups || BoardID_remote || A_pub || B_pub)

uint8_t key_established_mac[POLY1305_SIZE] = {0};

  

{

// Compute key_established_mac = Poly1305(enc_key, 0 || recv_groups || recv_board_id || A_pub || B_pub)

uint8_t zero = 0;

crypto_poly1305_ctx poly_ctx;

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &zero, sizeof(uint8_t));

for (uint8_t i = 0; i < recv_groups_num; i++) {

crypto_poly1305_update(&poly_ctx, &recv_groups[i], sizeof(uint16_t));

}

crypto_poly1305_update(&poly_ctx, &recv_board_id, BOARD_ID_LEN); // ? recv_board_id or board_id??

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, key_established_mac);

}

  

// Step 9:

// for each GroupID:

// - decrypt private_receive_key e firmare (GroupID || BoardID || pk_rec || pk_send)

// - signed_request_i = Sig(private_receive_key_i, GroupID_i || BoardID_remote || A_pub || B_pub)

  

// Step 10:

// Message3 = key_established_mac (16B) || signed_request_1..n (64B each)

{

// Creating send buffer

// uint8_t send_buf[POLY1305_SIZE] = {0};

// memcpy(send_buf, key_established_mac, PUB_X25519_SIZE); //? change it with POLY1305_SIZE, is 16 not 32??

  

// write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, POLY1305_SIZE);

  

// Derive a symmetric key from PIN and K_STORE

uint8_t pin_store_buf[PIN_LENGTH + KEY_SIZE] = {0};

memcpy(pin_store_buf, pin_local, PIN_LENGTH);

memcpy(pin_store_buf + PIN_LENGTH, K_STORE, KEY_SIZE);

  

uint8_t pin_store_hash[HASH_SIZE] = {0};

hash(pin_store_buf, sizeof(pin_store_buf), pin_store_hash);

crypto_wipe(pin_store_buf, sizeof(pin_store_buf));

  

// Generate one Ed25519 signature per group (signed request).

uint8_t signed_reqs[MAX_PERMS][SIG_SIZE];

memset(signed_reqs, 0, sizeof(signed_reqs));

  

for (uint8_t i = 0; i < recv_groups_num; i++) {

uint16_t gid = recv_groups[i];

  

// Find the permission entry for this group to retrieve private_receive_enc.

const group_permission_t *perm = find_group_perm(gid);

if (perm == NULL || !perm->receive) {

crypto_wipe(pin_store_hash, HASH_SIZE);

crypto_wipe(pin_local, PIN_LENGTH);

crypto_wipe(enc_key, KEY_SIZE);

print_error("Permission entry not found for group");

return -1;

}

  

// Decrypt the group's Ed25519 private receive key.

// private_receive_key = D(pin_store_key, perm->private_receive_enc)

uint8_t priv_recv_key[PRIV_EDDSA_SIZE] = {0};

if (decrypt_sym((uint8_t *)perm->private_receive_enc,

PRIV_EDDSA_SIZE,

pin_store_hash,

priv_recv_key) != 0) {

crypto_wipe(priv_recv_key, PRIV_EDDSA_SIZE);

crypto_wipe(pin_store_hash, HASH_SIZE);

crypto_wipe(pin_local, PIN_LENGTH);

crypto_wipe(enc_key, KEY_SIZE);

print_error("Decrypt private_receive_enc failed");

return -1;

}

  

// Build the message to be signed:

// msg = (GroupID || RemoteBoardID || A_pub || B_pub)

uint8_t msg[sizeof(uint16_t) + BOARD_ID_LEN + PUB_X25519_SIZE + PUB_X25519_SIZE] = {0};

size_t off = 0;

memcpy(msg + off, &gid, sizeof(uint16_t)); off += sizeof(uint16_t);

memcpy(msg + off, &recv_board_id, BOARD_ID_LEN); off += BOARD_ID_LEN;

memcpy(msg + off, public_key, PUB_X25519_SIZE); off += PUB_X25519_SIZE;

memcpy(msg + off, recv_public_key, PUB_X25519_SIZE); off += PUB_X25519_SIZE;

  

// Sign the request with the per-group private receive key (Ed25519).

crypto_ed25519_sign(signed_reqs[i], priv_recv_key, msg, sizeof(msg));

  

// Wipe per-iteration secrets.

crypto_wipe(priv_recv_key, PRIV_EDDSA_SIZE);

crypto_wipe(msg, sizeof(msg));

}

  

// Wipe secrets from stack.

crypto_wipe(pin_store_hash, HASH_SIZE);

crypto_wipe(pin_local, PIN_LENGTH);

  

// Message 3 = key_established_mac (16B) || signed_reqs[0] (64B) || ... || signed_reqs[n-1] (64B)

{

const pkt_len_t out_len = (pkt_len_t)(POLY1305_SIZE + recv_groups_num * SIG_SIZE);

uint8_t send_buf[out_len];

size_t off = 0;

  

memcpy(send_buf + off, key_established_mac, POLY1305_SIZE);

off += POLY1305_SIZE;

  

for (uint8_t i = 0; i < recv_groups_num; i++) {

memcpy(send_buf + off, signed_reqs[i], SIG_SIZE);

off += SIG_SIZE;

}

  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, out_len);

// Wipe secrets from stack.

crypto_wipe(send_buf, out_len);

crypto_wipe(signed_reqs, sizeof(signed_reqs));

}

  

}

  

// Step 11: Receive encrypted metadata list from neighbor.

// Step 12: Decrypt with enc_key and return to host.

  

list_response_t file_list;

memset(&file_list, 0, sizeof(file_list));

uint8_t ciphertext[sizeof(file_list)] = {0};

  

{

msg_type_t cmd;

const pkt_len_t buf_size = sizeof(file_list);

read_packet(TRANSFER_INTERFACE, &cmd, ciphertext, &buf_size); // ciphertext si a buffer so it dont need &ciphertext??

if (cmd != INTERROGATE_MSG) {

print_error("Opcode mismatch");

return -1;

}

}

  

uint8_t nonce[32] = {0}; //12?

crypto_chacha20_ietf(&file_list, ciphertext, sizeof(file_list), enc_key, nonce, 0);

// wipe encryption key from memory

crypto_wipe(enc_key, KEY_SIZE);

  

// Step 13: Return the metadata list to the host.

//write_packet(CONTROL_INTERFACE, INTERROGATE_MSG, &file_list, sizeof(file_list));

pkt_len_t length = LIST_PKT_LEN(file_list.n_files);

write_packet(CONTROL_INTERFACE, INTERROGATE_MSG, &file_list, length);

return 0;

  

// todo Wipe e gestione segreti: alcuni return non wipano

// todo sleep() on fail

}

  
  

/** @brief Perform the listen operation

*

* @return 0 upon success. A negative value on error.

*/

int listen(uint16_t pkt_len, uint8_t *buf) {

pkt_len_t write_length, read_length;

list_response_t file_list;

receive_request_t *command;

receive_response_t recv_resp;

const filesystem_entry_t *metadata;

  

msg_type_t cmd;

  

// Create receive buffer

const pkt_len_t buf_size = PUB_X25519_SIZE + sizeof(uint8_t) + MAX_PERMS * sizeof(uint16_t);

uint8_t recv_buf[buf_size] = {0};

  

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &buf_size);

  

switch (cmd) {

case INTERROGATE_MSG:

// Parsing response

size_t offset = 0;

uint8_t recv_groups_num = 0;

uint16_t recv_groups[MAX_PERMS] = {0};

uint8_t recv_public_key[PUB_X25519_SIZE] = {0};

  

memcpy(recv_public_key, recv_buf + offset, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(&recv_groups_num, recv_buf + offset, sizeof(uint8_t));

offset += sizeof(uint8_t);

memcpy(recv_groups, recv_buf + offset, MAX_PERMS * sizeof(uint16_t));

  

// Generate X25519 public and private keys

uint8_t private_key[PRIV_X25519_SIZE] = {0};

true_random((uint8_t*)private_key, PRIV_X25519_SIZE);

  

uint8_t public_key[PUB_X25519_SIZE] = {0};

crypto_x25519_public_key(public_key, private_key);

  

// Computing shared_secret

uint8_t shared_secret[KEY_SIZE] = {0};

crypto_x25519(shared_secret, private_key, recv_public_key);

crypto_wipe(private_key, PRIV_X25519_SIZE);

  

// Computing encryption key

uint8_t enc_key[KEY_SIZE] = {0};

uint32_t board_id = DL_FactoryRegion_getTraceID();

  

{

crypto_blake2b_ctx blake_ctx;

  

crypto_blake2b_keyed_init(&blake_ctx, HASH_SIZE, K_SESSION, KEY_SIZE);

crypto_blake2b_update(&blake_ctx, &recv_groups[0], sizeof(group_id_t));

crypto_blake2b_update(&blake_ctx, &board_id, BOARD_ID_LEN);

crypto_blake2b_update(&blake_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, shared_secret, KEY_SIZE);

crypto_blake2b_final(&blake_ctx, enc_key);

crypto_wipe(shared_secret, KEY_SIZE);

}

  

// Compute mac

uint8_t mac[POLY1305_SIZE] = {0};

{

const uint8_t one = 1;

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &one, sizeof(uint8_t));

for (uint8_t i = 0; i < recv_groups_num; i++) {

crypto_poly1305_update(&poly_ctx, &recv_groups[i], sizeof(uint16_t));

}

crypto_poly1305_update(&poly_ctx, &board_id, BOARD_ID_LEN); // ? recv_board_id or board_id?

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

}

  

{

size_t offset = 0;

const pkt_len_t buf_size = PUB_X25519_SIZE + BOARD_ID_LEN + POLY1305_SIZE;

  

// Creating send buffer

uint8_t send_buf[buf_size] = {0};

memcpy(send_buf + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(send_buf + offset, &board_id, BOARD_ID_LEN);

offset += sizeof(uint8_t);

memcpy(send_buf + offset, mac, POLY1305_SIZE);

  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, buf_size);

}

  

uint8_t key_established_mac[POLY1305_SIZE] = {0};

{

const pkt_len_t buf_size = POLY1305_SIZE;

  

// Create receive buffer

msg_type_t cmd;

read_packet(TRANSFER_INTERFACE, &cmd, key_established_mac, &buf_size);

if (cmd != INTERROGATE_MSG) {

print_error("Opcode mismatch");

return -1;

}

}

  

list_response_t full_file_list;

memset(&full_file_list, 0, sizeof(full_file_list));

generate_list_files(&full_file_list);

  

list_response_t file_list;

memset(&file_list, 0, sizeof(file_list));

  

for (uint8_t i = 0; i < full_file_list.n_files; i++) {

if (full_file_list.metadata[i].group_id == recv_groups[file_list.n_files]) {

memcpy(&file_list.metadata[file_list.n_files++], &full_file_list.metadata[i], sizeof(file_metadata_t));

}

}

  

uint8_t nonce[32] = {0}; //12?

uint8_t ciphertext[sizeof(file_list)] = {0};

crypto_chacha20_ietf(ciphertext, &file_list, sizeof(file_list), enc_key, nonce, 0);

crypto_wipe(enc_key, KEY_SIZE);

  

// Return the metadata list

write_length = LIST_PKT_LEN(file_list.n_files);

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, &ciphertext, sizeof(file_list));

break;

case RECEIVE_MSG:

// get the request

uint8_t uart_buf[sizeof(receive_request_t)];

command = (receive_request_t *)uart_buf;

  

// TODO: the reference design does not implement *ANY* security

// you will want to add something here to comply with SR1

  

// if this read fails, the other device will not receive a response and

// may need to be reset before further testing can occur

if (read_file(command->slot, &recv_resp.len, &recv_resp.file, &recv_resp.hdr) < 0) {

print_error("Failed to read file");

return -1;

}

  

metadata = get_file_metadata(command->slot);

if (metadata == NULL) {

print_error("Getting metadata failed");

return -1;

}

  

memcpy(&recv_resp.uuid, &metadata->uuid, UUID_SIZE);

  

// send the file to the neighbor hsm

write_length = sizeof(receive_response_t);

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, &recv_resp, write_length);

break;

default:

print_error("Bad message type");

return -1;

}

  

// Blank success message

write_packet(CONTROL_INTERFACE, LISTEN_MSG, NULL, 0);

return 0;

}