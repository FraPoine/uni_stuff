### **Parte A – Contesto generale**

1. **Perché il problema “synthetic vs real media” può essere visto come un problema di source identification?**
	- perchè il problema sta nel verificare la source da cui viene il media, se è un media prodotto da un dispositivo analogico o da un dispositivo digitale
    
2. **Quali sono i principali rischi sociali e forensi legati alla diffusione dei deepfake?**
	- principalmente il rischio della diffusione delle fake news e delle truffe digitali 
    
3. **Perché i media sintetici non sono intrinsecamente “cattivi”, ma comunque pericolosi?**
	- è una domanda molto filosofica, riusciresti a suggerirmi tu una risposta corretta?
	- io direi che in se non sono negativi e hanno molte potenzialità ma appunto dipende da come li si usa (come le armi)
    
4. **In che modo i social network aggravano il problema della diffusione dei deepfake?**
	- i solcian network amentano la velocità di diffusione dei prodotti sintetici data la velocità con cui alcune notizie diventano virali 
    

---

### **Parte B – Evoluzione dei deepfake**

5. **Come si è evoluto il concetto di deepfake nel tempo, prima e dopo l’introduzione del deep learning?**
	- In origine il concetto di deepfake comprendeva tecniche manuali come photo doctoring, CGI e Photoshop.
	- con l'introduzione dei deep learning, prima con GAN e poi con autocoder e face swapping, i contenuti sintetici sono diventati più realistici
	- in questo momento la generazione di deepfake è democratizzata, altamente realistica e accessibile a chiunque, spostando il problmea sul distinguere contenuti indistinguibili dalla realtà.
    
6. **Perché la diffusione dei modelli di diffusione (diffusion models) rappresenta un punto di svolta?**
	- i diffusion models producono contenuti fotorealistici, coerenti e con pochi artefatti, superando molti limiti dei GAN.
	- e permettono una generazione controllabile e accessibile, rendono i deepfake più difficili da rilevare.
	- **iper-realismo + democratizzazione**
    
7. **Qual è il ruolo delle normative (es. EU AI Act) nel contrasto ai deepfake e quali sono i loro limiti?**
	- esse mirano a introdurre obblighi di **trasparenza**
	- i loro limiti sono
		- difficoltà di applicazione pratica, mancanza di standard tecnici universali e problemi di enforcment
    

---

### **Parte C – Approcci di signal processing (pre-AI)**

8. **Perché le statistiche nei sottobandi wavelet possono distinguere immagini reali da immagini sintetiche?**
	- non ricordo
    
9. **Quali sono i primi quattro momenti statistici usati nell’analisi wavelet e cosa rappresentano?**
	- non ricordo
	
10. **Perché l’errore di predizione nei coefficienti wavelet tende a essere più basso nelle immagini sintetiche?**
	- non ricordo
    

---

### **Parte D – Analisi del volto**

11. **Perché la simmetria facciale è un indizio utile per distinguere volti reali e sintetici?**
	- dato che percepiamo più belli i volti simmetrici i volti sintetici tendono ad essere più simmetrici rispetto a quelli reali
    
12. **Che differenza c’è tra le metriche D-Face e S-Face e cosa misurano?**
	- non ricordo
    
13. **Perché è necessaria la normalizzazione geometrica e di illuminazione prima dell’analisi del volto?**
	- non ricordo
    

---

### **Parte E – Analisi dinamica e fisiologica**

14. **Perché le espressioni facciali degli avatar tendono a essere più ripetitive rispetto a quelle umane?**
	- perchè seguono le stesse 6 emozioni cercando di imitarle sempre allo stesso modo
    
15. **In cosa consiste l’analisi della dinamica delle emozioni (onset–apex–offset)?**
	- non ricordo
    
16. **Perché il battito cardiaco è considerato un forte indizio di “realness” in un video?**
	- semplicemente perchè gli avatar non hanno battito cardiaco
    
17. **Quali sono i principali limiti dell’uso dei segnali fisiologici per la detection dei deepfake?**
	- non ricordo
    

---

### **Parte F – Era AI vs AI**

18. **Perché i modelli di deep learning addestrati in laboratorio falliscono spesso in scenari reali?**
	- perchè sono addestrati in ambienti protetti con pochi campioni
    
19. **Perché è necessario addestrare i detector anche su immagini condivise sui social network?**
	- per dargli un idea di cosa spettarsi fuori dal laboratorio
    
