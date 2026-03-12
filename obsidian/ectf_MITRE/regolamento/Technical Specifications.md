Certo 🙂  
Questa sezione **“Technical Specifications”** è probabilmente **la più importante di tutto il regolamento**, perché definisce **che cosa il tuo HSM deve fare**, **come deve comunicarlo**, **che cosa deve impedire a livello di sicurezza** e **con quali limiti tecnici precisi**.  
Te la spiego in modo **strutturato, rigoroso ma leggibile**, distinguendo bene _cosa è obbligatorio per passare Handoff_ e _cosa invece serve per non farti bucare in Attack Phase_.

---

# 1) Functional Requirements

👉 **Cosa deve fare il tuo HSM per essere considerato “funzionante”**

Questi requisiti sono **testati automaticamente dagli organizzatori durante Handoff**.  
Se **anche uno solo fallisce → design rifiutato → niente Attack Phase**.

### Idea chiave

I Functional Requirements descrivono **l’API logica dell’HSM**, indipendentemente da come la implementi internamente.

---

## 1.1 Modello funzionale dell’HSM

Il tuo HSM è visto come un dispositivo che:

- mantiene fino a **8 file** persistenti;
    
- ogni file ha:
    
    - UUID (16 byte)
        
    - nome (max 32 byte)
        
    - contenuto (max 8192 byte)
        
    - permission group (group ID)
        
- espone **comandi ben definiti**, con input/output precisi;
    
- conserva i dati **anche dopo power loss**.
    

---

## 1.2 Comandi obbligatori (core)

Devi implementare **tutti e sei** questi comandi:

### 🔹 1. List Files

- **Protetto da PIN**
    
- Restituisce _solo metadata_ (UUID, nome, group ID, size)
    
- NON restituisce contenuti
    

👉 Serve a capire cosa c’è nell’HSM, ma non deve mai leakare dati sensibili.

---

### 🔹 2. Read File

- **Protetto da PIN**
    
- Richiede **Read permission** sul group ID
    
- Restituisce:
    
    - nome (padded)
        
    - contenuto completo
        

👉 Se non hai permesso → fallisce **senza rivelare nulla**

---

### 🔹 3. Write File

- **Protetto da PIN**
    
- Richiede **Write permission**
    
- Sovrascrive uno slot
    
- Deve essere **persistente**
    

👉 È qui che molti team sbagliano:  
_write riuscita + reset = file deve ancora esistere_.

---

### 🔹 4. Listen

- **NON protetto da PIN**
    
- Mette l’HSM in modalità di ascolto
    
- Serve solo per ricevere richieste da un altro HSM
    

👉 È intenzionalmente non protetto: la sicurezza va fatta _a livello di protocollo_.

---

### 🔹 5. Interrogate

- **Protetto da PIN**
    
- Chiede a un altro HSM la lista file
    
- Il remoto deve filtrare la risposta in base alle **Receive permissions**
    

👉 Non devi mai vedere file che non potresti ricevere.

---

### 🔹 6. Receive File

- **Protetto da PIN**
    
- Riceve un file da un altro HSM
    
- Il file deve essere scritto **solo se**:
    
    - il mittente è valido
        
    - hai Receive permission
        
    - il contenuto è integro
        

---

## 1.3 Timing requirements (fondamentali)

Ogni comando ha un **tempo massimo**:

|Operazione|Tempo max|
|---|---|
|Wake|1s|
|List|500 ms|
|Read|1000 ms|
|Write|1000 ms|
|Interrogate|1000 ms|
|Receive|2000 ms|
|**PIN errato**|**5 secondi obbligatori**|

👉 Se violi questi tempi:

- **test fallito**
    
- oppure exploit in Attack Phase
    

---

# 2) Host Interface

👉 **Come il PC parla con l’HSM**

Questa sezione definisce il **contratto di comunicazione** tra:

- **Host Computer** (tool eCTF)
    
- **HSM firmware**
    

---

