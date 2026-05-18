Certo — ho letto la documentazione “2026 eCTF” sul sito che hai linkato e qui sotto trovi una spiegazione **organica, completa e “da regolamento”** (con i punti chiave tecnici) di come funziona l’eCTF 2026 e quali vincoli devi rispettare.

---

## 1) Cos’è l’eCTF 2026 e come è strutturato

L’Embedded CTF (eCTF) di MITRE è una competizione di sicurezza embedded in cui i team **progettano e implementano** un sistema “sicuro” (Design Phase), lo consegnano per verifica funzionale (Handoff) e poi lo **attaccano/difendono** contro gli altri (Attack Phase). Le date generali 2026 indicate sul sito: **14 gennaio → 15 aprile** (chiusura scoreboard) con **cerimonia premi il 24 aprile**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/index.html "Welcome to the 2026 eCTF! — 2026 eCTF 2026.01.14 documentation"))

---

## 2) Timeline e fasi (con date)

Dal calendario ufficiale:

- **14 gennaio 2026**: kickoff e inizio **Design Phase**
    
- **25 febbraio 2026**: inizio **Handoff** (finestra di consegna/validazione)
    
- **15 aprile 2026**: chiusura **Scoreboard** (niente più flag accettate)
    
- **22 aprile 2026**: Poster Session (virtuale)
    
- **24 aprile 2026**: Award Ceremony (ibrida, Bedford MA + online) ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/schedule/index.html "Schedule — 2026 eCTF 2026.01.14 documentation"))
    

---

## 3) Come si fanno punti (scoring)

Il sistema punti è diviso in tre “famiglie”:

### A) Design Phase Points

- Punti tramite **Design Phase Flags**: sfide/checkpoint; punteggio pieno se entro la scadenza, parziale se in ritardo. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    
- Punti tramite **Bug Bounty** sulla reference design: trovare bug + proporre fix. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    

### B) Attack Phase Points

È dove si fa la maggior parte dei punti:

- **Defensive points**: appena passi Handoff e entri in Attack Phase, inizi ad accumulare punti “passivi” **per ogni attack-flag non ancora catturata** dagli altri. Quando una flag viene catturata, i punti già accumulati restano, ma **non cresce più**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    
- **Offensive points**: catturi le flag degli altri team. Qui c’è una particolarità importante: il valore di una flag è gestito a “quote/shares” e **può succedere che il tuo punteggio scenda** se dopo di te altri team catturano la stessa flag (perché la “torta” si redistribuisce). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    
- Novità 2026: rimosso il **“First Capture Bonus”** (non c’è più il premio extra per il primissimo capture), ma resta l’incentivo alla velocità tramite il meccanismo di “shares”. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    

### C) Miscellaneous points

- **Documentation Points** (assegnati dopo, su scala, legati a chiarezza di codice e doc)
    
- Punti Poster Session e altre opportunità annunciate dagli organizzatori ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/about/scoring_system.html "Scoring System — 2026 eCTF 2026.01.14 documentation"))
    

---

## 4) Regole “disciplinari” (Rules) — cosa è permesso/proibito

Queste sono le regole generali vincolanti (violazioni = penalità o squalifica):

