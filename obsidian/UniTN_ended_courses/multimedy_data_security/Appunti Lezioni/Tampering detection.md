# Multimedia Forensics: obiettivi generali


# Tampering Detection: definizione e compiti
- il tampering è qualsiasi modifiuca intenzionale di un contenuto multimediale 
- problemi principali
	- **Forgery detection** sabilire se è stata contraffatta
	- **Forgery Localizzation** stabilire dove è stata manipolata
### Pipeline tipica
- Estrazione delle feature forsensi
- classificazione, con o senza training 
- eventuale uso di sliding window per la localizzazione 
- aggregazione e decisione finale
- due metodi principali
	- supervisionati --> con training set di immagini genuine e forgite
	- blind --> senza training esplicito

# Classificazione delle tracce forensi
- le tracce usate per il tampering detection si dividomno in più livelli
### Pixel-level traces 
- Basate su statistiche locali dei pixel e sulle impronte lasciate dalla pipeline di acquisizione
	- CFA
	- PRNU
	- Tracce di filtraggi, tipo il filtraggio mediano
### Tracce fisiche e geometriche 
- basate sulla fisica della scena
	- direzione della luce
	- ombre
	- geometrica prospettica
### Tracce basate sul formato 
- compressione JPEG
- Doppia o multipla compressione 
### Livello semantico
- Coerenza di data, luogo e contenuto 

# Pixel-level traces: CFA
### Color Filter Array (CFA)
- Il CFA è una matrice di filtri colorati posta sopra il sensore
	- ogni pixel acquisisce una sola componente cromatica (R, G o B)
	- Lo schema più comune è il **Bayer pattern**
### Demosaicing 
- Poiché ogni pixel misura un solo colore, i valori mancanti vengono ricostruiti tramite **interpolazione (demosaicing)**. Questa operazione introduce:
	- **Correlazioni tra pixel vicini**
	- **Periodicità spaziali** legate alla struttura del CFA
### CFA come traccia forense
- Ogni produttore usa **algoritmi di interpolazione diversi**
- Le correlazioni periodiche possono essere stimate (es. nel dominio di Fourier)
- In una regione manomessa (splicing):
    - le tracce CFA possono essere assenti o incoerenti

# Tracce di filtraggio
### Filtro mediano
- il median filtering è spesso usato per timuvere rumore e mascherare operazioni di editing 
- gli effetti forensi che ha sono la modifica delle statistiche locali, e l'introduzione di pattern rilevabili nei segnali
### Filtri morfologici
- operazioni come erosione e dilatazione lasciano
	- strutture anomale 
	- regioni innaturalmente uniformi
- tracce utili per la localizzazione del tampering
# Tracce di illuminazione e ombre
### Direzione della luce
- in una scena reale
	- tutti gli oggetti sono illuminati dalla stessa sorgente luminosa 
- nel composing
	- è difficile rendere coerente la direzione della luce 
	- inconsistente --> indizio di splicing 
### Analisi delle ombre
- principio fisico,
	- un punto dell'ombra, il punto corrispondente sull'oggetto e la sorgente luminosa sono allineati
- nel piano immagine
	- le rette che contengono oggetti e ombre devono intersecarsi nello stesso punto
- ombre incoerenti
	- rette che non convergono nello stesso punto 
	- frte indicazione di manipolaizone
- importante, L’essere umano è **poco affidabile** nel giudicare la coerenza delle ombre --> servono strumenti automatici

# Tecniche geometriche
### Proiezione prospettica
- La proiezione da mondo 3D a immagine 2D è descritta da
	- parametri intrinsechi (focale, punto principale)
	- parametri estrinsechi (Rotazione e traslazione)
### Omografia 
- nel caso di punti planari
	- la relazione è descritta da un omografia H
### Calibrazione
- Assumendo 
	- Pixel quadrati 
	- Skew nullo
- è possibile stimare
	- punto principale e la lunghezza focale
### Photo composing 
- nel fotomontaggio
	- parti dell'immagine possono subire traslazioni o scalature, questo altera i parametri intrinseci stimati 

# Manipolazione del testo
- Il testo su superfici planari segue regole prospettiche precise.
- Problema
	- inserire o modificare il testo è facile visivamente ma è difficile rispettare esattamente la proiezione prospettica
- metodo
	- stimare l'omografia dal testo
	- rettificare l'immagine 
	- calcolare l'errore di ricostruzione
- risultato
	- Testo autentico --> errore basso
	- Testo manipolato --> errore alto 

# Tracce di compressione JPEG
### Compressione singola 
- le immagini naturali non compresse hanno istogrammi densi 
- La compressione JPEG introduce quantizzazione dei coefficienti DCT
- è possibile 
	- formulare un test statistico 
	- distinguere immagini mai compresse da immagini già compresse
### Doppia Compressione 
1. Prima quantizzazione con passo b
2. De-quantizzazione
3. Seconda quantizzazione con passo a
-  Effetti:
	- Istogrammi con **zeri periodici**
	- Periodicità legata ai passi di quantizzazione
- Caso più semplice:
	- Prima compressione più forte
	- Seconda compressione più debole

# Considerazioni finali
- Non esiste una soluzione universale al tampering detection
- Ogni tecnica è efficace per specifici tipi di manipolazione
- La combinazione di più strumenti è fondamentale
- Approcci recenti (es. deep learning, Noiseprint) sono promettenti