### **3. The U.S. Legal Framework for Software Copyright (2 pagine)**
#### **3.1 Copyright Act of 1976 and CONTU**
- software come literary work
- §117
#### **3.2 Fair Use and Judicial Interpretation**
- ruolo delle corti
- fair use come strumento di flessibilità
- reverse engineering e interoperabilità
👉 Qui fai vedere il **“judge-made law”**.

# Vr 2

## **3. The U.S. Approach to Software Copyright (2 pagine)**
**Struttura interna**
### 3.1 Copyright Act of 1976 and CONTU
- Inclusione del software tra le “literary works”.
- Section 117: backup e adattamenti necessari.
### 3.2 Judge-made law and Fair Use
- Ruolo centrale delle corti.
- Fair use come **strumento flessibile**:
    - studio del software
    - compatibilità
    - innovazione
- Breve riferimento a casi emblematici (senza appesantire troppo).
**Messaggio chiave**  
👉 Sistema **meno prevedibile**, ma più adattabile all’evoluzione tecnologica.

---
### **3.1 Copyright Act of 1976 e CONTU**
Negli Stati Uniti la disciplina fondamentale che regola il diritto d’autore è il **Copyright Act del 1976**, entrato in vigore il 1° gennaio 1978 come **Pub. L. No. 94-553**. Questa legge ha profondamente riformato il sistema, spostando la protezione da un regime legato alla **pubblicazione con avviso formale** verso un sistema in cui la protezione dei _works of authorship_ sussiste finché l’opera è **fissata in un supporto tangibile e originale** (tangible medium of expression).

Il Copyright Act non elencava originariamente i programmi informatici come una categoria distinta, ma riconosceva nei “**literary works**” (_opere letterarie_) anche quei materiali fissati in forma leggibile da un dispositivo, senza distinzione tra contenuto testuale tradizionale e codice sorgente o oggetto. In altri termini, il software poteva essere protetto come opera letteraria se soddisfaceva i requisiti di **originalità** e fissazione, pur se il legislatore non aveva ancora definito esplicitamente “computer program” all’interno del testo originario della legge.

Il dibattito e l’incertezza interpretativa nel periodo post-1976 su come applicare queste disposizioni al software portarono alla creazione della **Commission on New Technological Uses of Copyrighted Works (CONTU)** nel 1974, con mandato di studiare l’impatto delle tecnologie emergenti sui diritti d’autore. CONTU concluse che i programmi informatici dovevano essere espressamente riconosciuti all’interno del diritto d’autore per evitare lacune e incertezze, in particolare riguardo alle copie macchina-leggibili e alle operazioni informatiche non contemplabili nei paradigmi tradizionali del diritto d’autore. Le raccomandazioni della Commissione furono in gran parte recepite dal Congresso e confluirono nell’**amendment noto come Computer Software Copyright Act del 1980**, che modificò il Copyright Act includendo una definizione di _computer program_ e adattando specifiche norme per i software.[1 - 2]

In particolare, la definizione inserita descrive un _computer program_ come **“un insieme di istruzioni o enunciati da usare direttamente o indirettamente in un computer per ottenere un risultato specifico”**. Tale definizione chiarisce che **sia il codice sorgente sia il codice oggetto**, anche se non leggibile dall’uomo, rientrano nell’ambito delle opere letterarie tutelate dal Copyright Act, purché fissati in un supporto e originali.[3]
#### **La sezione 117 – deroghe alla esclusiva**

Una modifica cruciale introdotta nel 1980 su raccomandazione di CONTU riguarda la **Sezione 117 (§117) del Copyright Act**, che disciplina le **limitazioni al diritto esclusivo** del titolare del copyright nel caso di programmi informatici. Mentre il diritto esclusivo di riproduzione e di creazione di opere derivate è generalmente previsto da §106 dell’Act, §117 introduce **eccezioni specifiche per i software** per tener conto della loro natura funzionale e dell’uso pratico dei programmi nelle macchine.[4 - 5]

Secondo §117(a), **non costituisce violazione del diritto d’autore** la realizzazione di una copia aggiuntiva o la creazione di una “adattazione” di un programma da parte di chi detiene legalmente una copia, **se tale copia è essenziale per l’utilizzo del programma in connessione con un computer** e **non viene usata in altro modo**, oppure se è fatta **per scopi di archivio (backup)**, distruggendo la copia di backup se si cessa di possedere il programma originale.

In altre parole, §117 riconosce che l’esecuzione e l’uso di un software su un computer comportano **di per sé copie del programma** (ad esempio quando il codice viene caricato in memoria). Senza questa deroga, attività ordinarie come l’avvio del software o l’installazione sul disco rigido avrebbero potuto costituire riproduzioni non autorizzate. §117 permette, inoltre, che copie fatte per manutenzione o riparazione delle macchine siano regolari se non utilizzate in altri contesti.

Queste disposizioni riflettono una **funzione equilibratrice**: da una parte il regime statunitense mantiene la protezione generale del software come opera letteraria tramite copyright; dall’altra, consente **eccezioni calibrate alle esigenze tecniche dell’uso informatico**, lasciando tuttavia alle corti il compito di definire con precisione i limiti di tali deroghe attraverso la giurisprudenza, ad esempio, nelle controversie successivamente sorte su reverse engineering e interoperabilità.

