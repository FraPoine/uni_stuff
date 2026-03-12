# Why is important to distinguish synthetic and real media

# Media sintetici prima dell’era generativa: approccio signal processing

Prima dell’AI moderna, la detection si basava su analisi del segnale.
## Immagini – Wavelet statistics (Farid, 2005)
- Idea:
	- Le immagini sintetiche hanno strutture più regolare e meno naturali
	- analisi nei sottobando wavelet
- Caratteristiche estratte:
	- primi 4 movimenti statistici: media, varianza, skewness, kurtosis
	- su più livelli e canali colore
	- analisi dell'errore di predizione
- Classificazione
	- SVM binaria (reale vs sintetico)

### Simmetria facciale
- i volti sintetici sono sopratutto avatar e cgi e quindi sono più simmetrici
- i volti reali sono naturalmente asimmetrici
#### Metriche 
- D-Face: misuara asimmetrica
- S-Face: misura simmetrica
#### Pipeline
1. normalizzazione geometrica del volto
2. normalizzazione dell'illuminazione
3. confronto volto originale vs volto ribaltato

### Espressioni facciali ripetitive
- gli avatar esprimono le emozioni sempre nello stesso modo e gli umani hanno variazioni naturali
### metodo
- rilevamento automatico delle emozioni, ci sono 6 emozioni universali
- analisi della varianza dei landmark facciali
- espressioni sintetiche --> minore variabilità
### Dinamica delle espressioni
- analisi temporale 
	- onset --> apex --> Offset dell'emozione
	- parametri usati:
		- durata
		- velocità
		- accelerazione
		- ampiezza
### Segnali fisiologici
- idea chiave
	- gli umani hanno un battito cardiaco
	- gli avatar no
- metodo
	- Estrazione del PPG signal da micro-variazioni di colore/movimento della pelle 
	- analisi spettrale del segnale 
	- presenza di ritmo cardiaco --> forte indizio di realtà
- limiti
	- richiede una buona qulità video
	- sensibile a movimenti e compressione
### Era del generative AI 
- qualità delle immagini superiore alla percezione umana
- anche utenti esperti sbagliano
- i solcial rendono i contenuti virali in pochi secondi 
- è impossibile una verifica manuale

### AI vs AI: deep learning come difesa
- problema chiave
	- Modelli addestrati in laboratorio falliscono nel mondo reale 
	- compressione e condivisione social alterano le tracce forsensi 
- soluzione
	- addestramento ad-hoc su immagini condivise
	- incremental learning 

### Dataset real-world
- TrueFace
	- Immagini reali e fake
	- Condivise su social network
	- Open source
- TrueFake
	- 600k immagini
	- GAN + Diffusion
	- Versioni condivise su Facebook, Telegram, X
- VideoDiffusion
	- Video completamente sintetici
	- Diversi modelli di diffusione
	- Compressione H.264 a vari livelli
### Conclusion