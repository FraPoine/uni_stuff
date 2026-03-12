/**

* @file commands.c

* @author Orso Bruno

* @brief eCTF command handlers

* @date 2026

*

* @copyright Copyright (c) 2026 Università degli Studi di Trento

*/

  

#include "commands.h"

#include "crypto.h"

#include "filesystem.h"

#include "host_messaging.h"

#include "monocypher-ed25519.h"

#include "monocypher.h"

#include "secrets.h"

#include "random.h"

  

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

for (uint8_t slot_idx = 0; slot_idx < MAX_FILE_COUNT; slot_idx++) {

// Check if the file is in use

file_hdr_t *hdr = get_hdr(slot_idx);

if (hdr && is_slot_in_use(slot_idx)) {

file_list->metadata[file_list->n_files].slot = slot_idx;

file_list->metadata[file_list->n_files].group_id = hdr->group_id;

strncpy(file_list->metadata[file_list->n_files].name, (char *)&hdr->name, MAX_NAME_SIZE);

file_list->n_files++;

}

}

}

  

// todo find a better place.

static bool group_allowed(uint16_t gid, const uint16_t *groups, uint8_t n) {

for (uint8_t j = 0; j < n; j++) {

if (groups[j] == gid) return true;

}

return false;

}

  

// viene pre processata

static inline void crypto_1305_interrogate(uint8_t enc_key[KEY_SIZE], uint16_t recv_groups[MAX_PERMS], uint8_t recv_groups_num, uint8_t recv_public_key[PUB_X25519_SIZE], uint8_t public_key[PUB_X25519_SIZE], uint32_t board_id, uint8_t mac[POLY1305_SIZE], const uint8_t one) {

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &one, sizeof(uint8_t));

for (uint8_t i = 0; i < recv_groups_num; i++) {

crypto_poly1305_update(&poly_ctx, (uint8_t *)&recv_groups[i], sizeof(uint16_t));

}

crypto_poly1305_update(&poly_ctx, (uint8_t *)&board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, mac);

}

  

// TODO: doc

static inline void derive_k_keys(uint8_t k_keys[KEY_SIZE], const uint8_t pin[PIN_LENGTH]) {

crypto_blake2b_ctx ctx;

crypto_blake2b_init(&ctx, KEY_SIZE);

crypto_blake2b_update(&ctx, pin, PIN_LENGTH);

crypto_blake2b_update(&ctx, K_STORE, KEY_SIZE);

crypto_blake2b_final(&ctx, k_keys);

}

  

