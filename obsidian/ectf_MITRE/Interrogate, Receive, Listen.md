# Interrogate
- [x]  check PIN
- [x] generazioni chiavi effimere per handshake 
- [x] Determinare i gruppi interrogabili
- [x] Messaggio 1
- [x] messaggio 2
- [ ] derivazione shared secret + enc_key
	- tu aggiorni Blake2b solo con `&recv_groups[0]` (un solo group) e non con tutti i gruppi. Il documento parla di `GroupID1 || ... || GroupIDn`.
	- (Questa è una differenza importante, ma ti sto solo spiegando cosa fa, non “cosa cambiare” ancora.)
- [x] Verifica MAC
- [x] se Mac ok: calcolare key_established_mac (fase"0||...")
- [x] Preparar signed requests (una per gruppo)
- [x] Messaggio 3
	- PARZIALE
- [x] Messaggio 4
- [x] Decifrare e restituire all'host
- [ ] Error path




---
## signed requests
l’HSM locale deve mandare al remoto:
`signed_request_i = Sig(private_receive_key, GroupID || BoardID || A_pub || B_pub)`
mi serve --> crypto_ed25519_sign
quindi
`#include "monocypher-ed25519.h"`

## Salvare il pin prima della wipe
il documento chiede 
`private_receive_key = D(H(PIN || Kstore), private_receive_enc)`

## Helper: trova la permission entry del gruppo
















---
---
----
# Receive

- pin protetto
- serve a 
		- leggere un file da **una board vicina** via **UART1** (transfer interface)
	- e salvarlo in uno slot locale, **solo se** la board locale ha permesso di _receive_ per il gruppo di quel file.
### A prima parte
- **Host → A (Management UART)**: `Receive` con body `PIN(6) | ReadSlot(1) | WriteSlot(1)`.
- **A**: verifica PIN (hash con `Ksalt`, compare con `stored_pin`, e in caso negativo dorme ~5s).
- **A**: genera un **ephemeral x25519**:
	- private_exponent = gen_key()
	- A_pub = x25519_public_key(private_exponent)
- **A → B (UART1)**: manda un messaggio con almeno:
	- ReadSlot
	- `GroupID` (nel design appare nel “send message(read slot, group ID, public key)”)
	- A_pub
- **B → A (UART1)**: risponde con:
	- BoardID_B
	- `B_pub` (public key di B per lo scambio)
	- mac1 = MAC(enc_key, 1 || GroupID || BoardID_B || A_pub || B_pub)
- **A**: calcola `raw_shared_secret = x25519(private_exponent, B_pub)` e poi deriva:
	- enc_key = PRF(Ksession, GroupID || BoardID_B || A_pub || B_pub || raw_shared_secret)
- **A**: ricalcola `derived_mac = MAC(enc_key, 1 || GroupID || BoardID_B || A_pub || B_pub)` e confronta con `mac1`. Se non match → fail (+sleep).

### Seconda parte: richiesta firmata + consegna file
- **A**: crea `mac0 = MAC(enc_key, 0 || GroupID || BoardID_B || A_pub || B_pub)` (nel doc “key established mac”).
- **A**: decripta la **private receive key** dal “key store” PIN-protetto:
	- `Sprv_group,c = D(H(PIN||Kstore), private_receive_enc)`
- **A**: firma una richiesta:
	- signed_request = Sig(Sprv_group,c, GroupID || BoardID_B || A_pub || B_pub)
- **A → B (UART1)**: manda `mac0` + `signed_request`.
- **B → A (UART1)**: se tutto ok, invia **il file + metadata** (nel doc: “encrypted version of the file and metadata”).
- **A**: verifica la **firma del file** con la public write key (PIN-protetta) e salva nello `WriteSlot`.



---
---
---
# Funzioni comuni
- [ ]  Costruzione lista gruppi “receive-permitted” (comune, ma Receive di solito userà 1 group)
- [ ] Derivazione `enc_key` (PRF) e MAC transcript (uguale)
- [ ] Messaggi “Hello / response” su TRANSFER_INTERFACE (uguale pattern)
- [ ] Key-store + firma richiesta (riusabile)
- [ ] Pattern “handshake completo” come funzione unica (massimo riuso)

---
## Come appare il refactor nei due comandi (a grandi linee)

### `interrogate()`

1. `pin_copy_check_and_wipe(...)`
2. `n = get_receive_groups(...)`
3. `establish_session_key_interrogate(enc_key, pin, groups, n, ...)`
4. `read_packet()` ciphertext list
5. `decrypt list with enc_key`
6. wipe `enc_key`, return host
### `receive()`

1. `pin_copy_check_and_wipe(...)`
2. `establish_session_key_receive(enc_key, pin, read_slot, &gid, ...)`
3. `read_packet()` file package
4. `decrypt public_write_key` + `verify signature`
5. `has_receive_permission(gid)` (locale)
6. `write_file(write_slot, ...)`
7. wipe `enc_key`, return host

----
---
---
# Listen
- 