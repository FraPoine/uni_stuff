## 🎯 **Obiettivo del Documento**

Fornire linee guida preliminari per l’approvazione e l’utilizzo sicuro di applicazioni di **machine learning (ML)** nei sistemi aeronautici di **livello 1** (assistenza all’uomo) e **livello 2** (cooperazione uomo-macchina), in vista dello sviluppo di un futuro quadro normativo formale.

---
## 🧱 **AI Trustworthiness Guidelines (Capitolo C)**

Le linee guida si fondano su quattro sezioni principali:
### 🔹 **C.1 – Purpose and Applicability**

Stabilisce l'ambito d'applicazione:
- Destinata a **sistemi safety-related** o per **protezione ambientale**.
- Si applica **solo** a:
    - **AI di Livello 1 e 2** (non ancora al Livello 3).
    - **Apprendimento supervisionato**.
    - **Modelli “frozen”**, non aggiornabili in volo o online.
        
Domini coperti:
- Airworthiness (progettazione/sicurezza dei velivoli)
- Operazioni di volo
- ATM/ANS
- Manutenzione
- Addestramento
- Aerodromi 
- Impatti ambientali

### 🔹 **C.2 – Trustworthiness Analysis**
#### **C.2.1 – Caratterizzazione del sistema AI**
- Identificare utenti finali e i **task** ad essi associati.
- Definire il sistema AI e **funzioni ad alto livello**.
- Definire il **Concept of Operations (ConOps)**:
    - Scenario operativo.
    - Divisione dei compiti uomo-AI.
    - Limitazioni operative.
    - Rischi previsti e mitigazioni.
- Definire l’**Operational Domain (OD)** e successivamente l’**ODD** a livello dei componenti ML.
- Coinvolgimento degli utenti finali nella progettazione.
#### **C.2.2 – Safety Assessment**
- Due livelli:
    - **Valutazione iniziale della sicurezza** (progettazione, architettura).
    - **Valutazione continua della sicurezza** (dati operativi, monitoraggio).
- Gli errori nei modelli AI sono trattati come **common cause** di fallimento.
- Non si assume affidabilità software: serve garanzia tramite metodologia e dati.
#### **C.2.3 – Information Security**
- Identificare i requisiti di sicurezza informatica specifici per ML.
- Focus su:
    - Integrità dei dati di addestramento.
    - Resistenza ad attacchi avversari (adversarial examples).
    - Gestione accessi e aggiornamenti.
#### **C.2.4 – Valutazione Etica**
- Ispirata alle **linee guida etiche AI dell’UE**.
- Assicura:
    - Equità, non discriminazione.
    - Governance dei dati.
    - Trasparenza e responsabilità.
### 🔹 **C.3 – AI Assurance**
#### **C.3.1 – Learning Assurance**
- Approccio alternativo allo sviluppo tradizionale (requirements-based).
- Richiede:
    - **Gestione dei dati**: raccolta, qualità, bias, rappresentatività.
    - **Validazione e verifica**: performance su dati non visti.
    - **Documentazione dell’intero processo di apprendimento**.
#### **C.3.2 – Explainability**
- Due prospettive:
    - **Sviluppo/Post-ops**: per ingegneri, autorità, investigatori.
    - **Operativa**: per l’utente finale in volo o al controllo.
- Dev’essere:
    - **Comprensibile**, **affidabile**, **rilevante** e **tempestiva**.
### 🔹 **C.4 – Human Factors for AI**
Focalizzato su Human-AI Teaming (**HAT**), in particolare:
- **Explainability Operativa**: supporto comprensibile durante l’uso.
- **Cooperazione (Level 2A)**: AI supporta l’utente sotto supervisione.
- **Collaborazione (Level 2B)**: AI e umano condividono obiettivi e si adattano a vicenda.
- Design centrato sull’utente:
    - **Interfacce intuitive**
    - **Gestione errori**
    - **Modularità dell’interazione**
### 🔹 **C.5 – AI Safety Risk Mitigation**
- Accetta che il “black box effect” **non può sempre essere risolto**.
- Richiede:
    - **Strategie architetturali** per mitigare i rischi residui.
    - **Monitoraggio attivo** delle prestazioni operative.
    - **Contromisure a valle** (es. override umano, ridondanza).
---
## 🔢 **Classificazione delle Applicazioni AI (Livelli)**

- **Livello 1A**: supporto all’acquisizione e analisi dell’informazione (es. visualizzazione migliorata).
- **Livello 1B**: assistenza alla decisione umana.
- **Livello 2A**: cooperazione uomo-AI (decisioni automatiche ma completamente supervisionabili).
- **Livello 2B**: collaborazione uomo-AI (interazione bidirezionale, obiettivi condivisi, delega parziale dell’autorità).
- **Livello 3 (non coperto in questo documento)**: maggiore autonomia dell’AI, fino alla decisione non supervisionabile.

---
## 🧠 **Concetti Innovativi Introdotti**

- **Learning Assurance**: verifica della correttezza/completezza dei dati di addestramento e generalizzazione del modello.
- **Explainability**:
    - **Sviluppo & Post-Operazioni**: trasparenza per sviluppatori e autorità.
    - **Operativa**: comprensione delle decisioni da parte dell’utente finale.
- **OD/ODD** (Operational Domain / Operational Design Domain): definizione formale dei contesti in cui il sistema AI è progettato per operare.
- **Human-AI Teaming (HAT)**: cooperazione e collaborazione uomo-macchina, con enfasi su ruoli, autorità, situational awareness e interfacce.

---
## 🔐 **Aspetti di Sicurezza e Certificazione**

- Il documento fornisce **obiettivi e MOC (Means of Compliance)** attesi per AI-based systems nei seguenti domini:
    - **Airworthiness** (progettazione e certificazione)
    - **Operazioni di volo**
    - **ATM/ANS**
    - **Manutenzione**
    - **Formazione (Training/FSTD)**
    - **Aerodromi**
    - **Protezione ambientale**

---

## 🧪 **Esempi di Use Case Trattati**

Allegato F contiene numerosi casi d’uso pratici, tra cui:
- Sistemi di atterraggio visivo basati su AI.
- Assistenza radio per piloti.
- Predizione di traiettorie 4D.
- Ispezioni predittive e rilevamento danni (manutenzione).
- Rilevamento FOD negli aeroporti.
- Valutazione automatica della performance nei simulatori.
- Stima emissioni motore e impatti ambientali.

---
## 📏 **Proporzionalità e Applicabilità**

- Gli obiettivi possono essere **modulati** in funzione del livello di AI e della criticità della funzione (e.g. DAL/SWAL).
- Il documento si **applica solo a tecniche supervisionate** e a modelli **non adattivi** (modello “frozen” al momento dell’approvazione).

---
## 🧭 **Finalità**

Il documento è **non vincolante**, ma serve da riferimento per:

- Costruttori e operatori che vogliono proporre soluzioni AI.
- Autorità di certificazione.
- Preparazione ai regolamenti futuri sull’AI in ambito UE.