static inline void derive_exchange_key(uint8_t key[KEY_SIZE], const uint8_t shared[KEY_SIZE], const uint8_t pub1[PUB_X25519_SIZE], const uint8_t pub2[PUB_X25519_SIZE]) {

crypto_blake2b_ctx ctx;

crypto_blake2b_init(&ctx, KEY_SIZE);

crypto_blake2b_update(&ctx, shared, KEY_SIZE);

crypto_blake2b_update(&ctx, pub1, PUB_X25519_SIZE);

crypto_blake2b_update(&ctx, pub2, PUB_X25519_SIZE);

crypto_blake2b_final(&ctx, key);

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

list_command_t *command = (list_command_t *)buf;

  

// TODO: implement pin rate limiting

if (!check_pin(command->pin)) {

crypto_wipe((void *)command->pin, PIN_LENGTH);

print_error("Invalid pin");

return -1;

}

crypto_wipe((void *)command->pin, PIN_LENGTH);

  

list_response_t file_list;

memset(&file_list, 0, sizeof(file_list));

  

// copy relevant fields into the final struct

generate_list_files(&file_list);

  

// write success packet with list

pkt_len_t length = LIST_PKT_LEN(file_list.n_files);

write_packet(CONTROL_INTERFACE, LIST_MSG, &file_list, length);

crypto_wipe((void *)&file_list, sizeof(list_response_t));

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

read_command_t *command = (read_command_t *)buf;

read_response_t file_info;

group_id_t group_id;

int perm_idx;

  

if (!check_pin(command->pin)) {

print_error("Invalid pin");

return -1;

}

  

if (get_group_id(command->slot, &group_id) < 0) {

print_error("Could not retrieve group_id");

return -1;

}

  

perm_idx = validate_permission(group_id, PERM_READ);

if (perm_idx < 0 || perm_idx >= MAX_PERMS) {

print_error("Invalid permission");

return -1;

}

  

memset(&file_info, 0, sizeof(read_response_t));

  

// The hash is used as a random oracle (or PRF if keyed) for KEY derivation.

uint8_t hash_key[KEY_SIZE] = {0};

uint8_t public_write_key[PUB_EDDSA_SIZE] = {0};

uint8_t private_read_key[PRIV_X25519_SIZE] = {0};

uint8_t public_read_key[PUB_X25519_SIZE] = {0};

nonce_t nonce = {.group_id = group_id};

  

derive_k_keys(hash_key, command->pin);

  

// group_id || ctr(3)

nonce.ctr_idx = WRITE_PUB;

  

// Decrypt public_write_enc

decrypt(global_permissions[perm_idx].public_write_enc, public_write_key, PUB_EDDSA_SIZE, hash_key, (uint8_t *)&nonce);

  

if (get_file_name(command->slot, file_info.name) < 0) {

print_error("Could not find name");

return -1;

}

memcpy(file_info.contents, shadow_FAT[command->slot].flash_addr, shadow_FAT[command->slot].length);

  

uint8_t sig[SIGNATURE_SIZE];

if (get_file_sig(command->slot, sig) != 0) {

print_error("Could not find sig");

return -1;

}

if (eddsa_check_sig(sig, public_write_key, file_info.contents, (uint8_t *)shadow_FAT[command->slot].uuid, group_id, (uint8_t *)file_info.name) != 0) {

crypto_wipe(public_write_key, PUB_EDDSA_SIZE);

print_error("Sig error");

return -1;

}

  

crypto_wipe(public_write_key, PUB_EDDSA_SIZE);

  

// group_id || ctr(1)

nonce.ctr_idx = READ_PRIV;

  

// Decrypt private_read_key

decrypt(global_permissions[perm_idx].private_read_enc, private_read_key, PRIV_X25519_SIZE, hash_key, (uint8_t *)&nonce);

  

// TODO: define 25519 curve element size.

uint8_t raw_shared_secret[KEY_SIZE] = {0};

uint8_t appended_key[PUB_X25519_SIZE] = {0};

if (get_appended_key(command->slot, appended_key) < 0) {

print_error("Appended hash not found");

return -1;

}

  

crypto_x25519(raw_shared_secret, private_read_key, appended_key);

  

crypto_wipe(private_read_key, PRIV_X25519_SIZE);

  

// group_id || ctr(4)

nonce.ctr_idx = READ_PUB;

  

// TODO: check if it is more computationally feasible the decryption or the public key derivation.

// Decrypt public_read_key

decrypt(global_permissions[perm_idx].public_read_enc, public_read_key, PUB_X25519_SIZE, hash_key, (uint8_t *)&nonce);

  

derive_exchange_key(hash_key, raw_shared_secret, public_read_key, appended_key);

  

crypto_wipe(appended_key, PUB_X25519_SIZE);

crypto_wipe(raw_shared_secret, KEY_SIZE);

crypto_wipe(public_read_key, PUB_X25519_SIZE);

  

ad_aead_t ad;

memset(&ad, 0, sizeof(ad));

ad.slot = command->slot;

ad.group_id = group_id;

ad.contents_len = shadow_FAT[command->slot].length;

memcpy(ad.name, file_info.name, MAX_NAME_SIZE);

memcpy(ad.uuid, shadow_FAT[command->slot].uuid, UUID_SIZE);

  

uint8_t mac[POLY1305_SIZE] = {0};

  

if (get_file_mac(command->slot, mac) < 0) {

print_error("Mac not found");

return -1;

}

  

if (decrypt_aead(hash_key, file_info.contents, mac, &ad, sizeof(ad_aead_t), shadow_FAT[command->slot].flash_addr, ad.contents_len) < 0) {

crypto_wipe(hash_key, KEY_SIZE);

print_error("Decrypt error");

return -1;

}

  

pkt_len_t length = MAX_NAME_SIZE + ad.contents_len;

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

write_command_t *command = (write_command_t *)buf;

  

// pkt_len >= header_length

// command->hdr.contents_len + header_length == pkt_len

// command->hdr.contents_len <= MAX_CONTENTS_SIZE

  

if (pkt_len<sizeof(struct write_command_hdr) |

pkt_len != sizeof(struct write_command_hdr) + command->hdr.contents_len |

command->hdr.contents_len>

MAX_CONTENTS_SIZE) {

print_error("Invalid write command");

return -1;

}

  

if (!check_pin(command->hdr.pin)) {

print_error("Invalid pin");

return -1;

}

  

int perm_idx = validate_permission(command->hdr.group_id, PERM_WRITE);

if (perm_idx < 0 || perm_idx >= MAX_PERMS) {

print_error("Invalid permission");

return -1;

}

  

uint8_t private_exponent[PRIV_X25519_SIZE] = {0};

true_random(private_exponent, PRIV_X25519_SIZE);

  

uint8_t appended_key[PUB_X25519_SIZE] = {0};

crypto_x25519_public_key(appended_key, private_exponent);

  

uint8_t hash_pin_kstore[KEY_SIZE] = {0};

derive_k_keys(hash_pin_kstore, command->hdr.pin);

  

nonce_t nonce = {.group_id = command->hdr.group_id};

  

uint8_t public_read_key[PUB_X25519_SIZE] = {0};

nonce.ctr_idx = READ_PUB;

  

decrypt(global_permissions[perm_idx].public_read_enc, public_read_key, PUB_X25519_SIZE, hash_pin_kstore, (uint8_t *)&nonce);

  

// TODO: define 25519 curve element size.

uint8_t raw_shared_secret[KEY_SIZE] = {0};

crypto_x25519(raw_shared_secret, private_exponent, public_read_key);

crypto_wipe(private_exponent, PRIV_X25519_SIZE);

  

uint8_t enc_key[KEY_SIZE] = {0};

derive_exchange_key(enc_key, raw_shared_secret, public_read_key, appended_key);

  

crypto_wipe(raw_shared_secret, KEY_SIZE);

crypto_wipe(public_read_key, PUB_X25519_SIZE);

  

struct __attribute((packed)) {

uint8_t uuid[UUID_SIZE];

file_t content;

uint16_t group_id;

uint8_t name[MAX_NAME_SIZE];

} data;

memset(&data, 0, sizeof(data));

  

uint8_t mac[POLY1305_SIZE] = {0};

ad_aead_t ad;

memset(&ad, 0, sizeof(ad));

ad.slot = command->hdr.slot;

ad.group_id = command->hdr.group_id;

ad.contents_len = command->hdr.contents_len;

memcpy(ad.name, command->hdr.name, MAX_NAME_SIZE);

memcpy(ad.uuid, command->hdr.uuid, UUID_SIZE);

  

encrypt_aead(enc_key, &data.content.contents, mac, (uint8_t *)&ad, sizeof(ad_aead_t), command->contents, command->hdr.contents_len);

  

crypto_wipe(enc_key, HASH_SIZE);

  

memcpy(data.uuid, command->hdr.uuid, UUID_SIZE);

data.group_id = command->hdr.group_id;

memcpy(data.name, command->hdr.name, MAX_NAME_SIZE);

  

file_hdr_t curr_file_hdr = {

.in_use = FILE_IN_USE,

.group_id = data.group_id,

};

  

uint8_t private_write_key[PRIV_EDDSA_SIZE] = {0};

nonce.ctr_idx = WRITE_PRIV;

  

decrypt(global_permissions[perm_idx].private_write_enc, private_write_key, PRIV_EDDSA_SIZE, hash_pin_kstore, (uint8_t *)&nonce);

  

crypto_eddsa_sign(curr_file_hdr.sig, private_write_key, (uint8_t *)&data, sizeof(data));

crypto_wipe(private_write_key, PRIV_EDDSA_SIZE);

  

strncpy(curr_file_hdr.name, command->hdr.name, MAX_NAME_SIZE);

memmove(curr_file_hdr.appended_key, appended_key, PUB_X25519_SIZE);

memmove(curr_file_hdr.mac, mac, POLY1305_SIZE);

  

// Store the file persistently

if (write_file(command->hdr.slot, command->hdr.contents_len, data.content.contents, &curr_file_hdr, command->hdr.uuid) < 0) {

print_error("Error storing file");

return -1;

}

  

// Success message with an empty body

if (write_packet(CONTROL_INTERFACE, WRITE_MSG, NULL, 0) < 0) {

print_error("Error writing packet");

return -1;

}

  

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

pkt_len_t len_recv_msg;

int ret;

uint8_t pin_store_key[KEY_SIZE] = {0};

uint8_t signed_req[SIGNATURE_SIZE] = {0};

uint16_t gid = 0;

const group_permission_t *perm = NULL;

int perm_idx;

  
  

if (!check_pin(command->pin)) {

crypto_wipe((void *) command->pin, PIN_LENGTH);

print_error("Invalid pin");

return -1;

}

memset(&recv_resp, 0, sizeof(recv_resp));

memset(&request, 0, sizeof(request));

  

uint8_t private_key[PRIV_X25519_SIZE] = {0};

true_random((uint8_t*)private_key, PRIV_X25519_SIZE);

  

uint8_t public_key[PUB_X25519_SIZE] = {0};

crypto_x25519_public_key(public_key, private_key);

  

request.slot = command->read_slot;

// per ora Message 1 = A_pub (32B) || read_slot(1B)

{

size_t offset = 0;

const pkt_len_t buf_size = sizeof(uint8_t) + PUB_X25519_SIZE;

  

//creating send buffer

uint8_t send_buf_m1[buf_size] = {0};

  

// read_slot

memcpy(send_buf_m1 + offset, &command->read_slot, sizeof(uint8_t));

offset += sizeof(uint8_t);

  

// A_pub

memcpy(send_buf_m1 + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

  

// sanity: offset should now equal buf_size

if (offset != buf_size) {

print_error("Send buffer size mismatch");

return -1;

}

  

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, send_buf_m1, buf_size);

}

  

// Message 2 = group_id(2B) || B_pubk (32B) || BoardID_remote (4B) || MAC_remote (16B)

  

uint16_t recv_group_id = 0;

uint32_t recv_board_id = 0;

uint8_t recv_public_key[PUB_X25519_SIZE] = {0}; // B_pub

uint8_t recv_mac[POLY1305_SIZE] = {0}; // MAC_remote

nonce_t nonce = {0};

  

{

size_t offset = 0;

  

// Expected length for Message 2

const pkt_len_t expected_len = sizeof(group_id_t) + PUB_X25519_SIZE + BOARD_ID_LEN + POLY1305_SIZE;

  

// Use a separate variable for the length passed to read_packet

len_recv_msg = expected_len;

  

uint8_t recv_buf[expected_len];

memset(recv_buf, 0, sizeof(recv_buf));

  

msg_type_t cmd;

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &len_recv_msg);

  

if (cmd != RECEIVE_MSG) {

print_error("Opcode mismatch");

return -1;

}

  

// verify length is exactly what we expect

if (len_recv_msg != expected_len) {

print_error("Handshake response length mismatch");

return -1;

}

  

// Parsing response: group_id

memcpy(&recv_group_id, recv_buf + offset, sizeof(group_id_t));

offset += sizeof(group_id_t);

nonce.group_id = recv_group_id;

  

perm_idx = validate_permission(recv_group_id, PERM_READ);

if (perm_idx < 0 || perm_idx >= MAX_PERMS) {

print_error("Invalid permission");

return -1;

}

// B_pub

memcpy(recv_public_key, recv_buf + offset, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

// BoardID_remote

memcpy(&recv_board_id, recv_buf + offset, BOARD_ID_LEN);

offset += BOARD_ID_LEN;

// MAC_remote

memcpy(recv_mac, recv_buf + offset, POLY1305_SIZE);

offset += POLY1305_SIZE;

// sanity: offset should now equal expected_len

if (offset != expected_len) {

print_error("Handshake response parsing error");

return -1;

}

}

  

uint8_t shared_secret[KEY_SIZE] = {0};

crypto_x25519(shared_secret, private_key, recv_public_key);

crypto_wipe(private_key, PRIV_X25519_SIZE);

  

uint8_t enc_key[KEY_SIZE] = {0};

{

crypto_blake2b_ctx blake_ctx;

  

crypto_blake2b_keyed_init(&blake_ctx, HASH_SIZE, K_SESSION, KEY_SIZE);

// PRF input: GroupID (REMOTE) || BoardID_B || A_pub || B_pub || raw_shared_secret

crypto_blake2b_update(&blake_ctx, &recv_group_id, sizeof(uint16_t));

crypto_blake2b_update(&blake_ctx, &recv_board_id, BOARD_ID_LEN);

crypto_blake2b_update(&blake_ctx, public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, shared_secret, KEY_SIZE);

  

crypto_blake2b_final(&blake_ctx, enc_key);

  

crypto_wipe(shared_secret, KEY_SIZE);

}

  

// Compute mac

// mac = Poly1305(enc_key, 1 || recv_group_id || recv_board_id || A_pub || B_pub)

uint8_t mac[POLY1305_SIZE] = {0};

uint32_t board_id = DL_FactoryRegion_getTraceID();

  

{

const uint8_t one = 1;

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &one, sizeof(uint8_t));

crypto_poly1305_update(&poly_ctx, &recv_group_id, sizeof(group_id_t));

crypto_poly1305_update(&poly_ctx, &recv_board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, mac);

}

  