20. **Quali sono le principali sfide future nella lotta tra generazione e rilevazione dei media sintetici?**
	- Attualmente la sfida AI vs AI continua 
	- altre che non ricordo


---
# Approcci signal processing Pre AI
## Analisi wavelet
- essa scompone le immagini in
	- bassa frequenza (struttura)
	- alta frequenza (bordi, dettagli)
- ogni livello produce sottobande su più scale di colori
	- orizzontale 
	- verticale
	- diagonale 
## Statistiche nei sottobandi 
- per ogni sottobanda si estraggono i primi 4 momenti statici:
	1. media
	2. varianza
	3. skewness
	4. kurtosis
- le immagini sintetiche tendono ad avere distribuzioni:
	- più regolari
	- meno complesse
	- con minore varianza 
## Errore di Predizione
- idea
	- nelle immagini sintetiche molte regioni sono piatte e prevedibili
	- nelle immagini reali le texture sono irregolari 
- metodo
	- si prende un coefficiente wavelet usando i vicini e si analizza la statistica dell'errore di predizione 
- risultato
	- errore più basso, immagine sintetica
	- errore più alto, immagine reale

# Analisi del volto 
### Perchè il volto?
- è simmetricamente centrale
- è il target principale dei deepfake
- è fortemente riconoscibile dagli umani
### Simmetria Facciale 
- i volti sintetici sono spesso molto simmetrici
- i volti reali sono naturalmente asimmetrici 
- motivo:
	- la generazione è basata su modelli ideali
	- i dataset di addestramento sono sbilanciati verso volti esteticamente gradevoli
### Pipeline di analisi 
- Prima di misurare la simmetria serve 
1. **normalizzazione geometrica** 
	- allineamento occhi, naso, bocca
2. **normalizzazione dell'illuminazione** 
	- rimozione ombre e riflessi
senza normalizzazione --> falsi positivi
### Metriche principali 
- **D-Face (Density Difference)**
	- misura quanto il volto differisce dalla sua versione specchiata
	- più alto, più asimmetria, più probabile volto reale
- **S-Face (Edge Orientation Similarity)**
	- misura la similarità dell'orientamento dei bordi
	- più alto, più simmetria, più probabilità volto sintetico

# Analisi dinamica e fisiologica
### Perchè il tempo è importante
- il movimento è molto più difficile da simulare correttamente
### Espressioni facciali ripetute
- gli avatar esprimono le emozioni seguendo schemi fissi
- metodo
	- riconoscimento automatico delle emozioni Ekman
	- analisi della varianza dei landmark facciali
	- bassa variabilità --> probabile sintetico
### Dinamica delle emozioni
- ogni emozione segue uno schema temporale 
	- Onset --> inizio
	- Apex --> massimo
	- Offset --> riotorno alla neutralità
- vengono analizzati 
	- durata
	- velocità
	- accelerazione
	- ampiezza del movimento
- negli avatar la dinamica è più regolare e prevedibile 
### Segnali fisiologici (heart rate)
- gli umani hanno un battito cardiaco, gli avatar no
- metodo
	- estrazione del ppg signal
	- micro-variazioni di colore/movimento della pelle
	- analisi spettrale --> frequenza cardiaca
- se il battito è presente --> allora alta probabilità di realness
### Limiti dei segnali fisiologici
- bassa qualità dei video
- compressione
- movimento del soggetto
- pelle non visibile 
- **metodo potente ma poco robusto in the wild** 

# Era AI vs AI
### Cambio di paradigma
- con GAN e diffusion models:
	- gli artefatti classici spariscono
	- il signal processing da solo non basta
	- AI vs AI
### Detector deep learning 
- nel 2018
	- CNN (ResNat, Xception, EfficientNet)
	- Vision Transformer (CLIP)
- vantaggio
	- apprendono automaticamente feuture complesse
### Problema con la generalizzazione 
- i modelli
	- funzionano bene in laboratorio
	- falliscono su immagini
		- compresse
		- ridimensionate
		- condivise sui social
	- perchè le tracce forensi vengono alterate
### Social network forensics
- Un detector deve funzionare nel mondo reale e non solo in laboratorio
- soluzione
	- addestrarlo sui dati post social 
	- dataset real-world
	- incremental learning 
### **Sfide future**
- corsa continua **AI vs AI**
- nuovi modelli generativi
- attribution della sorgente
- estensione a video, audio e multimodale
- **ricostruzione della fiducia nei media**

---
- cos'è il GAN
