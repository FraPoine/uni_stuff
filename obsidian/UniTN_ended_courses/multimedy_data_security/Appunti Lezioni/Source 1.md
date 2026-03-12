# Photo Response Non-Uniformity Noise PRNU
not uniform response to the same light impulse
- its really tiny
- it start form a the sensors imperfection
	- sensor noise 

## Componenti del rumore: FPN vs PRNU
La lezione distingue due componenti principali (a livello intuitivo):
1. **Fixed Pattern Noise / Dark Current**  
    È una componente più “fissa”, ma spesso viene **compensata direttamente nel dispositivo**, quindi lascia meno tracce utili nel file finale.
2. **Photo Response Non-Uniformity (PRNU)**  
    È la parte più utile in forense: riguarda la **non uniformità nella risposta alla luce** della matrice del sensore.  
    È questa la “firma” che interessa: **piccolissima, invisibile a occhio**, ma presente in tutte le immagini scattate da quel sensore

## Come si stima il PRNU (costruzione del “reference fingerprint”)
#### 1) Raccolta immagini del dispositivo
- servono 20-50 immagini dallo stesso dispositivo
#### 2) Denoising e noise residual
- per ogni immagine si applica un filtro di denoising ottenendone la versione pulita dell'immagine
	- il risultato è chiamato ***noise residual***
- Nella lezione viene citato il **Wiener filter** come scelta classica proposta nel lavoro originale
#### 1) Media su più immagini per ottenere la fingerprint
- Un singolo residuo **W** è troppo “rumoroso” e dipende ancora dal contenuto. Quindi si combinano molti residui per ottenere una **stima robusta** della fingerprint PRNU del dispositivo
- In lezione viene descritta la classica forma di stima che “media” l’informazione su più immagini, pesando in funzione del contenuto dell’immagine, così da convergere verso un pattern stabile del sensore

## Come si usa il PRNU per identificare il dispositivo
Una volta che hai una **reference PRNU** per ciascun dispositivo (o per un insieme di dispositivi noti), il test su un’immagine ignota funziona così:
1. prendi l’immagine “sospetta”
2. fai denoising e calcoli il residual **W**
3. confronti **W** con ogni reference PRNU tramite **correlazione**
L’idea spiegata a lezione è molto intuitiva: se l’immagine proviene da uno dei dispositivi noti, la correlazione con la sua fingerprint sarà **significativamente più alta** rispetto alle altre → appare un **picco**

the reference prnu is a matrix
the reference matrix is needed for estimate if an image came from a specific device


## Applicazioni del PRNU
La lezione cita varie applicazioni (oltre al “device identification” puro):
- **Device identification** (quale dispositivo ha scattato)
- **Device linking** (due immagini provengono dallo stesso device?)
- **Tampering / forgery detection** (assenza o incoerenza della fingerprint in regioni locali)
- **Recovery della processing history** (capire se/come processing ha alterato la fingerprint)
- **Blind source clustering** (raggruppare immagini per device senza sapere a priori quanti device ci sono)

## Robustezza e limiti pratici

### Robustezza
Essendo un segnale debole, il PRNU non è “invincibile”, però la lezione sottolinea che spesso **sopravvive a processing comuni**, e questo è uno dei motivi per cui è molto usato anche in scenari reali (es. compressione JPEG non troppo aggressiva, resizing, post-processing tipico).

### Limiti / difficoltà
La lezione evidenzia soprattutto un problema pratico: **scalabilità**.
- Per identificare un device con PRNU devi avere (in genere) la **fingerprint di riferimento** → significa raccogliere immagini per ogni device (o usare database già esistenti).
- In contesti “stretti” (pochi sospetti / pochi dispositivi) è fattibile; in contesti enormi diventa costoso.
---
# Level 2
## model identification
- a lot of application
	- detect the model among different devices from the same family

there are a lot of thing to see but we dont have time 
there is a really dense pipeline 
- there are a lot of phase that are at the signal level 
- there is also a phase that permit us to analyze the metadata

## Scenarios - Perfect , Limited and 0 Knowledge

### Scenario **Perfect Knowledge**
Si parla di **perfect knowledge** quando:
- l’insieme dei **modelli di dispositivi possibili è noto**
- per **ogni modello** si dispone di **un numero sufficiente di immagini di training**
- le immagini di training sono **correttamente etichettate** (si sa da quale modello provengono)
In questo scenario:
- il problema di source identification è un **classico problema di classificazione multi-classe**
- è possibile addestrare un classificatore (tradizionale o deep learning)
- si può calcolare una **confusion matrix completa** per valutare le prestazioni
È lo scenario più “comodo” dal punto di vista teorico, ma **poco realistico** in applicazioni forensi reali, perché raramente si conoscono _tutti_ i modelli possibili in anticipo.
### Limited Knowledge scenario
Nel **limited knowledge scenario** si ha **conoscenza parziale**:
- si conosce **solo il modello/dispositivo target**
- non si conosce **quali né quanti altri modelli** possano comparire
- si dispone di molte immagini del **target**, mentre il resto è “unknown”
Il problema diventa:
_questa immagine è compatibile con il modello target oppure no?_
Si utilizzano tipicamente **one-class classifiers** o test di compatibilità (es. correlazione PRNU).
➡️ È uno scenario **più realistico** di quello perfect knowledge, spesso usato in ambito forense.