### **3.2 Fair Use e interpretazione giurisprudenziale**

Negli Stati Uniti il regime di tutela del software non si limita alle disposizioni testuali del Copyright Act, ma si costruisce in gran parte attraverso **l’interpretazione delle corti federali**, in particolare tramite la dottrina del **fair use** (17 U.S.C. §107). Questa dottrina non è un’eccezione specifica come quelle previste nella normativa europea (es. interoperabilità nella Direttiva 91/250/EEC), ma piuttosto un **strumento giuridico elastico** che consente ai giudici di equilibrare la protezione del titolare con interessi collettivi quali innovazione, concorrenza e interoperabilità. [6]

**Fair use come strumento di flessibilità.** Secondo la Sezione 107 del Copyright Act, una _“fair use”_ può essere riconosciuta quando l’uso di un’opera protetta avviene per finalità come critica, commento, ricerca, insegnamento o **analisi tecnica**, considerando quattro fattori: (i) scopo e carattere dell’uso; (ii) natura dell’opera; (iii) quantità e sostanzialità usata; (iv) effetto sul mercato potenziale dell’opera originale. La natura _bilanciante_ di questa dottrina dà al giudice ampio margine di adattamento ai casi concreti, specialmente nel contesto software dove molte attività tecniche non rientrano facilmente nelle categorie tradizionali di uso consentito.[7]

Un esempio classico del ruolo delle corti nell’applicazione del fair use al software è **Sega Enterprises Ltd. v. Accolade (1992)**. Nel caso, Accolade aveva disassemblato il codice del videogioco Sega per comprendere aspetti funzionali necessari a produrre giochi compatibili con la console Genesis. La Corte d’Appello del Nono Circuito ha ritenuto la reverse engineering un uso equo (_fair use_), poiché l’obiettivo era ottenere informazioni funzionali non protette da copyright per creare software compatibile, promuovendo così innovazione e concorrenza.[6 - 8]

Un altro caso significativo è **Sony Computer Entertainment v. Connectix (2000)**, in cui il Nono Circuito ha confermato che la copia di sezioni di codice durante il processo di sviluppo di un emulatore non costituiva violazione, perché l’attività di reverse engineering era finalizzata a produrre un software nuovo e trasformativo, e non a sostituire il mercato dell’opera originale. Questo consolidò la giurisprudenza che il fair use può giustificare la copia intermedia richiesta per comprendere aspetti funzionali del software.[9]

**Google v. Oracle: fair use su API software.** Molto discusso è anche il caso **Google LLC v. Oracle America, Inc. (2021)**. Qui la Corte Suprema degli Stati Uniti ha confermato che l’uso di alcune parti dell’API Java da parte di Google per consentire agli sviluppatori Java di scrivere applicazioni Android costituiva fair use. Pur assumendo per il bene dell’argomento che quelle parti fossero protette da copyright, la Corte si è concentrata sull’applicazione dei quattro fattori del fair use e ha ritenuto l’uso “trasformativo” e socialmente utile, sottolineando che il fair use può adattarsi alle **particolarità tecniche del software** come strumento di bilanciamento tra esclusiva e innovazione tecnologica.[10 - 11]

**Reverse engineering e interoperabilità.** La giurisprudenza U.S. ha in vari casi riconosciuto che il fair use può estendersi anche alla pratica del reverse engineering quando esso è l’unico modo per accedere a elementi funzionali _non protetti_ del software. Ciò riflette l’idea che la protezione del copyright non debba bloccare la libertà di sviluppare software interoperabile con altri programmi, purché l’uso del codice originale sia **limitato a ciò che è necessario** e non arrechi un danno significativo al mercato dell’opera protetta.[12]

In sintesi, mentre l’Unione Europea prevede eccezioni esplicite e codificate (es. decompilazione per interoperabilità), il sistema statunitense affida alla **dottrina del fair use** e alla **giurisprudenza delle corti** il compito di definire caso per caso i limiti della tutela del software, riuscendo così ad adattarsi alle complesse esigenze tecniche dell’era digitale ma introducendo anche una maggiore **indeterminazione normativa**.

---
1. https://en.wikipedia.org/wiki/CONTU
2. https://www.congress.gov/bill/96th-congress/house-bill/6934
3. https://www.c2st.org/the-computer-software-copyright-act-of-1980
4. https://www.law.cornell.edu/uscode/text/17/117
5. https://www.bitlaw.com/source/17usc/117.html
6. https://en.wikipedia.org/wiki/Limitations_on_exclusive_rights%3A_Computer_programs
7. https://www.jdsupra.com/legalnews/supreme-court-expands-upon-software-1221531
8. https://en.wikipedia.org/wiki/Sega_v._Accolade
9. https://en.wikipedia.org/wiki/Sony_Computer_Entertainment%2C_Inc._v._Connectix_Corp
10. https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf
11. https://www.clearygottlieb.com/news-and-insights/publication-listing/the-supreme-courts-decision-in-google-v-oracle
12. https://en.wikipedia.org/wiki/Limitations_on_exclusive_rights%3A_Computer_programs

