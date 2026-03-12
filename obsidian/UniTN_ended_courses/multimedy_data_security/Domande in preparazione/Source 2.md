1. Che cos’è la **digital passive forensics** e quali sono i suoi obiettivi principali?
	La digital passive forensics è la passive forensics nel mondo digitale 

2. Che cosa si intende per **source identification** e perché è importante in ambito forense?
	già visto in source 1

3. Quali sono i **livelli della source identification** e in cosa differiscono tra loro?
	già visto in source 1

4. Perché un’immagine digitale può essere collegata al **dispositivo di acquisizione** anche senza watermark intenzionali?
	già visto in source 1

5. Che cos’è la **PRNU** e che tipo di informazione fornisce sul dispositivo sorgente?
	già visto in source 1

6. In che modo la **PRNU** può essere usata non solo per identificare il dispositivo, ma anche per rilevare **tampering**?
	già visto in source 1

7. Che ruolo ha il **Color Filter Array (CFA)** nel processo di acquisizione di un’immagine?
	il Color FIlter Array CFA, è parte della pipeline per l'aquisizione di un immagine, esso rappresenta un pattern periodico che permette alla fotocamera di ricpstruire l'immagine interpolando i colori

8. Perché le **tracce CFA** sono utili per l’identificazione del modello e per la rilevazione di manipolazioni?
	perchè se il pattern viene rotto l'immagine è stata probabilmente manipolata

9. In che modo la **compressione JPEG** può lasciare tracce utili all’analisi forense?
	non ricordo, mi aiuti a fare un ripasso
	La **compressione JPEG** lascia tracce perché
	- è **lossy** → perde informazione
	- usa parametri **non standardizzati**:
		- quantization tables
        - Huffman codes
    Ogni fotocamera / software sceglie **i propri parametri**
	Tracce utili:
	- **quantization tables** → firma di brand/modello 
	- **Huffman codes** → firma del software/dispositivo
	- **double JPEG compression**:
	    - istogrammi dei coefficienti DCT con “buchi” (zeri periodici)
	    - utile per scoprire splicing o editing
	- **incoerenze locali** → regioni con storie di compressione diverse

10. Perché, in ambito forense, si preferiscono spesso tecniche **basate su modelli e signal processing** rispetto a metodi di **deep learning**?
	non ricordo, mi aiuti a fare un ripasso
	
	In ambito forense **legale**:
	- i metodi devono essere:
	    - **interpretabili**
	    - **riproducibili**
	    - **spiegabili in tribunale**
	
	Il deep learning:
	- è una **black box**
	- non spiega _perché_ prende una decisione
	- dipende molto dal dataset
	- può fallire su dispositivi nuovi
	
	👉 Per questo si preferiscono:
	- **modelli fisici**
	- **signal processing**
	- **tracce legate alla pipeline di acquisizione**


mi riesci a fare più domande sul cfa e meno sugli argomenti condivisi con source 1

- Perché il sensore di una fotocamera **non acquisisce direttamente un’immagine RGB completa**?
	- il sensore di una fotocamera è in grado di catturare solo l'intensità luminosa e non il colore dell'immagine


- Che cos’è il **Color Filter Array (CFA)** e quale problema risolve?
	- il CFA color filter Array è un reticolo RGB che si pone davanti ad un sensore per riuscire a catturare i colori di un' immagine

    
- Perché il CFA ha una **struttura periodica** (es. Bayer)?
	- è necessario per l'interpolazione dei pixel, così che ogni pixel riesce ad estrarre i valori mancanti dai pixel vicini. 
	- inoltre è comodo nell'individuare tampering nell'ambito forense

    
- Che cos’è il **demosaicing** e perché è necessario?
	- per completare i valori mancanti nell'RGB dei pixel

    
- Qual è la differenza tra **pixel originali** e **pixel interpolati**?
	- qua si parla di piani, prendiamo ad esempio il piano verde, i pixel originali sono quelli che hanno catturato il proprio valore verde, quelli interpolati sono quelli che l'hanno ricavato dai vicini

    