1. Devi rispettare **anche** leggi locali e policy del tuo ateneo/organizzazione. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
2. Tutti (advisor incluso) devono aver firmato il **Participant Agreement**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
3. MITRE può aggiornare/chiarire regole e requisiti in qualunque momento. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
4. In **Handoff** devi condividere **tutto**: sorgenti + documentazione. Sarà condiviso con i team attaccanti (niente “security by obscurity”). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
5. **No offuscamento intenzionale** nella submission (codice o doc). In particolare: non puoi usare linguaggi fuori da quelli consentiti senza approvazione. (Obfuscation compile-time o run-time “come tecnica difensiva” è esplicitamente ammessa; qui il divieto è sull’offuscamento deliberato della submission per renderla incomprensibile.) ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
6. Puoi attaccare **solo** i sistemi designati come target e **solo** durante Attack Phase. Strumenti/infrastrutture MITRE e bootloader MITRE sono **fuori scope**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
7. Ogni flag catturata in Attack Phase va **validata** inviando una breve descrizione dell’attacco, abbastanza dettagliata da permettere al defender di correggere. MITRE può rimuovere punti se non validata entro fine competizione. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
8. **Vietatissimo condividere flag tra team**: squalifica immediata. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
9. Il design **non può “brickare”** permanentemente se rileva un attacco. È ammessa una **penalty delay di 5 secondi** se rilevi comportamento da attacco (anche persistente fra power-cycle). Se invece rilevi instabilità/corruzione hardware puoi richiedere power-cycle (anche multipli finché sparisce). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
10. Devi usare **l’hardware/piattaforma fornita**: non puoi cambiare piattaforma in Design Phase. Puoi modificare hardware solo per aiutarti ad attaccare/sperimentare, ma ai test Handoff useranno hardware non modificato. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
11. Tutti i documenti consegnati devono essere **PDF**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
12. AI-assisted code generation: **permesso**, ma raccomandano di capire davvero cosa consegni (responsabilità tua). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
13. Tutto ciò che consegni deve essere fatto da membri registrati, con eccezioni: reference design, OSS attribuito correttamente, materiale condiviso dagli organizzatori o su canali pubblici Zulip, e snippet banali senza impatto sostanziale. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
14. Se passano design non perfettamente compliant e viene scoperto dopo: gli organizzatori decidono la risoluzione (da “ok senza penalty” fino a penalità/espulsione se intenzionale). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    
15. IP: il design è tuo, ma lo condividi per la gara; la licenza nel repo governa usi fuori gara; MITRE non fa enforcement ma chiede rispetto reciproco. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/rules.html "Rules — 2026 eCTF 2026.01.14 documentation"))
    

---

## 5) Specifiche tecniche obbligatorie (il “cuore” della gara 2026)

Il sistema 2026 ruota attorno a un **Hardware Security Module (HSM)** che gestisce **file** con gruppi e permessi, e può comunicare con un “neighbor HSM” via UART per interrogare/ricevere file. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))

### 5.1 Requisiti funzionali (testati in Handoff)

I functional requirements sono verificati dagli organizzatori durante Handoff: se non li rispetti, **non passi**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))

**Build / provisioning (obbligatorio via Docker):**

- Devi avere un ambiente di build basato su **Docker** (eseguono `docker build -t build-hsm .`). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- Devi implementare una fase “deployment” con `gen_secrets.py` che genera i **Global Secrets** (trattati come read-only dopo generazione). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- Gli HSM si buildano in container; i secrets vengono montati read-only; ci sono variabili d’ambiente come `HSM_PIN` e `PERMISSIONS`. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- In Attack Phase gli attaccanti **non** hanno accesso ai Global Secrets. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    

**Comandi che il tuo HSM deve supportare (6):**

1. **List files** (protetto da PIN) → metadata di tutti i file
    
2. **Read file** (PIN + permessi di gruppo) → nome (padded) + contenuto
    
3. **Write file** (PIN + permessi) → sovrascrive slot; persistenza su power loss; max 8 file
    
4. **Listen** (non PIN) → modalità “ascolto” per gestire una richiesta dal vicino
    
5. **Interrogate** (PIN) → lista file del vicino filtrata da receive-permissions
    
6. **Receive file** (PIN) → riceve file dal vicino e lo scrive in slot se autorizzato ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    

### 5.2 Requisiti di sicurezza (NON testati in Handoff, ma “testati” dagli attacchi)

Qui la logica è: non ti bocciano in Handoff se sei insicuro, ma gli altri ti fanno punti.

- **SR1**: un attaccante non deve riuscire a fare azioni sui file senza un HSM valido e con permessi corretti (read/write/receive; e interrogate deve rispettare i receive permissions). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/security_reqs.html "Security Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- **SR2**: nessuna azione protetta da PIN deve essere completabile senza conoscere il PIN; il PIN non deve trapelare. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/security_reqs.html "Security Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- **SR3**: un HSM non deve accettare file “ricevuti” che non provengano da un HSM valido con write permission; serve protezione dell’integrità dei file. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/security_reqs.html "Security Requirements — 2026 eCTF 2026.01.14 documentation"))
    

### 5.3 Specifiche di dettaglio (formati, limiti, timing)

Alcuni vincoli “duri”:

**PIN e permessi**

- PIN: **esattamente 6 caratteri** esadecimali lowercase (0-9, a-f). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))
    
- Permission string a build time (esempio `1234=RW-:aabb=RWC:1a2b=--C`):
    
    - lista separata da `:`
        
    - ogni entry `group_id=perm`
        
    - `group_id` = 16-bit esadecimale, 4 char senza `0x`
        
    - `perm` = 3 char con lettere per permessi presenti e `-` per assenti (R/W/C). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))
        