if (crypto_verify16(mac, recv_mac) != 0) {

// Handshake failed: wipe session key and abort

crypto_wipe(enc_key, KEY_SIZE);

// sleep(); // TODO: implement constant time comparison

print_error("Handshake MAC mismatch");

return -1;

}

uint8_t key_established_mac[POLY1305_SIZE] = {0};

  

{

// Compute key_established_mac = Poly1305(enc_key, 0 || recv_group_id || recv_board_id || A_pub || B_pub)

uint8_t zero = 0;

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &zero, sizeof(uint8_t));

crypto_poly1305_update(&poly_ctx, &recv_group_id, sizeof(group_id_t));

crypto_poly1305_update(&poly_ctx, &recv_board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, key_established_mac);

}

  

perm_idx = validate_permission(recv_group_id, PERM_RECEIVE);

if (perm_idx < 0 || perm_idx >= MAX_PERMS) {

print_error("Invalid permission");

return -1;

}

  

uint8_t sig[SIGNATURE_SIZE] = {0};

  

{

uint8_t private_receive_key[PUB_EDDSA_SIZE] = {0};

uint8_t hash_key[KEY_SIZE] = {0};

  

derive_k_keys(hash_key, command->pin);

nonce.ctr_idx = READ_PRIV;

nonce.group_id = recv_group_id;

  

// Decrypt private_receive_key

decrypt(global_permissions[perm_idx].private_receive_enc, private_receive_key, PUB_EDDSA_SIZE, hash_key, (uint8_t*)&nonce);

  

// signed request = Sig(private receive key, Group ID ∥ Board ID ∥ public key rec ∥ public key send)

// crypto wipe(private receive key)

struct __attribute((packed)) {

uint16_t group_id;

uint8_t board_id;

uint8_t public_key_rec;

uint8_t public_key_send;

} data;

memset(&data, 0, sizeof(data));

  

data.group_id = recv_group_id;

data.board_id = recv_board_id;

memcpy(&data.public_key_rec, public_key, PUB_X25519_SIZE);

memcpy(&data.public_key_send, recv_public_key, PUB_X25519_SIZE);

  
  

crypto_eddsa_sign(sig, private_receive_key, (uint8_t *)&data, sizeof(data));

crypto_wipe(private_receive_key, PRIV_EDDSA_SIZE);

  

}

  

