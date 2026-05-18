Certo — quella lista “System Overview” è, di fatto, la **mappa dei pezzi del sistema eCTF 2026** e di come interagiscono tra loro. Te la spiego voce per voce, con “che cos’è”, “a cosa serve” e “cosa ci fai in pratica”.

---

## Reference Design

È il **progetto di esempio** fornito dagli organizzatori: compila, gira sulla board, e **rispetta tutti i Functional Requirements**, ma **non implementa sicurezza** (quindi non soddisfa i Security Requirements). Serve come base/guida per capire struttura repo, build, toolchain e flusso di lavoro. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/reference_design.html "Reference Design — 2026 eCTF 2026.01.14 documentation"))

Cose importanti che mostra:

- Come organizzare l’ambiente di build in **Docker** (dipendenze, toolchain, ecc.). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/reference_design.html "Reference Design — 2026 eCTF 2026.01.14 documentation"))
    
- Dove e come si genera il materiale di “deployment” tipo i **Global Secrets** tramite `gen_secrets.py` (nel reference non fa “vera” sicurezza, ma ti mostra il meccanismo). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/reference_design.html "Reference Design — 2026 eCTF 2026.01.14 documentation"))
    
- Include librerie “utility” che astraggono cose low-level e semplificano la vita a chi è nuovo. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/reference_design.html "Reference Design — 2026 eCTF 2026.01.14 documentation"))
    

---

## eCTF Tools

Sono gli **strumenti host ufficiali** (CLI) con cui il tuo PC parla sia con l’HSM sia col bootloader e col testing service. L’idea è: _interfaccia standard uguale per tutti_, così il tuo lavoro si concentra sul firmware, non sugli script lato PC. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))

Punti chiave:

- Sono pubblicati su **PyPI** e il modo supportato per usarli è tramite **uv** (es. `uvx ectf --help`). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))
    
- Hanno “sottocomandi” principali:
    
    - `ectf tools`: comandi per usare le funzionalità dell’HSM (list/read/write/listen/interrogate/receive, ecc.). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))
        
    - `ectf hw`: comandi per parlare con il **bootloader** (es. start app, query digest, ecc.). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))
        
    - `ectf api`: comandi per interagire con la **web API**/testing infrastructure. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))
        
- Gli host tools che parlano col device sono **scritti dagli organizzatori**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

---

## eCTF Bootloader

È il bootloader MITRE “di gara” che fa da **strato di avvio/controllo** per le applicazioni. Nel Getting Started ti fanno usare l’**Insecure Bootloader** (non protetto) perché ti permette di sviluppare binari compatibili con quello “protetto” che userai nella Attack Phase. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/bootloader.html "eCTF Bootloader — 2026 eCTF 2026.01.14 documentation"))

Dettagli pratici:

- Il **Reference Design funziona solo** con il bootloader eCTF, quindi devi usarlo anche tu durante lo sviluppo. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/bootloader.html "eCTF Bootloader — 2026 eCTF 2026.01.14 documentation"))
    
- Le board “Design Phase” che ricevi **non lo includono** già flashato: devi scaricarlo e flasharlo. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/bootloader.html "eCTF Bootloader — 2026 eCTF 2026.01.14 documentation"))
    
- Per flasharlo usi **TI Uniflash** e scegli device MSPM0L2228 + connessione XDS110, poi carichi `insecure.out`. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/bootloader.html "eCTF Bootloader — 2026 eCTF 2026.01.14 documentation"))
    
- Poi, durante sviluppo, per interagire col bootloader usi `ectf hw ...` (strumenti ufficiali). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/ectf_tools.html "eCTF Tools — 2026 eCTF 2026.01.14 documentation"))
    

---

## eCTF API

È una **web API** (servizio remoto) che abilita tooling automatizzato: in particolare, l’infrastruttura di testing/validazione che verifica che il tuo design rispetti i **Functional Requirements**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/api.html "eCTF API — 2026 eCTF 2026.01.14 documentation"))

Concetti importanti che compaiono in quella pagina:

- L’API è usata dal testing service; gli organizzatori forniscono anche un **client Python** dentro i tool pubblici per interagirci. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/api.html "eCTF API — 2026 eCTF 2026.01.14 documentation"))
    
- La pagina spiega termini come **Flows** (pipeline completa: test/submit/scenario remoto…) e **Jobs** (step dentro un flow, con dipendenze). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/api.html "eCTF API — 2026 eCTF 2026.01.14 documentation"))
    
- Ogni team ha un **token privato di autorizzazione** da includere nelle richieste. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/api.html "eCTF API — 2026 eCTF 2026.01.14 documentation"))
    

---

## Host Computer

È semplicemente **il tuo laptop/desktop** (macchina “normale”) che:

- parla con l’HSM via **seriale**,
    
- usando gli **eCTF Tools** per invocare i comandi (list/read/write…),
    
- e legge in output status e dati. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

Nota di filosofia: per “semplificare il sistema”, tutti gli host tools che parlano col device sono forniti dagli organizzatori. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))

---

## Hardware Security Module (HSM)

È **il pezzo principale** che il tuo team deve progettare/rafforzare. L’HSM:

- conserva file (nome, permission group, UUID, contenuto) in slot,
    
- e trasferisce file/metadata ad altri HSM. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

Interfacce (fondamentali per capire l’architettura):

- **Management Interface**: è l’interfaccia “utente → HSM” (tipicamente da host computer), e la maggior parte delle azioni è protetta da **PIN**. La comunicazione segue il protocollo dei Functional Requirements. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- **Transfer Interface**: è separata fisicamente dalla management; serve per **HSM ↔ HSM** quando fai listen/interrogate/receive. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

Permessi (il “cuore” del threat model):

- Ogni file appartiene a un **permission group**, e ogni HSM ha per ogni gruppo un set di permessi (R/W/Receive). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- Receive: abilita a ricevere file di quel gruppo da un altro HSM (se non ce l’hai, l’altro dovrebbe rifiutare). ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- Write: abilita a creare/aggiornare file per quel gruppo. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- Read: abilita a restituire contenuti verso l’utente via management interface; importante: “stoccare” un file non implica necessariamente poterlo leggere. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

---

## Development Resources

È l’elenco delle **risorse fisiche** che ti forniscono per lavorare:

- **3 board “un-keyed” (Design Phase)**: per sviluppare e testare localmente. Non possono eseguire i design “Attack Phase” provisionati dagli organizzatori, ma puoi usarle per provare attacchi su binari compilati localmente da sorgenti. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- **3 board “keyed” (Attack Phase)**: sono predisposte per caricare in modo sicuro i design degli altri team durante l’Attack Phase; proprio per questo **non sono utilizzabili in Design Phase**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- **4 debugger XDS110-ETP-EVM**: per programmare/comunicare/debuggare la board. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    
- **jumper wires**: sia per collegare debugger↔board sia per collegare **UART tra due HSM**. ([rules.ectf.mitre.org](https://rules.ectf.mitre.org/2026/system/index.html "System Overview — 2026 eCTF 2026.01.14 documentation"))
    

---

Se vuoi, posso anche collegare i puntini con un flusso “tipo” in 8 righe (da _accendo la board_ a _testo con API_ a _pronto per handoff_), usando esattamente questi componenti.