### Zero Knowledge scenario
Nel **zero knowledge scenario** non si assume **alcuna informazione a priori**:
- non si conosce il **numero di dispositivi**
- non si conoscono **i modelli**
- si ha solo un **insieme di immagini non etichettate**
L’obiettivo non è “dare un nome al device”, ma:
- **raggruppare le immagini** che provengono dallo **stesso dispositivo o modello**
Questo è un problema di **blind source clustering**, spesso basato su:
- similarità PRNU
- fingerprint di sensore
- metodi non supervisionati
➡️ È lo scenario **più difficile**, ma anche **il più realistico** in indagini reali.

---
# Source identification - model

## Format level
### JPEG (source identification)

Nel **format-level JPEG** l’analisi non si basa sul contenuto dell’immagine o sul segnale (come PRNU o CFA), ma **sulla struttura del file JPEG** e sui **parametri di compressione** scelti dal dispositivo o dal software che ha generato l’immagine.

L’idea chiave è che **lo standard JPEG non impone scelte uniche**: ogni produttore (o software) può implementarlo in modo leggermente diverso, lasciando **tracce caratteristiche** nel file.
### Quali tracce JPEG si analizzano
A livello di formato, si analizzano soprattutto:
- **Tabelle di quantizzazione**
    - matrici 8×8 usate nella compressione DCT
    - diverse per luminanza e crominanza
    - spesso **specifiche di brand o modello**
- **Codici di Huffman**
    - mappature usate per l’encoding entropico
    - il JPEG standard non impone codici fissi
- **Dimensioni dell’immagine**
    - risoluzione tipica del sensore
- **Struttura dell’header JPEG**
    - marker presenti
    - ordine e numero dei segmenti
- **Metadata EXIF**
    - campi standard
    - campi proprietari
    - errori di parsing (considerati feature)
### Perché funziona
Ogni fotocamera o software:
- sceglie **specifiche tabelle di quantizzazione**
- usa **propri codici di Huffman**
- organizza **header e metadata** in modo caratteristico
Questa combinazione crea una **firma di formato** che può essere:
- confrontata con un database di firme note
- usata per **brand/model identification**
- usata per **rilevare editing** (es. Photoshop)

### A cosa serve il format-level JPEG
Nel contesto forense, viene usato per:
- **Identificazione del modello o brand**
- **Verifica di coerenza**
    - EXIF dice “Nikon”, ma la firma JPEG non è Nikon → sospetto
- **Rilevamento di software di editing**
- **Pre-filtraggio**
    - ridurre il numero di device candidati prima di analisi più costose (es. PRNU)
### Limiti principali
- **Non identifica il singolo dispositivo** (non è device-level)
- Le firme possono coincidere tra modelli diversi
- Editing o ri-salvataggi possono alterare la firma
## JPEG Header 
Il **JPEG Header** è la parte iniziale del file JPEG che **descrive come l’immagine è stata compressa e memorizzata**, prima ancora dei dati di immagine veri e propri.
Non contiene il contenuto visivo, ma **tutte le informazioni necessarie per decodificare correttamente l’immagine**, oltre a metadata e parametri scelti dal dispositivo o dal software.
In ambito forense, il JPEG Header è importante perché **molte di queste scelte non sono standardizzate**, quindi costituiscono una **firma caratteristica** del dispositivo o del software di acquisizione.

#### Struttura generale del JPEG Header
Il file JPEG è composto da **marker segments**, ognuno identificato da un codice (marker).  
Il **numero, il tipo e l’ordine** di questi marker può variare.
Nel JPEG Header troviamo principalmente:
1. Marker di **inizio file**
2. Segmenti di **definizione della compressione**
3. Segmenti di **metadata**
4. (eventualmente) **thumbnail**
#### Tabelle di quantizzazione
Uno degli elementi più importanti del JPEG Header sono le **tabelle di quantizzazione**:
- Matrici **8×8** associate alle frequenze DCT
- Separate per **luminanza (Y)** e **crominanza (Cb, Cr)**
- Controllano il compromesso **qualità ↔ compressione**

Punti chiave:
- Lo standard JPEG **non impone valori fissi**
- Ogni produttore può usare **tabelle proprietarie**
- Modelli diversi usano tabelle diverse

➡️ In forense, l’insieme dei valori di quantizzazione è una **feature discriminante** per brand e modello.

#### Codici di Huffman
Il JPEG Header contiene anche le **tabelle di Huffman**, usate per la codifica entropica dei coefficienti DCT:
- Tabelle separate per:
    - coefficiente **DC**
    - coefficienti **AC**
- Per ciascun canale (Y, Cb, Cr)
- Rappresentate come distribuzione dei codici di lunghezza 1…15
Punti chiave:
- Anche i codici di Huffman **non sono obbligatoriamente standard**
- Fotocamere e software scelgono configurazioni diverse
- I codici di Huffman fanno parte della **firma JPEG**
#### Dimensioni dell’immagine
Nel JPEG Header sono presenti anche:
- larghezza
- altezza
- numero di canali
Queste informazioni:
- riflettono la **risoluzione del sensore**
- aiutano a distinguere modelli con sensori diversi
## Thumbnail (immagine incorporata)
Molti JPEG contengono una **thumbnail** (miniatura) incorporata:
- compressa separatamente
- con **proprie tabelle di quantizzazione e Huffman**
- non sempre presente (dipende dal dispositivo)

# CONTINUARE PIU' AVANTI

---

## Signal Level