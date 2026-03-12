### **2. Background (2 pagine)**
#### **2.1 Technical Nature of Software**
- codice sorgente / oggetto
- algoritmi, interfacce, interoperabilità
- reverse engineering (cos’è tecnicamente)
#### **2.2 Copyright and Software: General Issues**
- idea/expression dichotomy
- perché il software è un caso limite
- perché serve un intervento normativo specifico
👉 Questa sezione è l’equivalente del suo “Network Neutrality + 5G”.

## **2. Technical Background: What is Software and Why Law Struggles to Regulate It (1–1.5 pagine)**
Qui fai vedere che **capisci l’informatica**.
**Contenuti**
- Distinzione:
    - codice sorgente vs codice oggetto   
    - idea / algoritmo / funzione vs implementazione  
- Concetti tecnici chiave:
    - interoperabilità
    - reverse engineering
    - decompilazione
- Perché **proteggere il software come un libro è problematico**.
👉 Questa sezione giustifica **perché UE e USA hanno fatto scelte diverse**.

---
### **2.1 Codice sorgente e codice oggetto**

Dal punto di vista tecnico, un programma software può presentarsi in forme diverse, ciascuna delle quali ha implicazioni rilevanti anche sul piano giuridico. Il **codice sorgente** (_source code_) è la forma **leggibile dall’essere umano** in cui un programmatore scrive le istruzioni utilizzando un linguaggio di programmazione ad alto livello (come C, Python o Java). Questa forma di codice contiene dichiarazioni, logica e struttura del programma che possono essere modificate, analizzate e comprese direttamente da un essere umano. [1]

Il **codice oggetto** (_object code_), invece, è il risultato della **traduzione automatica del codice sorgente in linguaggio macchina** (binario) effettuata da un compilatore. Esso è destinato all’esecuzione diretta da parte dell’hardware ed è, nella pratica, incomprensibile o difficilmente interpretabile per l’essere umano che non disponga del codice sorgente originale.[2]

La distinzione tra queste due forme è importante perché, mentre il codice sorgente rappresenta il **progetto e l’implementazione voluta dal programmatore**, il codice oggetto esprime la **funzionalità eseguibile** di quel progetto: dal punto di vista giuridico entrambi sono considerati “espressione” di un programma, ma la **capacità di leggerli o modificarli cambia radicalmente il loro ruolo nell’uso, nella distribuzione e nell’analisi tecnica dei software**.[1 - 2]

### **2.2 Idee, algoritmi, interoperabilità e tecniche di analisi del software**

L’analisi di un programma informatico richiede di distinguere tra il **livello concettuale** e quello **implementativo**. L’**idea** o la **funzione** di un software descrive ciò che il programma è destinato a fare, mentre l’**algoritmo** individua il procedimento logico attraverso cui tale funzione viene realizzata. Questi elementi sono astratti e indipendenti dalla forma concreta del codice: uno stesso algoritmo può essere implementato in linguaggi diversi o attraverso soluzioni tecniche differenti. L’**implementazione** rappresenta invece la traduzione concreta dell’algoritmo in codice sorgente e, successivamente, in codice oggetto per l’esecuzione da parte del calcolatore. In termini giuridici, la tutela del diritto d’autore riguarda tipicamente l’implementazione espressa nel codice, e non l’idea o l’algoritmo in quanto tali, che rientrano nella sfera delle funzionalità tecniche riutilizzabili. [3]

In un contesto software contemporaneo, assume particolare rilievo il concetto di **interoperabilità**, intesa come la capacità di programmi diversi di comunicare, scambiarsi dati o funzionare insieme. Per garantire interoperabilità è spesso necessario comprendere come un programma interpreta dati, quali formati utilizza o quali interfacce espone. Quando tali informazioni non sono disponibili, si ricorre a tecniche di **reverse engineering**, che consistono nell’analisi di un programma partendo dalla sua forma eseguibile al fine di ricostruirne il comportamento o la struttura logica. [4]

Una forma specifica di reverse engineering è la **decompilazione**, che mira a tradurre il codice oggetto in una rappresentazione più leggibile o in una forma intermedia, avvicinandosi al codice sorgente. Sebbene tecnicamente complessa e spesso incompleta, la decompilazione può essere indispensabile per comprendere interfacce, protocolli o formati necessari alla realizzazione di software interoperabile. [5]

Dal punto di vista giuridico, tali pratiche pongono problemi rilevanti: se da un lato la protezione del software come opera giustifica il controllo dell’autore sulla riproduzione e sulla traduzione del codice, dall’altro un divieto assoluto di queste attività rischierebbe di ostacolare concorrenza, innovazione e sviluppo di sistemi compatibili.
### 2. 3 Perché proteggere il software come un’opera letteraria è problematico

Le caratteristiche tecniche del software rendono problematica la sua assimilazione alle opere letterarie tradizionali. Pur essendo formalmente qualificato come _opera letteraria_, il software non è destinato alla fruizione umana diretta, ma all’esecuzione da parte di una macchina, e il suo utilizzo implica necessariamente atti di riproduzione e trasformazione tecnica del codice, come il caricamento in memoria o la traduzione in forma eseguibile. [1–2–6]

