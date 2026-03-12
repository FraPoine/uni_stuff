### 🔹 Parte 1 – Concetti fondamentali

1. Che cosa si intende oggi per **deepfake** e come è evoluta questa definizione nel tempo?
	- una volta era legato a delle tecniche manuali, come CGI e photoshop
	- adesso è accessibile a chiunque e io problema si è spostato nel distinguere i media generati da quelli reali
	- grande sfiducia nei media
    
2. Perché i deepfake **non sono un fenomeno esclusivamente legato all’AI moderna**?
	- esistono da molto tempo, l'IA moderli li ha resi solo molto più democratizzati 
    
3. Quali sono i principali **rischi sociali e di sicurezza** associati ai media sintetici?
	- la difficoltà nel distinguere un prodotto reale da uno costruito
    

---

### 🔹 Parte 2 – Approcci pre–Generative AI

4. Quali tecniche di **signal processing** venivano utilizzate per distinguere volti reali e sintetici prima dell’era GAN?
	- prima dell'era GAN c'erano molte techinche per distinguere i volti reali da quelli sintetici
		- analisi wavelet, che scompone le immagini in alta e bassa frequenza
			- ogni livello produce sottobande su più scale di colori e per ogni sottobanda si estraggono i primi 4 momenti statici
				- media, varianza, skewness e kurtosis
			- le immagini sintetiche tendono ad avere distribuzioni più regolari, con minore varianza 
		- errore di predizione
			- nelle immagini sintetiche molte regioni sono piatte e prevedibili, nelle immagini reali le texture sono irregolari 
			- si prende un coefficiente wavelet usando i vicini e si analizza la statistica dell'errore di predizione
				- errore basso --> immagine sintetica
				- errore alto --> immagine reale 
		- Analisi del volto, 
			- ci sono varie tecniche di analisi del volto per capire se una immagine è sintetica, il volto viene comodo da analizzare dato che è simmetricamente centrale, è il target principale dei deepfake è fortemente riconoscibile dagli umani
			- si usa:
				- la simmetria facciale facendo una normalizzazione geometrica  e la normalizzazione dell'illuminazione 
				- e su usano la D-Face e la S-Face
    
5. In che modo la **simmetria facciale** veniva sfruttata nella detection?
	- i volti sintetici tendono ad essere più simmetrici dato che partono da modelli ideali e lo studio della simmetria aiuta a comprendere l'origine del volto.
		- la simmetria facciale si valuta tramite una normalizzazione geometrica, ovvero l'allineamento di naso, occhi, bocca, e la normalizzazione dell'illuminazione, ombre e riflessi
		- inoltre si usano la D-Face, Density difference, che valuta quanto il volto differisce dalla sua versione specchiata, e la S-Face, edge orientation similarity, che misura la similarità dell'orientamento dei bordi
    
6. Quali **indizi temporali** venivano analizzati nei video sintetici?
	- nei video sintetici vengono valutati:
		- le espressioni facciali ripetute
		- la dinamica delle emozioni durante l'onset, l'apex e l'Offset
		- i segnali fisiologici (heart rate)
	
7. Perché questi approcci hanno perso efficacia con l’aumento del realismo dei media?
	- perchè con lo sviluppo di diffusion model, GAN e di deep learning model, la realizazzione di media sintetici è sempre più vicino a quella reale e il modo migliore per contrastarla è combatterla con le stesse armi
    

---

### 🔹 Parte 3 – Generative AI e percezione umana

8. Che cosa dimostrano gli esperimenti percettivi “**more real than real**”?
	- che gli osservatori non addestrati non sono in grado di distinguere i media sintetici da quelli reali
    
9. Perché anche **osservatori esperti** faticano a distinguere immagini reali e sintetiche?
	- perchè i modelli di generazione delle immagini sintetici sono difficili da distinguere dall'occhio umano

10. Qual è l’impatto della **riduzione degli artefatti visivi** sulla capacità di detection umana?
	- l'incapacità di distinguere un deepfake e quindi al perdita di fiducia nei media 
    