// Creating send bufferPOLY1305_SIZE

uint8_t send_buf[POLY1305_SIZE + SIGNATURE_SIZE] = {0};

memcpy(send_buf, key_established_mac, POLY1305_SIZE);

memcpy(send_buf + POLY1305_SIZE, sig, SIGNATURE_SIZE);

  

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, send_buf, POLY1305_SIZE + SIGNATURE_SIZE);

  

{

// Message 4 = file package (variable, up to 64KB): GroupID (2B) || file metadata (variable) || file contents (variable)

uint8_t public_write_key[PUB_EDDSA_SIZE] = {0};

uint8_t hash_key[KEY_SIZE] = {0};

  

struct __attribute((packed)) {

receive_response_t ciphertext;

uint8_t mac[POLY1305_SIZE];

} msg;

{

msg_type_t cmd;

pkt_len_t buf_size = sizeof(msg); // We expect the message to include the ciphertext and the MAC

read_packet(TRANSFER_INTERFACE, &cmd, &msg, &buf_size);

if (cmd != RECEIVE_MSG) {

print_error("Opcode mismatch");

return -1;

}

}

if(decrypt_aead(enc_key, &msg.ciphertext, msg.mac, NULL, 0, &msg.ciphertext, sizeof(receive_response_t)) < 0) {

print_error("Decryption failed");

return -1;

}

  

derive_k_keys(hash_key, command->pin);

nonce.ctr_idx = WRITE_PUB;

  

// Decrypt public_write_key

decrypt(global_permissions[perm_idx].public_write_enc, public_write_key, PUB_EDDSA_SIZE, hash_key, (uint8_t*)&nonce);

  

if (eddsa_check_sig(msg.ciphertext.hdr.sig, public_write_key, msg.ciphertext.file.contents, (uint8_t *)msg.ciphertext.uuid, msg.ciphertext.hdr.group_id, (uint8_t *)msg.ciphertext.hdr.name) != 0) {

crypto_wipe(public_write_key, PUB_EDDSA_SIZE);

print_error("Sig error");

return -1;

}

  

crypto_wipe(public_write_key, PUB_EDDSA_SIZE);

if (write_file(command->write_slot, msg.ciphertext.len, msg.ciphertext.file.contents, &msg.ciphertext.hdr, msg.ciphertext.uuid) < 0) {

print_error("Error storing file");

return -1;

}

  

}

  

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

  

  
  

