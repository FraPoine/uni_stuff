Perfetto, questa è davvero **l’ultima sezione chiave** del regolamento, perché **Handoff è il “collo di bottiglia”**: tutto il lavoro fatto prima **vale zero** se qui qualcosa va storto.

Ti spiego **Handoff** in modo molto chiaro, seguendo esattamente i sottoparagrafi e mettendo in evidenza:

- cosa succede tecnicamente,
    
- cosa controllano davvero,
    
- cosa può andare storto,
    
- cosa conviene fare per non rischiare.
    

---

# Handoff – cos’è e perché è cruciale

**Handoff** è la fase in cui:

- smetti di sviluppare “per te”,
    
- consegni il tuo design agli organizzatori,
    
- loro lo **testano automaticamente**,
    
- e decidono se il tuo HSM **entra o no in Attack Phase**.
    

👉 Se **non passi Handoff**, sei **fuori dalla competizione attiva** (niente punti offensivi o difensivi).

---

# 1) Automated Testing Service

👉 **Il giudice automatico**

Questa è l’infrastruttura MITRE che:

- clona il tuo repository,
    
- costruisce il firmware usando **Docker**,
    
- provisiona i secrets,
    
- flasha il binario su hardware pulito,
    
- esegue **test funzionali standardizzati**.
    

### Cosa testa (molto importante)

✔️ **Solo** i **Functional Requirements**  
❌ **NON** testa i **Security Requirements**

Questo significa:

- puoi passare Handoff con un design insicuro,
    
- ma verrai distrutto in Attack Phase.
    

---

## 1.1 Come funziona tecnicamente

Il servizio fa più o meno questo:

1. `git clone` del tuo repo
    
2. `docker build -t build-hsm .`
    
3. esecuzione `gen_secrets.py`
    
4. build del firmware dentro il container
    
5. flash su board non modificata
    
6. esecuzione di test automatici:
    
    - list
        
    - read
        
    - write
        
    - interrogate
        
    - receive
        
    - reboot / power-cycle
        
    - timing
        

👉 **Qualsiasi deviazione** dal comportamento atteso = test fallito.

---

## 1.2 Cosa NON puoi controllare

- L’hardware usato **non è il tuo**
    
- I Global Secrets **non sono quelli locali**
    
- L’ambiente **non è interattivo**
    
- Il timing è misurato con precisione
    

👉 Per questo “funziona sulla mia board” **non conta nulla**.

---

# 2) Submission Process

👉 **Come consegni il design**

La submission è **un’azione formale**, non “carico un zip e via”.

---

## 2.1 Quando puoi sottomettere

- La finestra di Handoff **si apre a una data precisa**.
    
- Puoi sottomettere **più volte** finché:
    
    - non passi i test,
        
    - o non chiude la finestra.
        

👉 Strategia tipica:  
**sottomettere presto**, anche con design semplice, per evitare sorprese.

---

## 2.2 Cosa deve contenere la submission

Il repository deve includere:

✔️ Codice sorgente completo  
✔️ Dockerfile funzionante  
✔️ Script di provisioning (`gen_secrets.py`)  
✔️ Documentazione richiesta (PDF)  
✔️ Nessun segreto hardcoded

❌ Niente file temporanei  
❌ Niente binari non necessari  
❌ Niente credenziali

---

## 2.3 Cosa succede dopo la submission

Dopo che sottometti:

- il sistema lancia automaticamente i test,
    
- **entro ~2 giorni lavorativi** ricevi:
    
    - **Accepted**
        
    - oppure **Rejected** con motivazione.
        

---

# 3) Accepted Designs

👉 **Cosa succede se passi**

Se il tuo design è **Accepted**:

### 3.1 Creazione dell’Handoff Package

Gli organizzatori creano un **handoff package**, che include:

- il tuo firmware compilato,
    
- la documentazione,
    
- gli artefatti per Attack Phase.
    

⚠️ **Ultimo checkpoint**:  
ti viene chiesto di **approvare il pacchetto**.

👉 È l’ultima occasione per dire:

> “Aspetta, ho lasciato dentro qualcosa che non doveva esserci”.

---

### 3.2 Congelamento del design

Dopo l’approvazione:

🚫 **Non puoi più modificare il design**  
🚫 Nessun bugfix  
🚫 Nessuna patch

Il design è **frozen**.

---

### 3.3 Ingresso in Attack Phase

- Il tuo HSM entra nello scoreboard.
    
- Inizi ad accumulare **punti difensivi passivi**.
    
- Gli altri team possono iniziare ad attaccarti.
    

👉 Più presto entri → più punti difensivi accumuli.

---

# 4) Rejected Designs

👉 **Cosa succede se NON passi**

Se il design è **Rejected**:

### 4.1 Ricevi un report

Il report indica:

- quale test è fallito,
    
- perché,
    
- spesso con log o messaggi d’errore.
    

⚠️ Non è un hint di sicurezza,  
è solo un **fallimento funzionale**.

---

### 4.2 Cosa puoi fare

Puoi:

- correggere il problema,
    
- **sottomettere di nuovo** (se la finestra è ancora aperta).
    

Non c’è penalità diretta per i reject,  
ma **perdi tempo** (e punti difensivi futuri).

---

### 4.3 Cause tipiche di reject (molto comuni)

- Timing fuori specifica
    
- Parsing input fragile
    
- Persistenza non corretta dopo reboot
    
- Dockerfile non deterministico
    
- Dipendenze mancanti
    
- Output leggermente diverso dallo standard
    

👉 Molti team forti vengono rejectati **almeno una volta**.

---

# 🧠 Come affrontare Handoff in modo intelligente

### Strategia consigliata

1. **Automated Testing locale** il prima possibile
    
2. Design minimale ma corretto
    
3. Submission anticipata
    
4. Solo dopo → hardening sicurezza
    

### Mentalità corretta

> Handoff non è “dimostrare che sei bravo”,  
> è “dimostrare che sei conforme”.

---

# 🔚 Riassunto secco

- **Automated Testing Service** → giudice implacabile
    
- **Submission Process** → formale e rigido
    
- **Accepted Design** → frozen, entra in Attack Phase
    
- **Rejected Design** → correggi e riprova
    

---

Se vuoi, come chiusura del percorso, posso:

- farti una **checklist finale pre-handoff**,
    
- oppure una **lista degli errori più comuni che fanno fallire Handoff**,
    
- oppure un **diagramma mentale “da kickoff a scoreboard”**.