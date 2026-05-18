# Timeline degli sprint

## Sprint 1 — Setup, design e documenti

**Obiettivo:** organizzare il lavoro prima di iniziare lo sviluppo vero e proprio.

**Attività principali:**
- Definire l’idea finale del progetto
- Scrivere la proposta iniziale
- Preparare i documenti funzionali
- Definire cosa deve fare il sistema
- Scegliere i personaggi / dataset
- Preparare i mockup dell’interfaccia
- Definire architettura, data model e piano di valutazione
- Organizzare repository, milestone e issue

**Output attesi:**
- `docs/proposal.md`
- `docs/functional_spec.md`
- `docs/data_model.md`
- `docs/evaluation_plan.md`
- Mockup UI
- Sprint plan iniziale

---

## Sprint 2 — Minimum Viable Build tecnico

**Obiettivo:** costruire una prima pipeline minima end-to-end.

**Attività principali:**
- Implementare l’estrazione delle persona
- Creare i primi persona JSON
- Implementare il runtime base degli agenti
- Far generare risposte a 2 personaggi
- Salvare transcript e log
- Preparare una prima configurazione eseguibile

**Output attesi:**
- `extract_persona.py`
- `agent_runtime.py`
- `simulate_chat.py`
- Prime persona JSON
- Prima chat simulata tra 2 personaggi
- Logging minimo funzionante

---

## Sprint 3 — Simulazione completa

**Obiettivo:** estendere il sistema da prototipo minimo a simulazione multi-agente utilizzabile.

**Attività principali:**
- Aumentare il numero di personaggi
- Simulare conversazioni tra più agenti
- Aggiungere configurazioni per topic, seed, modello e numero di turni
- Versionare i prompt
- Migliorare logging e riproducibilità
- Preparare una UI o CLI minimale

**Output attesi:**
- 6–8 persona JSON
- Simulazioni multi-agente complete
- Prompt in `prompts/`
- Configurazioni in `configs/`
- Log strutturati
- Sistema eseguibile da comando

---

## Sprint 4 — Evaluation e raccolta dati

**Obiettivo:** costruire e avviare la valutazione del comportamento delle persona generate.

**Attività principali:**
- Generare snippet anonimi dalle conversazioni
- Preparare una blind evaluation
- Creare Google Form o mini-UI per i rater
- Definire le condizioni di valutazione
- Raccogliere risposte dai valutatori
- Salvare i dati in formato analizzabile

**Output attesi:**
- Dataset di snippet anonimi
- Form o interfaccia di valutazione
- Risposte dei rater
- File dati per l’analisi
- Prima verifica della qualità delle persona

---

## Sprint 5 — Analisi, findings e report draft

**Obiettivo:** analizzare i risultati e trasformarli in findings difendibili.

**Attività principali:**
- Calcolare accuracy complessiva
- Calcolare accuracy per personaggio
- Costruire confusion matrix
- Confrontare condizioni diverse, se presenti
- Calcolare intervalli di confidenza
- Analizzare errori e failure mode
- Scrivere una prima bozza del report

**Output attesi:**
- `analyze.py`
- Grafici e tabelle dei risultati
- Confusion matrix
- Findings principali
- Bozza del report tecnico
- Discussione preliminare dei limiti

---

## Sprint 6 — Report finale e presentazione

**Obiettivo:** preparare la consegna finale e rendere il progetto presentabile e riproducibile.

**Attività principali:**
- Finalizzare il report
- Preparare la presentazione finale
- Pulire README e documentazione
- Verificare che il progetto sia eseguibile da zero
- Preparare una demo stabile
- Sistemare repo, log, dati e grafici
- Provare la presentazione

**Output attesi:**
- Report tecnico finale
- Slide deck da 15–20 minuti
- README completo
- Demo funzionante
- Codice e dati organizzati
- Repo pronto per la consegna