**Timing Requirements (importantissimo anche per la regola anti-brick e per penalità PIN)**

- Wake: 1s
    
- List: 500ms
    
- Read: 1000ms
    
- Write: 1000ms
    
- Receive: 2000ms
    
- Interrogate: 1000ms
    
- **Invalid PIN**: deve costare **5 secondi** ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))
    

**Dimensioni e limiti**

- Group ID: 16 bit
    
- UUID file: 16 byte
    
- Nome file: max 32 byte
    
- Contenuto: max 8192 byte
    
- Slot file: 8
    
- Gruppi supportati: 32 ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))
    

**Flash layout / FAT**  
C’è un vincolo di layout in flash (bootloader riservato, regioni APP1/APP2) e una **File Allocation Table** a indirizzo specifico (0x3a000) usata dal bootloader per calcolare digest crittografici. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))

**Linguaggi consentiti**  
Pre-approvati: **C, C++, Rust**. Se vuoi altro, devi chiedere approvazione. Inoltre, anche se usi linguaggi con panic handler, devi rispettare i timing e non finire in loop infinito su input “normali”. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/detailed_specs.html "Detailed Specifications — 2026 eCTF 2026.01.14 documentation"))

---

## 6) Flag e “cosa significa vincere/attaccare” nel 2026

### 6.1 Scenario Attack Phase

Lo scenario è “fictional” e introduce tre attori/ruoli (Technician HSM, Engineer HSM, Photolithography HSM) per definire un threat model coerente con i requisiti di sicurezza. I file sono categorizzati per “permission groups” (group ID). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/flags/attack_flags.html "Attack Phase Flags and Scenarios — 2026 eCTF 2026.01.14 documentation"))

### 6.2 Tipi di Attack Phase Flags (formati e obiettivo)

Le flag principali descritte sono:

- **Steal Design** `ectf{steal_*}`: ricevere un file senza avere receive permission
    
- **Read Update** `ectf{update_*}`: leggere un file senza read permission
    
- **Read Design** `ectf{design_*}`: leggere un file di design da un device di cui non hai il PIN
    
- **Compromise Machine** `ectf{compromise_*}`: far accettare al remoto un update corrotto
    
- **Backdoored Design** `ectf{backdoor_*}`: far accettare al remoto un design “backdoored” craftato ad hoc ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/flags/attack_flags.html "Attack Phase Flags and Scenarios — 2026 eCTF 2026.01.14 documentation"))
    

---

## 7) Handoff: cosa devi fare per “entrare” nell’Attack Phase

Da **25 febbraio** puoi sottomettere la design.

- Prima di sottomettere, devi passare i test con l’**Automated Testing Service** (durante Design Phase conviene usarlo spesso per non divergere dai functional requirements). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/handoff/index.html "Handoff — 2026 eCTF 2026.01.14 documentation"))
    
- Gli organizzatori clonano il repo, provisionano e fanno una batteria di test funzionali.
    
- Ti rispondono tipicamente **entro due business days** dicendo “accepted/rejected” e perché. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/handoff/index.html "Handoff — 2026 eCTF 2026.01.14 documentation"))
    
- Se accepted: viene creato un **handoff package** (codice + doc + artefatti Attack Phase). Tu lo approvi: è l’ultima occasione per controllare di non aver lasciato materiali sensibili nel repo. Dopo l’approvazione **non puoi più modificare** il design. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/handoff/index.html "Handoff — 2026 eCTF 2026.01.14 documentation"))
    
- L’ingresso in Attack Phase avviene tipicamente **due giorni** dopo la prima submission che passa, ma può variare. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/handoff/index.html "Handoff — 2026 eCTF 2026.01.14 documentation"))
    

---

## 8) Due “takeaway” pratici (se vuoi usarlo come checklist)

- Per **non farti bocciare in Handoff**: rispetta i Functional Requirements + i vincoli di build (Docker, packaging, interfacce) + formati/limiti/timing. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/functional_reqs.html "Functional Requirements — 2026 eCTF 2026.01.14 documentation"))
    
- Per **non farti distruggere in Attack Phase**: tratta i Security Requirements come “veri requisiti”, perché ogni falla diventa una flag per gli altri. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/specs/security_reqs.html "Security Requirements — 2026 eCTF 2026.01.14 documentation"))
    