- In che modo l’interpolazione CFA introduce **correlazioni tra pixel vicini**?
	- l'interpolazione, che cambia da modello a modello, implica che ogni pixel fa una media pesata dei valori dei pixel vicini per ottenere i propri valori mancanti
    
- Perché algoritmi di interpolazione diversi producono **tracce diverse**?
	- perchè un interpolazione diversa fa ottenere un valore diverso RGB ad ogni pixel interpolato
    
- Perché le tracce CFA possono essere usate per la **model identification** ma non per la device identification?
	- perchè il cfa segue un pattern periodico e un modello di interpolazione diverso per ogni modello, ma per dispositivi dello stesso modello è uguale 
    
- Qual è l’idea di base della **CFA-based tampering detection**?
	- che se il cfa non segue il modello di interpolazione o il pattern periodico allora l'immagine è stata modificata
    
- Perché lo **splicing** può rompere la coerenza delle tracce CFA?
	- perchè può interrompere la coerenza del pattern o del modello di interpolazione
    
- Che ruolo ha l’**Expectation–Maximization (EM)** nell’analisi CFA?
	- l'expectation prova ad indovinare il modello di interpolazione dando un peso ai pixel che sembrano originali e dando meno peso a quelli interpolati
	- e il maximization prova a verificarne l'esattezza
	- non mi ricordo benissimo, se mi ripassi un pochino questa cosa mi aiuti
    
- Cosa rappresenta la **mappa di probabilità CFA**?
	- la mappa di probabilità è una mappa che rappresenta per ogni pixel la probabilità che sia originale o interpolato
    
- Perché la periodicità CFA può essere evidenziata nel **dominio della frequenza**?
	- perchè il fatto che sia periodico dovrebbe dare dei picchi definiti e predicibili, 
    
- Che informazione forniscono i **picchi nella trasformata di Fourier**?
	- se un'immagine viene alterata genera dei picchi sospetti o non ne genera affatto
    
- Perché operazioni come **resize e rotazione** sono critiche per la CFA-based detection?
	- perchè potrebbero non rompere il pattern periodico e l'interpolazione, facendo in modo che il cfa non risulti compromesso

# Ripasso su CFA
## Perchè il CFA esiste
- il sensore non vede i colori, vede l'intensità luminosa
- ogni pixel misura quanta luce arriva, non il colore
- per ottenere un immagine colorata serve un meccanismo che separi le parti cromatiche
il **CFA Color Filter Array**
- è una matrice di fili colorati che viene posta davanti al sensore 
- ogni pixel del sensore viene coperto con un solo filtro, o rosso o verde o blu
- ogni pixel misura un solo colore
#### Bayer pattern 
- il CFA più comune è il bayer pattern
	- è una struttura periodica 
	- vede 2 verdi, 1 rosso e un blu in ogni blocco 2x2
	- più verde perchè è il colore a cui l'occhio umano è più sensibile 
	- il bayer pattern è periodico, fondamentale per la forensics
#### Problema introdotto dal CFA
- ogni pixel ha un solo colore
- mancano 2 componenti su 3
- l'immagine finale deve essere RGB completa 
- bisogna ricostruire i valori mancanti
### DEMOSAICING (interpolazione CFA)
- il processo di ricostruzione dei colori si chiama **demosaicing** o **CFA interpolation**
- idea base:
	- stimare i pixel mancanti usando quelli vicini
	- esempio
		- se manca il verde si usa la media dei verdi vicini
#### Interpolazione ≠ neutra
- l'interpolazione
	- non è unica 
	- non è standardizzata
- dipende dal produttore
	- ongni modello ha una interpolazione diversa
#### Cosa introduce il demosaicing nel segnale 
- **Correlazione tra pixel**
	- i pixel interpolati dipendono dai vicini
	- quindi non sono indipendenti
- **Correlazioni Periodiche**
	- perchè il CFA è periodico
	- quindi lo stessa schema si ripete su tutta l'immagine 
