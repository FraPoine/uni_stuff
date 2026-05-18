# 📘 MITRE eCTF 2026 — REGOLAMENTO COMPLETO (SCHEMA TOTALE)

---

## 1️⃣ Cos’è l’eCTF

- Competizione di **sicurezza embedded**
- Organizzata da **MITRE**
- Ogni team:
    - progetta un **Hardware Security Module (HSM)**
    - lo consegna (Handoff)
    - lo difende
    - attacca quelli degli altri

---

## 2️⃣ Timeline (macro-fasi)

### 🟦 Design Phase

- Studio del sistema
- Implementazione HSM
- Design Phase Flags
- Debugger Flag
- Design Document
- Preparazione Handoff

### 🟧 Handoff

- Submission formale
- Test automatici MITRE
- Accepted → entra in Attack Phase
- Rejected → fix e nuova submission (se in tempo)

### 🟥 Attack Phase

- Attacchi offensivi
- Difesa passiva
- Accumulo punti
- Validazione flag

### 🟩 Post-gara

- Documentation Points
- Poster Session
- Award Ceremony

---

## 3️⃣ Architettura generale del sistema

### Componenti principali

- **Reference Design**
- **eCTF Tools** (CLI ufficiali)
- **eCTF Bootloader**
- **eCTF API**
- **Host Computer**
- **Hardware Security Module (HSM)**
- **Development Resources (board, debugger)**

---

## 4️⃣ Hardware

- Board ufficiale: **MSP-LITO-L2228**
- MCU Cortex-M0+
- Flash + RAM limitate
- Comunicazione:
    - Host ↔ HSM (management interface)
    - HSM ↔ HSM (transfer interface, UART)

---

## 5️⃣ Reference Design

- Firmware di esempio
- Funziona ma **non è sicuro**
- Serve per:
    - capire struttura
    - toolchain
    - flusso Docker
    - interfacce

---

## 6️⃣ Tooling obbligatorio

### eCTF Tools

- CLI ufficiale (via `uv`)
- Nessun tool custom lato PC
- Comandi:
    - gestione HSM
    - bootloader
    - testing service
    - API
### Docker

- Build **obbligatoria**
- Ambiente riproducibile
- Usato da MITRE in Handoff

### OpenOCD / Debug

- Debug hardware
- Richiesto per Debugger Flag
- Essenziale per Attack Phase

---

## 7️⃣ Bootloader eCTF

- Fornito da MITRE
- Gestisce avvio, layout flash, digest
- Reference + design devono essere compatibili
- Versione “insecure” in Design Phase
- Versione protetta in Attack Phase

---

## 8️⃣ HSM — Modello funzionale

### File system HSM
- Max **8 file**
- Ogni file ha:
    - UUID (16 byte)
    - Nome (≤32 byte)
    - Contenuto (≤8192 byte)
    - Permission Group
### Permission Groups

- Max 32
- Permessi:
    - R = Read
    - W = Write
    - C = Receive

---

## 9️⃣ Functional Requirements (OBBLIGATORI)

⚠️ **Testati in Handoff**

### Comandi richiesti (6)

1. List files (PIN)
2. Read file (PIN + R)
3. Write file (PIN + W)
4. Listen (NO PIN)
5. Interrogate (PIN)
6. Receive file (PIN + C)

### Requisiti chiave

- Persistenza su power loss
- Output esatto
- Parsing robusto
- Error handling corretto

### Timing massimi

- Wake: 1s
- List: 500ms
- Read: 1s
- Write: 1s
- Interrogate: 1s
- Receive: 2s
- **PIN errato: 5s obbligatori**

---

## 🔟 Host Interface

- Protocollo **rigido**
- Host tools forniti da MITRE
- Firmware deve adattarsi al protocollo
- Input potenzialmente malevolo → da gestire

---

## 1️⃣1️⃣ Security Requirements (NON testati in Handoff)

⚠️ **Violazioni = flag Attack Phase**

### SR1 — Permessi
- Nessuna azione senza permesso corretto
- Nessuna info leakage

### SR2 — PIN
- Nessuna operazione senza PIN
- PIN non deve trapelare
- Anti-bruteforce (delay)

### SR3 — Integrità

- File ricevuti:
    - autentici
    - integri
    - da HSM validi

---

## 1️⃣2️⃣ Detailed Specifications

- PIN: 6 hex lowercase
- Permission string build-time
- Limiti dimensionali rigidi
- Flash layout fisso
- Linguaggi ammessi:
    - C
    - C++
    - Rust

---

## 1️⃣3️⃣ Flags — come si fanno punti

### Design Phase Flags
- Apprendimento
- Setup
- Comprensione sistema
- Deadlines → punti parziali se tardi

### Design Document
- PDF
- Architettura
- Threat model
- Scelte di sicurezza

### Debugger Flag
- Uso reale di debugger
- Analisi stato interno

---

## 1️⃣4️⃣ Attack Phase Flags

### Tipologie
- Read/Steal senza permesso
- PIN bypass
- Integrity compromise
- Backdoor
### Regole
- Flag da spiegare
- No condivisione flag
- Attacchi solo su target validi

---

## 1️⃣5️⃣ Scoring

### Difensivo
- Punti passivi finché non vieni bucato
- Prima entri → più punti

### Offensivo
- Capture flag
- Valore condiviso tra team
- Possibili riduzioni se altri catturano dopo

### Extra
- Documentation Points
- Poster Session

---

## 1️⃣6️⃣ Remote Scenario

- Attacchi via infrastruttura MITRE
- Nessun accesso fisico
- Simula attaccante reale remoto

---

## 1️⃣7️⃣ Handoff (CRITICO)

### Automated Testing Service
- Clona repo
- Build Docker
- Provision secrets
- Flash
- Test Functional Requirements

### Submission

- Repo completo
- Dockerfile valido
- Nessun segreto hardcoded
- PDF richiesti

---

## 1️⃣8️⃣ Accepted Design

- Test superati
- Creazione Handoff Package
- Approvazione finale team
- **Design congelato**
- Ingresso Attack Phase   

---

## 1️⃣9️⃣ Rejected Design

- Report errore
- Fix possibile
- Nuova submission (se in tempo)
- Perdita punti difensivi per ritardo

---

## 2️⃣0️⃣ Regole disciplinari chiave

- No flag sharing → squalifica
- No offuscamento submission
- No bricking device
- Solo hardware ufficiale
- Tutto il lavoro deve essere del team
- AI consentita, responsabilità del team

---