---

### 🔹 Parte 4 – AI vs AI e deep learning

11. Perché si parla di una battaglia **AI vs AI** nella multimedia forensics?
    
12. Perché modelli di deep learning **general-purpose** (es. ResNet) risultano efficaci nella detection forense?
    
13. Che cos’è **Noiseprint** e quale relazione ha con il **PRNU**?
    
14. Perché nella forensics è spesso più importante analizzare il **rumore** piuttosto che il contenuto semantico?



---

### 🔹 Parte 5 – Generalizzazione e scenari reali

15. Che differenza c’è tra **pre-social** e **post-social data**?
    
16. Perché i detector addestrati in laboratorio falliscono quando i media vengono condivisi sui social network?
    
17. Qual è il contributo dei dataset realistici (es. TrueFace) alla detection dei deepfake?
    

---

### 🔹 Parte 6 – Diffusion models e futuro

18. Perché i **diffusion models** rappresentano una nuova e più complessa sfida per la multimedia forensics?

****
****

# AI vs AI e Deep Learning

### Perchè si parla di AI vs AI
- generative AI, il problema cambia natura 
- AI che genera media vs AI che li deve rilevare

#### Perché il deep learning è diventato centrale
- esso permette un apprendimento automatico delle tracce forensi, l'utilizzo di reti general-purpose, maggiore robustezza rispetto alle tecniche manuali
- **Le reti nate per la computer vision funzionano meglio delle soluzioni forensi ad hoc**, se opportunamente adattate.

### Reti usate nella detection
- **2018–2020**
    - EfficientNet
    - XceptionNet
    - DenseNet
- **2020–2023**
    - **ResNet**
    - **Noiseprint**
- **2024–oggi**
    - Transformer
    - Vision Transformer (ViT)
    - CLIP-based methods

### Perché ResNet funziona bene in forensics
- essa non è enorme, usa connesioni residue e riesce a catturare pattern deboli ma persistenti
- la forensics **non guarda il contenuto semantico** (chi c’è nella foto), ma **le tracce lasciate dal processo di generazione/acquisizione**.

### Noiseprint e legame con PRNU
- Il PRNU è un fingerprint del sensore ed è basato su pattern di rumore fisso 
- Il Noiseprint
	- è una versione deep learning del PRNU
	- non identifica il singolo dispositivo ma è la firma del processo
	- è molto efficace per rilevare manipolazioni locali e per la distinzione del reale vs sintetico
	- Noiseprint sfrutta il deep learning per apprendere automaticamente le tracce di acquisizione e generazione presenti nel rumore dell’immagine.

# Generalizzazione e Social Network
### Il vero problema: la generalizzazione
- un detector funziona bene sui dati di training ma funziona male su dati diversi
- tipi di mismatch
	- nuovo generatore
	- nuova risoluzione
	- compressione
	- condivisione su social
### Pre-social vs Post-social data
- Pre-social data
	- immagini originali
	- non complesse
	- condizioni di laboratorio
- Post social 
	- immagini condivise tramite social
	- subiscono compressione, resizing, filtraggio, predita di tracce forensi 
- detector addestrati solo su pre-social **crollano** sui post-social.
### Perché i social “rompono” i detector
- i social network alterano il rumore, distruggono pattern deboli e cambiano statistiche locali
- il risultato è che detector che in lab performano bene nel mondo reale peggiorano molto 
### Dataset realistici: TrueFace
- è importante perchè include immagini reali e sintetiche, include versioni condivise sui social e rappresenta uno scenario in the wild
- per funzionare nel mondo reale, i detector devono essere addestrati su dati realistici.
### Fine-tuning e adattamento
- non basta addestrare una volta sola, serve fare fine tuning su dati post social 
- training con pre + post social, domain adaptation, data argumentation mirata

# Diffusion Models e futuro
- magari la guardo meglio domani o stasse