int interrogate(uint16_t pkt_len, uint8_t *buf) {

interrogate_command_t *command = (interrogate_command_t *)buf;

  

if (!check_pin(command->pin)) {

crypto_wipe((void *) command->pin, PIN_LENGTH);

print_error("Invalid pin");

return -1;

}

crypto_wipe((void *) command->pin, PIN_LENGTH);

  

// Compute group IDs for which the HSM has receive permissions

uint8_t recv_groups_num = 0;

uint16_t recv_groups[MAX_PERMS] = {0};

for (uint8_t i = 0; i < MAX_PERMS; i++) {

if (global_permissions[i].receive) {

recv_groups[recv_groups_num++] = global_permissions[i].group_id;

}

}

  

// Generate X25519 public and private keys

uint8_t private_key[PRIV_X25519_SIZE] = {0};

true_random((uint8_t*)private_key, PRIV_X25519_SIZE);

  

uint8_t public_key[PUB_X25519_SIZE] = {0};

crypto_x25519_public_key(public_key, private_key);

  

{

size_t offset = 0;

// Creating send buffer

uint8_t send_buf[KEY_EXCHANGE_INIT_SIZE] = {0};

memcpy(send_buf + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(send_buf + offset, &recv_groups_num, sizeof(uint8_t));

offset += sizeof(uint8_t);

//memcpy(send_buf + offset, recv_groups, MAX_PERMS * sizeof(group_id_t));

memcpy(send_buf + offset, recv_groups, recv_groups_num * sizeof(group_id_t));

  
  
  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, KEY_EXCHANGE_INIT_SIZE);

}

  

uint32_t recv_board_id = 0;

uint8_t recv_public_key[PUB_X25519_SIZE] = {0};

uint8_t recv_mac[POLY1305_SIZE] = {0};

  

{

size_t offset = 0;

pkt_len_t buf_size = KEY_EXCHANGE_REPLY_SIZE;

  

// Create receive buffer

uint8_t recv_buf[KEY_EXCHANGE_REPLY_SIZE] = {0};

  

msg_type_t cmd;

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &buf_size);

if (cmd != INTERROGATE_MSG || buf_size != KEY_EXCHANGE_REPLY_SIZE) {

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

  

// Computing shared_secret

uint8_t shared_secret[KEY_SIZE] = {0};

crypto_x25519(shared_secret, private_key, recv_public_key);

crypto_wipe(private_key, PRIV_X25519_SIZE);

  

// Computing encryption key

uint8_t enc_key[KEY_SIZE] = {0};

  

{

crypto_blake2b_ctx blake_ctx;

  

crypto_blake2b_keyed_init(&blake_ctx, HASH_SIZE, K_SESSION, KEY_SIZE);

crypto_blake2b_update(&blake_ctx, (uint8_t *)&recv_groups[0], sizeof(group_id_t));

crypto_blake2b_update(&blake_ctx, (uint8_t *)&recv_board_id, BOARD_ID_LEN);

crypto_blake2b_update(&blake_ctx, public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_blake2b_update(&blake_ctx, shared_secret, KEY_SIZE);

crypto_blake2b_final(&blake_ctx, enc_key);

crypto_wipe(shared_secret, KEY_SIZE);

}

  

// Compute mac

uint8_t mac[POLY1305_SIZE] = {0};

uint32_t board_id = DL_FactoryRegion_getTraceID();

  

// {

// const uint8_t one = 1;

// crypto_poly1305_ctx poly_ctx;

  

// crypto_poly1305_init(&poly_ctx, enc_key);

// crypto_poly1305_update(&poly_ctx, &one, sizeof(uint8_t));

// for (uint8_t i = 0; i < recv_groups_num; i++) {

// crypto_poly1305_update(&poly_ctx, (uint8_t *)&recv_groups[i], sizeof(uint16_t));

// }

// crypto_poly1305_update(&poly_ctx, (uint8_t *)&recv_board_id, BOARD_ID_LEN);

// crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

// crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

// crypto_poly1305_final(&poly_ctx, mac);

// }

  

crypto_1305_interrogate(enc_key, recv_groups, recv_groups_num, recv_public_key, public_key, board_id, mac, 1);

  

// TODO: implement constant time comparison

if (crypto_verify16(mac, recv_mac) != 0) {

crypto_wipe(enc_key, KEY_SIZE);

return -1;

}

  

uint8_t key_established_mac[POLY1305_SIZE] = {0};

  

// {

// uint8_t zero = 0;

// crypto_poly1305_ctx poly_ctx;

  

// crypto_poly1305_init(&poly_ctx, enc_key);

// crypto_poly1305_update(&poly_ctx, &zero, sizeof(uint8_t));

// for (uint8_t i = 0; i < recv_groups_num; i++) {

// crypto_poly1305_update(&poly_ctx, (uint8_t *)&recv_groups[i], sizeof(uint16_t));

// }

// crypto_poly1305_update(&poly_ctx, (uint8_t *)&board_id, BOARD_ID_LEN);

// crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

// crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

// crypto_poly1305_final(&poly_ctx, key_established_mac);

// }

crypto_1305_interrogate(enc_key, recv_groups, recv_groups_num, recv_public_key, public_key, board_id, key_established_mac, 0);

  
  

{

// Creating send buffer

uint8_t send_buf[SESSION_ESTABLISH_SIZE] = {0};

memcpy(send_buf, key_established_mac, SESSION_ESTABLISH_SIZE);

  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, SESSION_ESTABLISH_SIZE);

}

  

// list_response_t file_list;

// memset(&file_list, 0, sizeof(list_response_t));

struct __attribute((packed)) {

uint8_t ciphertext[sizeof(list_response_t)];

uint8_t mac[POLY1305_SIZE];

} msg;

  

{

msg_type_t cmd;

pkt_len_t buf_size = ENCRYPTED_RESPONSE_SIZE;

read_packet(TRANSFER_INTERFACE, &cmd, &msg, &buf_size);

if (cmd != INTERROGATE_MSG || buf_size != ENCRYPTED_RESPONSE_SIZE) {

print_error("Opcode mismatch");

return -1;

}

}

  

decrypt_aead(enc_key, msg.ciphertext, msg.mac, NULL, 0, msg.ciphertext, sizeof(list_response_t));

// crypto_chacha20_ietf((uint8_t *)&file_list, ciphertext, ENCRYPTED_RESPONSE_SIZE, enc_key, nonce, 0);

crypto_wipe(enc_key, KEY_SIZE);

  

// Return the metadata list

pkt_len_t write_length = LIST_PKT_LEN(((list_response_t *)msg.ciphertext)->n_files);

write_packet(CONTROL_INTERFACE, INTERROGATE_MSG, (list_response_t *)msg.ciphertext, write_length);

return 0;

}

  
  

/** @brief Perform the listen operation

*

* @return 0 upon success. A negative value on error.

*/

int listen(uint16_t pkt_len, uint8_t *buf) {

pkt_len_t write_length, read_length;

msg_type_t cmd;

  

// Create receive buffer

pkt_len_t buf_size = KEY_EXCHANGE_INIT_SIZE;

uint8_t recv_buf[KEY_EXCHANGE_INIT_SIZE] = {0};

  

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &buf_size);

  

switch (cmd) {

case INTERROGATE_MSG: {

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

// char t[64];

// snprintf(t, sizeof(t), "[N] recv_groups_num=%u\n", recv_groups_num);

// print_debug(t);

// print_hex_debug(recv_groups, recv_groups_num * sizeof(uint16_t));

  

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

crypto_blake2b_update(&blake_ctx, (uint8_t *)&recv_groups[0], sizeof(group_id_t));

crypto_blake2b_update(&blake_ctx, (uint8_t *)&board_id, BOARD_ID_LEN);

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

crypto_poly1305_update(&poly_ctx, (uint8_t *)&recv_groups[i], sizeof(uint16_t));

}

crypto_poly1305_update(&poly_ctx, (uint8_t *)&board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, mac);

  

}

  

{

size_t offset = 0;

pkt_len_t buf_size = KEY_EXCHANGE_REPLY_SIZE;

  

// Creating send buffer

uint8_t send_buf[KEY_EXCHANGE_REPLY_SIZE] = {0};

memcpy(send_buf + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

memcpy(send_buf + offset, &board_id, BOARD_ID_LEN);

offset += BOARD_ID_LEN;

memcpy(send_buf + offset, mac, POLY1305_SIZE);

  

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, send_buf, KEY_EXCHANGE_REPLY_SIZE);

}

  

uint8_t key_established_mac[SESSION_ESTABLISH_SIZE] = {0};

{

pkt_len_t buf_size = SESSION_ESTABLISH_SIZE;

  

// Create receive buffer

msg_type_t cmd;

read_packet(TRANSFER_INTERFACE, &cmd, key_established_mac, &buf_size);

if (cmd != INTERROGATE_MSG || buf_size != SESSION_ESTABLISH_SIZE) {

print_error("Opcode mismatch");

return -1;

}

}

  

list_response_t full_file_list;

memset(&full_file_list, 0, sizeof(full_file_list));

generate_list_files(&full_file_list);

  

// snprintf(t, sizeof(t), "[N] full n_files=%u\n", full_file_list.n_files);

// print_debug(t);

  

list_response_t file_list;

memset(&file_list, 0, sizeof(list_response_t));

  

// for (uint8_t i = 0; i < full_file_list.n_files; i++) {

// if (full_file_list.metadata[i].group_id == recv_groups[file_list.n_files]) {

// memcpy(&file_list.metadata[file_list.n_files++], &full_file_list.metadata[i], sizeof(file_metadata_t));

// }

// }

  

file_list.n_files = 0;

for (uint8_t i = 0; i < full_file_list.n_files; i++) {

if (group_allowed(full_file_list.metadata[i].group_id, recv_groups, recv_groups_num)) {

memcpy(&file_list.metadata[file_list.n_files], &full_file_list.metadata[i], sizeof(file_metadata_t));

file_list.n_files++;

}

}

  

// snprintf(t, sizeof(t), "[N] filtered n_files=%u\n", file_list.n_files);

// print_debug(t);

  

struct __attribute((packed)) {

uint8_t ciphertext[sizeof(list_response_t)];

uint8_t mac[POLY1305_SIZE];

} msg;

  

encrypt_aead(enc_key, msg.ciphertext, msg.mac, NULL, 0, &file_list, sizeof(list_response_t));

crypto_wipe(enc_key, KEY_SIZE);

  

// Return the metadata list

write_length = LIST_PKT_LEN(file_list.n_files);

write_packet(TRANSFER_INTERFACE, INTERROGATE_MSG, &msg, ENCRYPTED_RESPONSE_SIZE);

break;

}