## 2.1 Concetto chiave

Tu **non scrivi il software lato PC**.  
Devi **adattare il tuo firmware** al protocollo imposto.

👉 È fatto così apposta per:

- eliminare ambiguità
    
- rendere gli attacchi comparabili
    

---

## 2.2 Management Interface

È l’interfaccia:

> Host PC → HSM

Usata per:

- list
    
- read
    
- write
    
- interrogate
    
- receive
    

Caratteristiche:

- seriale
    
- framing rigido
    
- error codes standard
    
- parsing **robusto** (input malformati devono essere gestiti)
    

---

## 2.3 Transfer Interface

È l’interfaccia:

> HSM ↔ HSM

Usata solo per:

- listen
    
- interrogate
    
- receive
    

È:

- fisicamente separata
    
- più pericolosa
    
- principale vettore di attacco
    

👉 La sicurezza **non è data dall’interfaccia**, ma da ciò che ci fai sopra.

---

# 3) Security Requirements

👉 **Cosa NON deve mai essere possibile fare**

⚠️ **Non vengono testati in Handoff**  
⚠️ **Ma ogni violazione = flag per gli attaccanti**

---

## SR1 — Enforcement dei permessi

Un attaccante **non deve mai** poter:

- leggere senza Read
    
- scrivere senza Write
    
- ricevere senza Receive
    
- interrogare ottenendo info non autorizzate
    

👉 Anche _side-channel_ o errori diversi contano come violazione.

---

## SR2 — Protezione del PIN

- Nessuna operazione protetta deve riuscire senza PIN
    
- Il PIN non deve:
    
    - comparire in memoria leggibile
        
    - essere deducibile da timing
        
    - essere bypassabile
        

👉 Il delay di 5s sul PIN errato è **obbligatorio** proprio per prevenire brute-force.

---

## SR3 — Integrità dei file ricevuti

- Un file ricevuto deve essere:
    
    - autentico
        
    - integro
        
    - proveniente da un HSM valido
        

👉 Se accetti un file corrotto o spoofato → **compromise flag**.

---

# 4) Detailed Specifications

👉 **Tutti i vincoli “a vite stretta”**

Questa sezione elimina ogni ambiguità.

---

## 4.1 PIN

- Esattamente **6 caratteri**
    
- Solo **hex lowercase** (`0-9a-f`)
    
- Deve essere controllato **sempre**
    

---

## 4.2 Permission string (build-time)

Formato:

```
group_id=RW-
```

- group_id: 16 bit hex
    
- R = Read
    
- W = Write
    
- C = Receive
    
- `-` = permesso assente
    

👉 Parsing errato = comportamento indefinito = exploit.

---

## 4.3 Limiti dimensionali

- File name: 32 byte
    
- File size: 8192 byte
    
- File slots: 8
    
- Permission groups: 32
    

👉 **Mai allocare dinamicamente oltre questi limiti.**

---

## 4.4 Flash layout

- Bootloader: regione riservata
    
- App: due slot (A/B)
    
- FAT a indirizzo fisso (usata per hash/digest)
    

👉 Se rompi il layout → bootloader non carica → design morto.

---

## 4.5 Linguaggi consentiti

- C
    
- C++
    
- Rust
    

Con vincoli:

- niente loop infiniti su input valido
    
- panic gestiti
    
- timing rispettati
    

---

# 🧠 Come leggerla “da team”

Un modo corretto di usare questa sezione è:

- **Functional Requirements** → checklist per passare Handoff
    
- **Host Interface** → guida per il parsing & protocollo
    
- **Security Requirements** → threat model ufficiale
    
- **Detailed Specifications** → lista dei “non puoi sbagliare”
    

---

Se vuoi, nel prossimo messaggio posso:

- trasformare questa sezione in una **checklist di implementazione**
    
- oppure spiegarti **come i requisiti diventano flag reali in Attack Phase**
    
- oppure analizzare **errori tipici che portano a exploit**