---
# Versione snellita

### **3.1 Copyright Act, CONTU e qualificazione del software**

Negli Stati Uniti, la disciplina fondamentale in materia di diritto d’autore è il **Copyright Act del 1976**, entrato in vigore nel 1978, che ha riformato il sistema spostando la protezione da un modello formale legato alla pubblicazione a un regime fondato sulla **fissazione dell’opera in un supporto tangibile e sull’originalità**. Sebbene il testo originario non menzionasse espressamente i programmi informatici, la categoria dei _literary works_ era formulata in modo sufficientemente ampio da includere materiali leggibili da un dispositivo, consentendo in linea di principio la protezione del software come opera letteraria.

Le incertezze interpretative emerse nella seconda metà degli anni Settanta portarono all’istituzione della **Commission on New Technological Uses of Copyrighted Works (CONTU)**, incaricata di valutare l’impatto delle nuove tecnologie sul diritto d’autore. CONTU concluse che i programmi informatici dovessero essere esplicitamente ricompresi nel sistema del copyright per evitare lacune normative, in particolare con riferimento alle copie macchina-leggibili e alle operazioni tecniche necessarie all’uso del software. Tali raccomandazioni confluirono nel **Computer Software Copyright Act del 1980**, che introdusse una definizione normativa di _computer program_ e chiarì che **sia il codice sorgente sia il codice oggetto** possono costituire espressione protetta, purché originali e fissati in un supporto.[1 – 3]

Questa scelta ha consolidato l’assimilazione del software alle opere letterarie, pur senza risolvere tutte le tensioni derivanti dalla sua natura funzionale, già evidenziate nel capitolo precedente.

### **3.2 La Sezione 117 e le deroghe funzionali**

Un elemento centrale dell’approccio statunitense è rappresentato dalla **Sezione 117 (§117) del Copyright Act**, introdotta nel 1980 su raccomandazione di CONTU. Essa prevede limitazioni specifiche ai diritti esclusivi del titolare nel caso di programmi informatici, riconoscendo che l’uso di un software comporta necessariamente atti di riproduzione e adattamento tecnico.

In particolare, §117 consente al legittimo acquirente di un programma di realizzare copie o adattamenti **quando ciò sia essenziale per l’utilizzo del software in connessione con un computer** oppure per finalità di **archiviazione (backup)**, a condizione che tali copie non siano utilizzate in altri contesti.[4 – 5] In questo modo, il legislatore statunitense ha evitato che operazioni tecnicamente inevitabili, come il caricamento del codice in memoria, potessero configurare violazioni del diritto d’autore.

La Sezione 117 rappresenta dunque un primo tentativo di **adattamento funzionale del copyright al software**, ma lascia ampi margini interpretativi, rimettendo alle corti la definizione concreta dei limiti delle deroghe.

### **3.3 Fair use e ruolo della giurisprudenza**

A differenza dell’ordinamento europeo, il sistema statunitense affida un ruolo centrale alla **dottrina del fair use** (17 U.S.C. §107) come strumento di bilanciamento tra tutela dei diritti esclusivi e interessi quali innovazione, concorrenza e interoperabilità. Il fair use non costituisce un’eccezione tipizzata, ma uno **standard aperto**, applicato caso per caso sulla base di quattro fattori, che consente alle corti di adattare la disciplina del copyright alle peculiarità tecniche del software.[6 – 7]

In questo quadro, la giurisprudenza ha riconosciuto che attività di **reverse engineering** possono rientrare nel fair use quando siano finalizzate all’accesso a elementi funzionali non protetti dal diritto d’autore e risultino necessarie per lo sviluppo di software interoperabile. Casi come _Sega v. Accolade_ e _Sony v. Connectix_ hanno chiarito che la copia intermedia del codice, pur costituendo una riproduzione, può essere lecita se limitata allo stretto necessario e priva di effetti sostitutivi sul mercato dell’opera originale.[8 – 9]

Questo approccio è stato ulteriormente confermato dalla Corte Suprema nel caso _Google v. Oracle_, in cui l’uso di parti delle API Java è stato ritenuto fair use in quanto funzionale alla creazione di una piattaforma innovativa e compatibile, sottolineando il ruolo del fair use come **meccanismo flessibile di adattamento del copyright alle esigenze dell’industria del software**.[10 – 11]
### **3.4 Sintesi del modello statunitense**

Nel complesso, il modello statunitense di tutela del software si caratterizza per una protezione formale ampia, fondata sull’assimilazione del software alle opere letterarie, bilanciata però da **deroghe funzionali** (§117) e da un ricorso esteso alla **giurisprudenza e al fair use** per affrontare questioni quali interoperabilità e reverse engineering. Questo assetto consente un’elevata adattabilità ai mutamenti tecnologici, ma comporta anche un maggiore grado di **incertezza giuridica**, affidando la definizione dei confini della tutela all’evoluzione interpretativa delle corti.