## PRNU Recall

## Model identification

### Scenarios
- perfet knowledge
- partial knowledge 
- 0 knowledge

# Signal-level Traces: CFA-based
## Colour filter Array
- il sensore misura solo un colore per pixel. Gli altri due colori vengono stimati tramite demosaicing
- caratteristiche chiave
	- pattern periodico
	- più verde che rosso/blu
	- Interpolazione dipendente da marca e modello
- L’interpolazione introduce **correlazioni tra pixel vicini**, che sono sfruttabili a fini forensi.
## Tracce CFA e interpolazione
- the crux of this approach lies on estimating these coefficients and associating them with the digital camera-model used to capture the images

## Least squares and Weighted Least Squares
- usati per stimare modelli lineari in presenza di rumore
### Least squares
- Il **Least Squares** cerca il modello che **minimizza l’errore totale** tra:
	- i valori osservati;
	- i valori predetti dal modello.
- Limiti
	- esso assume implicitamente che tutti i punti siano ugualmente affidabili
	- ma ciò non è vero
### Weighted least squares
- in esso 
	- ogni punto ha un peso
	- i punti più affidabili valgono di più
### Intuizione forense 
- i pixel interpolati seguiono il modello
- i pixel originali non lo seguono
- quindi
	- diamo più peso ai pixel interpolati rispetto che quelli originali

## Expectation Maximization EM
- EM serve a stimare i parametri di un modello quando una parte delle informazioni è nascosta 
- Abbiamo:
	- i parametri dei coefficienti di interpolazione CFA
	- e nascosti i pixel interpolati e originali
- la strategia consiste nel
	- fingere di sapere le regole ed assegnare i punti
	- aggiornare le regole usando i punti assegnati
	- ripeti fino ad essere stabile 
- diviso in due step 
#### E step (Expectation)
- dato il modello attuale, quanto è probabile che questo dato appartenga a ciascun modello?
#### M step (Maximization)
- dato quanto ogni dato appartiene a ciascun modello, qual'è il miglior modello possibile

Quindi noi abbiamo due modelli in gioco
- quello in cui i pixel sono interpolati e seguono il kernel
- quello in cui ipixel sono originali e non seguono il modello

### E step
- ***OBIETTIVO***
	- Calcolare se P è interpolato
- come 
	- assumiamo noti i coefficienti
	- calcoliamo l'errore
		- ei = yi - aTXi
	- se l'errore è piccolo il pixel è coerente
	- se l'errore è grande, il pixel è originale
	- il peso al pixel viene dato in base a se è originale o coerente
### M step
- ***OBIETTIVO***
	- aggiornare il kernel di interpolazione a
- Come?
	- usando il wheighted least squares
		- pixel con il peso alto contano molto
		- pixel con il peso basso contano poco

### Perchè EM funziona?
EM funziona perché:
- all’inizio il modello è grezzo;
- assegna probabilità grossolane;
- migliora il modello;
- riassegna meglio le probabilità;
- raffina progressivamente entrambe.

### Output di EM
- dopo la convergenza otteniamo:
- Una **mappa di probabilità**
	- indica dove l'interpolazione è presente
	- evidenzia periodicità CFA
	- trova le zone incoerenti --> dove potrebbe esserci stato tampering
		- Se un’immagine è splicata:
			- regioni diverse → modelli diversi;
			- EM stima male un modello unico;
			- le probabilità diventano incoerenti;
			- la periodicità si rompe.
- I parametri del Kernel
	- fingerprint del modello di camera
	- utilizzabili per la classificazione
#### Collegamento con fourier
- La mappa di probabilità:
	- è periodica (Bayer pattern);
	- applicando FFT:
	    - compaiono picchi caratteristici;
	    - dipendono dal modello di camera.
#### Limiti dell’EM (da ricordare)
- convergenza a minimi locali;
- dipendenza dall’inizializzazione;
- sensibile a:
    - rumore forte;
    - resizing;
    - ri-interpolazione.

---
# Back on CFA color filter array
# CFA and tampering detection
### Cosa succede in un’immagine autentica?
In un’immagine **non manipolata**:
- i pixel interpolati:
    - seguono **lo stesso modello**
    - con **la stessa periodicità**
- la mappa delle correlazioni:
    - è **regolare**
    - ripetitiva
    - coerente su tutta l’immagine

--- 
# Signal level traces: deep Learning


---
# Format-level Traces: JPEG


---
# Open issues
- exploit jpeg 