Inoltre, mentre un’opera letteraria comunica principalmente un contenuto informativo, il software incorpora **funzionalità operative**, algoritmi e comportamenti che possono essere realizzati attraverso implementazioni differenti dello stesso progetto concettuale. [3] La distinzione tra **idea, algoritmo e implementazione** diventa quindi cruciale: estendere la tutela del diritto d’autore oltre l’espressione del codice rischierebbe di attribuire un controllo esclusivo su elementi funzionali che, dal punto di vista tecnico, devono rimanere accessibili per consentire interoperabilità e sviluppo di software compatibile. [3–4–7]

In questo quadro, attività come il **reverse engineering** e la **decompilazione**, spesso necessarie per comprendere interfacce o comportamenti non documentati, risultano difficilmente conciliabili con una concezione puramente letteraria del copyright, poiché implicano operazioni di analisi che possono includere copie o traduzioni del codice oggetto. [4–5]

Questa tensione strutturale tra la **natura funzionale del software** e le categorie tradizionali del diritto d’autore spiega perché la protezione dei programmi informatici abbia richiesto adattamenti specifici e meccanismi di bilanciamento, e perché ordinamenti diversi abbiano adottato soluzioni differenti per conciliare tutela dell’implementazione, interoperabilità e innovazione tecnologica.

---
# Source
1. https://en.wikipedia.org/wiki/Source_code
2. https://en.wikipedia.org/wiki/Object_code
3. https://en.wikipedia.org/wiki/Algorithm
4. https://en.wikipedia.org/wiki/Interoperability
5. https://en.wikipedia.org/wiki/Decompiler
6. https://en.wikipedia.org/wiki/Reverse_engineering
7. Slide del corso: _Legal Protection of Software_
8. Slide del corso: _copyright\_law_

---
## **2. Background tecnico (versione snellita)**

### **2.1 Codice sorgente e codice oggetto**

Dal punto di vista tecnico, un programma software può presentarsi in forme diverse, rilevanti anche sul piano giuridico. Il **codice sorgente** (_source code_) è la forma leggibile dall’essere umano in cui il programmatore esprime la logica e la struttura del programma mediante un linguaggio di programmazione ad alto livello.[1]

Il **codice oggetto** (_object code_) è invece il risultato della traduzione automatica del codice sorgente in linguaggio macchina effettuata da un compilatore ed è destinato all’esecuzione diretta da parte dell’hardware, risultando di fatto non leggibile senza strumenti tecnici specifici.[2]

Sebbene entrambe le forme costituiscano espressione del programma ai fini della tutela giuridica, la loro diversa intelligibilità incide significativamente sulle modalità di utilizzo, distribuzione e analisi del software.[1 – 2]
### **2.2 Idee, algoritmi e interoperabilità**

L’analisi di un programma informatico richiede di distinguere tra **idea o funzione**, **algoritmo** e **implementazione**. L’idea descrive il risultato che il software è destinato a ottenere, mentre l’algoritmo individua il procedimento logico per conseguirlo; entrambi sono elementi astratti, indipendenti dalla forma concreta del codice e suscettibili di molteplici implementazioni tecniche.[3]

L’**implementazione** rappresenta invece la traduzione concreta dell’algoritmo in codice sorgente e, successivamente, in codice oggetto. In termini giuridici, la tutela del diritto d’autore riguarda tipicamente tale livello espressivo, e non l’idea o l’algoritmo in quanto tali.[3]

In questo contesto assume rilievo il concetto di **interoperabilità**, intesa come la capacità di programmi diversi di comunicare e funzionare insieme. Quando le informazioni necessarie non sono disponibili, l’interoperabilità può richiedere attività di **reverse engineering**, ossia l’analisi di un programma a partire dalla sua forma eseguibile per comprenderne il comportamento o le interfacce.[4 - 6] Una tecnica specifica è la **decompilazione**, che mira a ricostruire una rappresentazione più leggibile del codice oggetto, sebbene in forma spesso incompleta.[5]

### **2.3 I limiti della qualificazione del software come opera letteraria**

Le caratteristiche tecniche del software rendono problematica la sua assimilazione alle opere letterarie tradizionali. Pur essendo formalmente qualificato come _opera letteraria_, il software non è destinato alla fruizione umana diretta, ma all’esecuzione da parte di una macchina, e il suo utilizzo implica necessariamente atti di riproduzione e trasformazione tecnica del codice.[1 – 2]

Inoltre, il software incorpora funzionalità operative e algoritmi che possono essere realizzati attraverso implementazioni differenti dello stesso progetto concettuale.[3] La distinzione tra **idea, algoritmo e implementazione** diventa quindi centrale: un’estensione eccessiva della tutela oltre l’espressione del codice rischierebbe di attribuire un controllo esclusivo su elementi funzionali, con potenziali effetti restrittivi su interoperabilità e concorrenza.[3 - 4 - 7]

Questa tensione strutturale tra la natura funzionale del software e le categorie tradizionali del diritto d’autore spiega la necessità di discipline specifiche e di meccanismi di bilanciamento tra tutela dei diritti esclusivi, interoperabilità e innovazione tecnologica.