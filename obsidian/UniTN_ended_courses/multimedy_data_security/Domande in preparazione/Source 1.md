### 1.
Che cosa si intende per **passive multimedia forensics** e quale problema principale affronta?
non ricordo molto bene
l'identificazione dei device che producono un media per la polizia?

### 2.
Che cos’è la **source identification** e a quali livelli può essere affrontata?
Con source identification si intende l'identicazione del device che ha prodoto un media taghet
essa è divisa in 3 livelli con diverse tecniche di identificazione
il primo livello è il livello di tipo del device, ovvero la famiglia di device che ha prodotto il media, se un cellulare, una fotocamera, un computer, un immagine in cg
il secondo livello è quello dell'identificazione della marca e del modello, la marca di cellulare, il modello di fotocamera
e il terzo livello è quello dell'identificazione del singolo dispositivo che ha prodotto il media
### 3.
Perché le immagini digitali possono essere collegate al **dispositivo di acquisizione** anche senza watermark intenzionali?
perchè i dispositivi hanno un fingerprint non intenzionale che dipende da errori dei componenti che catturano il media, e lasciano inevitabilmente un rumore sull'immagine
**dovute alle imperfezioni fisiche dei componenti hardware**

### 4.
Che cos’è il **PRNU** e da cosa nasce fisicamente?
Il PRNU Photo response non-uniformity, è un rumore costante che viene lasciato dai componenti di un device su un media prodotto, è sempre costante perchè dipende da componenti fisci 
riguarda la non uniformità della risposta alla luce da parte della matrice del sensore ed è una firma del singolo dispositivo sui media prodotti da lui

**rumore moltiplicativo**
### 5.
Perché il PRNU è considerato una **firma del singolo dispositivo** e non solo del modello?
perchè è proprio del singolo dispositivo, tramite esso si può ricondurre una immagine al singolo dispositivo e non al modello, che ha altre cose per riconoscerlo, come il CFA

### 6.
Come viene stimato il PRNU a partire da un insieme di immagini?
serve un insieme di immagini, preferibilmente tra le 20 e le 50, molto illuminate, il consiglio è di scattare foto al cielo sereno. dopo di che si applica un filtro di denoising, ne viene citato uno specifico ma non ricordo quale, ottenendo così l'immagine senza rumore. dopo di che si sottrae l'immagine senza rumore a quella con, ottenendo il residuo, e con la serie di residui si riesce a ricostruire il PRNU, (se mi riesci a rispiegare un attimo melgio l'ultimo passaggio mi fai un piacere)

Ogni **residuo singolo** contiene:
- PRNU
- rumore casuale
- residui di contenuto
**Mediando molti residui**, il rumore casuale e il contenuto **si annullano**, mentre il PRNU (che è sempre uguale) **si rafforza**.
il residuo viene **pesato usando l’immagine originale**, perché il PRNU è **moltiplicativo**.

### 7.
In che modo il PRNU può essere usato sia per **identificazione** sia per **tampering detection**?
il PRNU, essendo una firma propria di un solo dispositivo, avendo la matrice di riconoscimento, è possibile ricollegare un immagine ad un dispositivo, quidni l'identificazione. Inoltre è possibile verificare l'integrità del prnu anche in sezioni dell'immagine, per verificare se è stata modificata

Sottolinea la **correlation map**.

### 8.
Che cosa si intende per **format-level JPEG analysis** e che tipo di informazioni sfrutta?
non ricordo, vorrei fare un ripasso

La format-level JPEG analysis analizza la struttura del file JPEG, come tabelle di quantizzazione, codici di Huffman, dimensioni dell’immagine e metadata EXIF. Poiché lo standard JPEG non impone scelte uniche, queste informazioni costituiscono una firma utile per identificare brand, modello o software di editing.

### 9.
Qual è la differenza principale tra **signal-level methods** (es. PRNU) e **format-level methods** (JPEG header)?
non ricordo, vorrei fare un ripasso

I metodi signal-level analizzano tracce presenti nel contenuto dell’immagine (es. PRNU, CFA), mentre i metodi format-level analizzano la struttura del file e i parametri di compressione. I primi permettono il device-level, i secondi sono tipicamente limitati a brand/model identification.

### 10.
Che cosa cambiano gli scenari di **perfect knowledge**, **limited knowledge** e **zero knowledge** nel modo di affrontare la source identification?
non ricordo, vorrei fare un ripasso

Nel perfect knowledge scenario sono noti tutti i modelli e si usa una classificazione multiclasse. Nel limited knowledge scenario è noto solo il target e si verifica la compatibilità. Nel zero knowledge scenario non si conosce nulla a priori e si ricorre al clustering non supervisionato.