#### Pixel originali vs pixel interpolati
- quindi nell'immagine finale 
	- I pixel originali
		- sono valori acquisiti dal sensore
		- e non seguono il modello di interpolazione 
	- i pixel interpolati
		- sono valori stimati
		- seguono il modello CFA
- la forensics cerca di distinguere questi due gruppi e stimare il modello di interpolazione
#### CFA e Model Identification
- poichè il pattern è simile per tutti ma l'interpolazione cambia
- il CFA è ideale per identificare il modello ma non il singolo dispositivo
- è un fingerprint trutturale legato al software/hardware del modello
#### CFA e Tampering Detection
- Le correlazioni CFA sono coerenti ovunque 
- se c'è tampering 
	- una regione dell'immagine può essere interpolata diversa, avere un CFA disallineato, avere una doppia interpolazione
- la coerenza si rompe localmente
#### come si rivela la rottura
- ipotesi di partenza
	- i pixel interpolati 
		- seguono una relazione prevedibile 
		- dipendono dai pixel vicini
		- possono essere descritti da un modello linera
	- i pixel non coerenti
		- non seguono quel modello
		- e sono:
			- pixel originali
			- pixel alterati
			- pixel da un'altra immagine 
#### Problemo
- non sappiamo quali pixel seguono il modello, quali no, e banalmente quale sia il modello
- dobbiamo stimare tutto assieme
#### Strategia concettule
- provo a spiegare l'immagine assumento che esista un certo modello di interpolazione. poi guardo quali pixel si comportano bene e quali no
#### Algoritmi utilizzato
- **Expectation-Maximization EM** 
	- serve per stimare contemporaneamente pixel interpolati, quelli no, e il modello
- **Least Square LS**
	- serve per stimare i parametri di interpolazione lineare
	- si assume che il CFA sia approssimabile come modello lineare
	- LS minimizza l'errore tra valore del pixel e valore stimato dai vicini
- **Weighted Least Square WLS**
	- versione più importante del LS nel contesto CFA
	- serve per stimare il modello dando più peso ai pixel probabilmente interpolati e meno peso ai pixel sospetti
- **Fourier Transform (DFT/FFT)**
	- usata dopo la stima del CFA
	- serve ad evidenziare la periodicità delle tracce CFA e ad analizzare la mappa di probabilità nel dominio della frequenza
	- funziona perchè il CFA è periodico e la periodicità genera pochi picchi spettrali

#### Cosa fa l'algoritmo
- inizialmente ipotizza un modello di interpolazione anche super grossolano
- dopo di che verifica se i pixel sono coerenti con il modello ipottizato
	- sul singolo pixel se è coerente gli si attribuisce un errore piccolo se non lo è un errore grande
- invece di dire sì e no si assegna una probabilità che è alta se il pixel è coerente, è bassa se il pixel è sospetto
Nasce la mappa di probabilità
#### cos'è la mappa di probabilità
- è un immagine dove ogni pixel ha un valore che dice se il pixel segue il CFA stimato

#### Dove entra il tampering
- guardiamo la mappa spazialmente
	- in caso di un immagine autentica la mappa è omogenea, regolare e periodica
	- se l'immagine è manipolata nasce una macchia sospetta

### Perché si usa la fourier Transform 
- dato che la cfa è periodica e le correlazioni sono periodiche nel dominio della frequenza emergono picchi caratteristici
- se l'img è autentica allora escono picchi chiari
- se l'img non lo è escono picchi assenti o diversi

### Limiti del CFA
- è fragile al 
	-  resizing
	- rotazione
	- ri-campionamento
	- forte blur
	- nuova interpolazione globale
- tutte queste operazioni **creano nuova interpolazione** e “coprono” la traccia originale

Il Color Filter Array introduce correlazioni periodiche tra pixel a causa del processo di demosaicing. Tali correlazioni dipendono dall’algoritmo di interpolazione adottato dal modello di fotocamera e possono essere sfruttate per l’identificazione del modello e per la rilevazione di manipolazioni che ne rompono la coerenza.