case RECEIVE_MSG: {

// Parsing response

size_t offset = 0;

uint8_t read_slot = 0;

uint8_t recv_public_key[PUB_X25519_SIZE] = {0};

group_id_t recv_group_id = 0;

memcpy(&read_slot, recv_buf + offset, sizeof(uint8_t));

offset += sizeof(uint8_t);

memcpy(recv_public_key, recv_buf + offset, PUB_X25519_SIZE);

  

get_group_id(read_slot, &recv_group_id);

  

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

crypto_blake2b_update(&blake_ctx, &recv_group_id, sizeof(group_id_t));

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

crypto_poly1305_update(&poly_ctx, &recv_group_id, sizeof(group_id_t));

crypto_poly1305_update(&poly_ctx, &board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, mac);

  

}

  

{

size_t offset = 0;

const pkt_len_t buf_size = sizeof(group_id_t) + PUB_X25519_SIZE + BOARD_ID_LEN + POLY1305_SIZE;

  

// Creating send buffer

uint8_t send_buf[buf_size] = {0};

  

memcpy(send_buf + offset, &recv_group_id, sizeof(group_id_t));

offset += sizeof(group_id_t);

// A_pubuint16_t

memcpy(send_buf + offset, public_key, PUB_X25519_SIZE);

offset += PUB_X25519_SIZE;

// BoardID_remote

memcpy(send_buf + offset, &board_id, BOARD_ID_LEN);

offset += BOARD_ID_LEN;

// MAC_remote

memcpy(send_buf + offset, mac, POLY1305_SIZE);

  

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, send_buf, buf_size);

}

  

