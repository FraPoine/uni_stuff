## **1. Fondamenti di Multimedia / Passive Forensics**

- Cos’è la _digital passive forensics_ e quali problemi affronta (source identification, tampering detection, synthetic vs real.
- Catena di acquisizione dell’immagine e tracce introdotte da ogni fase: lente, CFA, sensore, A/D, DIP.
- Concetto di _fingerprint_ del dispositivo: analogia con balistica e armi da fuoco .
---

## **2. Source Identification**

### **2.1 Livelli di identificazione**

- **Livello 1 – Device level:** distinguere dispositivi dello stesso modello, tramite PRNU
- **Livello 2 – Brand/Model level:** discriminare marche e modelli tramite tracce nel pipeline di acquisizione (CFA, quantizzazione, pipeline).
- **Livello 3 – Class level:** distinguere foto reali, scannerizzate o generate al computer/AI.
### **2.2 PRNU (Photo Response Non-Uniformity)**

- Modello del segnale: componente additiva + moltiplicativa PRNU.
- Estrazione del riferimento PRNU attraverso denoising e media dei residui.
- Misure di autenticità: correlazione, PCE, correlation map.
- Robustezza a compressione JPEG, noise, resizing (tema dei laboratori).
- Uso del PRNU anche per _local tampering detection_ (assenza di correlazione su regioni manipolate).
### **2.3 Tracce di Model Identification**

- Tracce non specificate negli standard (es. tabelle di quantizzazione JPEG, CFA, H-tables).
- Tracce legate all’hardware: sensore CCD/CMOS, difetti fisici, pixel difettosi, rumore di foto-risposta.
- Demosaicing: correlazioni periodiche, kernel diversi per ogni produttore .

---

## **3. Discriminazione Synthetic vs Real**

### **3.1 Evoluzione dei media sintetici**

- Dai primi CG/CGI a GAN, StyleGAN, StyleGAN2, Diffusion Models
    

- .
    
- I media sintetici recenti sono iper-realistici e spesso indistinguibili anche per esperti
    

- .
    

### **3.2 Approcci di discriminazione (signal processing)**

- **Wavelet-based statistics** (momenti nei sottoband e predizioni cross-channel) per classificare immagini come reali o CG via SVM
    

- .
    
- **Analisi di simmetria facciale** (D-Face, S-Face) per individuare asimmetrie tipiche di volti reali vs simmetria innaturale dei CG
    
- .
    
- **Analisi di espressioni ripetitive**, dinamiche facciali, deformazioni geometriche e segnali fisiologici nei video
    

- .
    

### **3.3 Studi percettivi**

- Esperimenti su 640 partecipanti: impossibilità di distinguere volti sintetici (spec. StyleGAN2) da reali → performance vicino al caso (random guess)
    

- .
    
- Nuovi esperimenti su _trustworthiness_ e percezione di video deepfake (ancora senza pubblicazioni)
    

- .
    

### **3.4 Rischi, impatti e casi reali**

- Truffe tramite video deepfake iper-realistici (esempio: falso video di Elon Musk)
    

- .
    
- Necessità di strumenti di autenticazione (es. startup "Get Real") nelle videoconferenze
    
- .
    
- Rischi legali, pedopornografia sintetica, identificazione biometrica falsificata
    
- .
    
- Nuove normative: AI Act, obbligo di disclosure per media AI-generated
    

- .
    

---

## **4. Tampering Detection**

### **4.1 Tipologie di manipolazioni**

- Splicing, copy-move, global processing, filtering
    

- .
    

### **4.2 Tracce e metodi**

- **Pixel-level traces:** PRNU inconsistente, CFA mancante, filtraggi, median/morphological filtering
    

- .
    
- **Format-level traces:** doppia compressione JPEG, histogram merging, quantizzazione multipla (teoria e formule)
    
- .
    
- **Physical traces:** direzione della luce, ombre incoerenti, prospettiva
    
- .
    
- **Semantic traces:** coerenza metadati, luogo, data, contesto
    

- .
    

### **4.3 Localizzazione del tampering**

- Approcci sliding window + classifier
    

- .
    
- Mappe di heat/entropy/stima delle tracce inconsistenti
    

- .
    

---

## **5. Contesto attuale e progetti di ricerca**

- Ricerche su deepfake detection, media manipulation chain, social network forensics (TrueBees, Darpa Unchained, FF4ALL, Sargasso)
    

- .
    
- Problema crescente della disinformazione, democratizzazione dei modelli di generazione, impatti sociali e cognitivi
    
.