uint8_t recv_mac[POLY1305_SIZE] = {0};

uint8_t key_established_mac[POLY1305_SIZE] = {0};

uint8_t sig[SIGNATURE_SIZE] = {0};

  

//qua mi arriva anche la sign req

{

const pkt_len_t buf_size = POLY1305_SIZE + SIGNATURE_SIZE;

  

// Create receive buffer

msg_type_t cmd;

uint8_t recv_buf[buf_size];

read_packet(TRANSFER_INTERFACE, &cmd, recv_buf, &buf_size);

if (cmd != RECEIVE_MSG) {

print_error("Opcode mismatch");

return -1;

}

memcpy(recv_mac, recv_buf, POLY1305_SIZE);

memcpy(sig, recv_buf + POLY1305_SIZE, SIGNATURE_SIZE);

}

  

//verifica del mac

{

const uint8_t zero = 0;

crypto_poly1305_ctx poly_ctx;

  

crypto_poly1305_init(&poly_ctx, enc_key);

crypto_poly1305_update(&poly_ctx, &zero, sizeof(uint8_t));

crypto_poly1305_update(&poly_ctx, &recv_group_id, sizeof(group_id_t));

crypto_poly1305_update(&poly_ctx, &board_id, BOARD_ID_LEN);

crypto_poly1305_update(&poly_ctx, public_key, PUB_X25519_SIZE);

crypto_poly1305_update(&poly_ctx, recv_public_key, PUB_X25519_SIZE);

crypto_poly1305_final(&poly_ctx, key_established_mac);

}

  

if (crypto_verify16(recv_mac, key_established_mac) != 0) {

crypto_wipe(enc_key, KEY_SIZE);

print_error("Handshake MAC mismatch");

return -1;

}

  

struct __attribute((packed)) {

receive_response_t ciphertext;

uint8_t mac[POLY1305_SIZE];

} msg;

  

memset(&msg, 0, sizeof(msg));

  

// uint8_t mac_buffer[POLY1305_SIZE] = {0};

  

read_file(read_slot, &msg.ciphertext.len, &msg.ciphertext.file, &msg.ciphertext.hdr);

  

memcpy(msg.ciphertext.uuid, shadow_FAT[read_slot].uuid, UUID_SIZE);

  

encrypt_aead(enc_key, &msg.ciphertext, msg.mac, NULL, 0, &msg.ciphertext, sizeof(receive_response_t));

crypto_wipe(enc_key, KEY_SIZE);

  

write_packet(TRANSFER_INTERFACE, RECEIVE_MSG, &msg, sizeof(msg));

break;

}

default:

print_error("Bad message type");

return -1;

}

  

// Blank success message

write_packet(CONTROL_INTERFACE, LISTEN_MSG, NULL, 0);

return 0;

}