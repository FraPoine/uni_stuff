# **1. La protezione giuridica del software**

La storia della protezione legale del software è strettamente intrecciata con l’evoluzione dell’informatica come disciplina accademica e, successivamente, come settore industriale. Nei primi decenni, tra anni ’50 e ’70, la comunità scientifica lavorava con un forte spirito di condivisione: i primi linguaggi di programmazione, i sistemi operativi sperimentali e gli ambienti di sviluppo nascevano all’interno delle università e venivano scambiati liberamente. È in questo contesto che nasce Unix nei laboratori Bell di AT&T, un sistema che inizialmente circolava in forma di codice sorgente presso istituti di ricerca, contribuendo enormemente alla diffusione delle idee tecniche di base dell’informatica moderna.

Tuttavia, con la progressiva commercializzazione dell’industria del software, AT&T iniziò a imporre restrizioni, chiedendo di mantenere segreto il codice Unix per garantirsi la tutela come segreto industriale. Questo cambiamento rese evidente l’esigenza di norme giuridiche più chiare: il software, fino ad allora, non rientrava nemmeno nella definizione di opera protetta dal copyright, che richiedeva una forma comprensibile “a occhio nudo”. Solo nel 1976 il nuovo Copyright Act statunitense introdusse una definizione di "opera letteraria" abbastanza ampia da includere anche il codice di un programma.

Negli anni successivi la legislazione si adattò ulteriormente. Nel 1980, grazie ai lavori della commissione CONTU, vennero introdotte norme specifiche che riconoscevano il software come un’opera tutelata, ma con eccezioni necessarie al suo utilizzo: per esempio, era consentita la copia di backup o la modifica del programma per esigenze operative dell’utente.

Parallelamente, anche l’Europa sentì la necessità di normare il settore. Con la direttiva 91/250/CEE, poi aggiornata nel 2009, si stabilì che i programmi per computer sono protetti come opere letterarie, ma che idee, principi e concetti alla base del loro funzionamento non possono essere monopolizzati. La direttiva definisce inoltre i diritti esclusivi del titolare (riproduzione, modifica, distribuzione), introducendo però importanti eccezioni come la possibilità di osservare il programma o di decompilarlo quando ciò è indispensabile per ottenere interoperabilità.

---

# **2. Il movimento del Free Software, l’Open Source e i modelli di sviluppo**

Il movimento del software libero nasce come reazione a un clima sempre più restrittivo nel mondo della programmazione. Emblematico è il caso della stampante del MIT AI Lab, il cui codice non venne condiviso da un ricercatore esterno: un episodio che spinge Richard Stallman a riflettere sull’impatto sociale delle restrizioni sul software. Da questa consapevolezza, nel 1984 Stallman lascia il MIT e fonda prima il progetto GNU e poi la Free Software Foundation, con l’obiettivo ambizioso di creare un sistema operativo completamente libero.

Al centro di questa filosofia ci sono le “quattro libertà”: la libertà di eseguire un programma, di studiarlo, di modificarlo e di ridistribuirlo. La GNU General Public License (GPL), pubblicata nel 1989, rappresenta il pilastro giuridico di queste libertà: attraverso il meccanismo del copyleft, garantisce che chiunque redistribuisca il software – anche modificandolo – debba mantenere le stesse libertà per gli utenti futuri.

Negli anni ’90 la dinamica dello sviluppo collaborativo subisce una trasformazione radicale con l’arrivo di Linux, il kernel creato da Linus Torvalds. A differenza dei progetti della FSF, Linux viene sviluppato in modo distribuito, senza una struttura gerarchica rigida, grazie a Internet e alla collaborazione spontanea di migliaia di sviluppatori. La combinazione del kernel Linux con gli strumenti GNU dà origine al primo sistema operativo completamente libero, comunemente conosciuto come GNU/Linux.

Parallelamente si afferma anche la famiglia dei sistemi BSD: derivati dal lavoro di Berkeley, dopo la rimozione del codice AT&T diventano completamente liberi e danno vita a progetti indipendenti come FreeBSD, OpenBSD e NetBSD.

Sul finire degli anni ’90 nasce poi l’Open Source Initiative, una risposta strategica al timore che il termine “free software” fosse ambiguo o poco gradito al mondo delle imprese. L’OSI propone un approccio più pragmatico, definendo l’Open Source Definition e certificando un numero crescente di licenze. Questa proliferazione, tuttavia, porta anche a nuovi problemi: incompatibilità tra licenze diverse e difficoltà nella riusabilità del codice.

---

# **3. Le licenze FLOSS: categorie, principi e compatibilità**

Le licenze del software libero e open source si possono distinguere innanzitutto in due grandi famiglie: **copyleft** e **non-copyleft**. Le licenze copyleft, come la GPL e l’AGPL, garantiscono che ogni redistribuzione del codice (anche modificato) mantenga le stesse libertà previste dalla licenza originale. La logica è quella di impedire che un soggetto possa privatizzare un lavoro collettivo. All’interno del copyleft esistono vari gradi di “forza”: le versioni forti obbligano a mantenere la stessa licenza per qualsiasi derivato, mentre quelle deboli, come la LGPL o la MPL, consentono una maggiore flessibilità, soprattutto nel caso di librerie.

Le licenze non-copyleft, o permissive, come BSD, MIT o Apache, adottano un approccio diverso: permettono infatti di riutilizzare il codice anche all’interno di software proprietario. È un modello che favorisce la massima libertà di riutilizzo, ma senza la garanzia che le libertà rimangano anche nelle opere derivate. Un esempio interessante è l’evoluzione delle licenze BSD: la versione originale richiedeva una clausola pubblicitaria molto invasiva, poi rimossa per agevolare la diffusione del codice.

La GPL nel tempo ha continuato a evolversi. La versione 3 introduce maggiore protezione contro pratiche come la “tivoizzazione”, ovvero l’imposizione di restrizioni hardware che impediscono all’utente di modificare un software pur essendo formalmente libero. Inoltre, migliora la compatibilità con la licenza Apache 2.0 grazie a specifiche clausole sui brevetti.

Altre licenze particolari includono l’AGPL, pensata per il software utilizzato in rete: impone la divulgazione del codice sorgente anche quando gli utenti interagiscono con il programma tramite servizi online, colmando un limite della GPL tradizionale.

La compatibilità tra licenze è un tema complesso. Alcune combinazioni sono impossibili: ad esempio, codice Apache 2.0 non può essere integrato in un progetto sotto GPLv2. La Mozilla Public License 2.0 fa un passo avanti, introducendo il concetto di “Secondary License”, che permette – in certi casi – di ridistribuire il codice anche sotto licenze della famiglia GPL, facilitando l’interoperabilità.

Infine, esiste il modello del **multi-licensing**, attraverso il quale un progetto può essere distribuito contemporaneamente con una licenza libera e una proprietaria. È una strategia commerciale adottata da software come Asterisk o Qt, che combina apertura e sostenibilità economica.

---
---

# Secondo tentativo

# **1. La protezione giuridica del software**

La storia della tutela del software è strettamente collegata all’evoluzione dell’informatica. In origine, l’informatica nasce come disciplina accademica, basata sulla condivisione del sapere: i primi linguaggi di programmazione, le prime tecniche di time-sharing e perfino i primi sistemi operativi venivano sviluppati nelle università e scambiati liberamente. Un esempio significativo è Unix, creato tra il 1969 e il 1973 ai Bell Labs. Per molti anni AT&T, che ne deteneva il copyright, ne permetteva la distribuzione alle università in formato sorgente, favorendo la crescita della comunità scientifica. Tutto cambia però alla fine degli anni ’70, quando AT&T decide di impedire che il codice Unix venga usato per insegnare. Per continuare a formare nuovi programmatori, alcuni studiosi iniziano allora a creare sistemi alternativi liberi da vincoli, come MINIX.

Sul piano giuridico, la situazione era altrettanto in evoluzione. Fino al 1976 il software non poteva essere protetto dal diritto d’autore perché la legge statunitense richiedeva che l’opera fosse leggibile “a occhio nudo”, cosa impossibile per un programma. Con il nuovo Copyright Act del 1976, e poi con gli interventi della commissione CONTU nel 1980, il software viene finalmente riconosciuto come opera letteraria. Da quel momento è tutelato dal copyright, ma con alcune eccezioni fondamentali per il suo utilizzo, come la possibilità di creare copie di backup o di modificare il programma per esigenze personali.

In Europa il percorso è analogo. Dagli anni ’80 diversi Stati iniziano a introdurre norme specifiche, fino alla direttiva del 1991 (poi aggiornata nel 2009) che stabilisce che i programmi per computer sono protetti come opere letterarie. La direttiva introduce principi fondamentali: si proteggono solo le espressioni del software, non le idee o i principi alla base del suo funzionamento, e gli utenti legittimi hanno diritti minimi irrinunciabili, come studiare il programma o decompilarlo quando ciò è necessario per renderlo interoperabile con altri sistemi. Queste norme formano ancora oggi la base della protezione giuridica del software in Europa.

---

# **2. Free Software, Open Source e modelli di sviluppo**

L’idea di software libero nasce come reazione alle crescenti restrizioni imposte nell’ambiente informatico. Un episodio simbolico riguarda Richard Stallman, ricercatore del MIT, che racconta di quando non gli fu concesso il codice sorgente necessario per migliorare la stampante del laboratorio. L’idea che un programmatore non potesse aiutare il proprio collega perché vincolato da un accordo di riservatezza divenne per lui inaccettabile. Per questo, nel 1984 Stallman lascia il MIT e avvia il progetto GNU, con l’obiettivo di creare un sistema operativo completamente libero, basato su quattro libertà fondamentali: eseguire il programma, studiarlo, modificarlo e ridistribuirlo.

Per garantire che queste libertà non fossero mai compromesse, nel 1989 nasce la GNU General Public License (GPL), una licenza innovativa che utilizza il diritto d’autore in modo “inverso”: invece di creare monopoli, assicura che il software rimanga libero in ogni futura redistribuzione. Nei primi anni ’90 GNU aveva già sviluppato quasi tutti gli strumenti necessari a un sistema operativo completo, mancava solo un kernel. La soluzione arrivò nel 1991, quando Linus Torvalds rilasciò Linux e poco dopo lo distribuì sotto GPL. L’unione di GNU e Linux diede vita a un nuovo modello di sviluppo, più aperto e collaborativo, basato su contributi spontanei da tutto il mondo e organizzato tramite Internet.

Accanto al mondo GNU/Linux cresce anche quello dei sistemi BSD, eredi del lavoro dell’Università di Berkeley. Dopo anni di dispute legali con AT&T, negli anni ’90 il codice BSD diventa completamente libero e dà vita a progetti indipendenti come FreeBSD, OpenBSD e NetBSD. Questi sistemi si diffondono grazie alla loro stabilità e alla loro licenza molto permissiva.

Sul finire degli anni ’90, il movimento del software libero incontra un nuovo ostacolo: la percezione negativa del termine “free software” nel mondo aziendale. Molti pensavano erroneamente che significasse “gratuito”, oppure temevano la rigidità del copyleft. È in questo contesto che nasce l’Open Source Initiative, che propone un nuovo nome e un approccio più pragmatico, basato su una definizione formale dei requisiti di apertura del codice. L’OSI approva molte licenze diverse, favorendo così una grande espansione dell’open source, ma anche generando problemi di compatibilità tra licenze e una crescente difficoltà nella gestione dei progetti.

---

# **3. Le licenze FLOSS: categorie, principi e compatibilità**

Le licenze del software libero e open source si dividono principalmente in due categorie. Le licenze copyleft, come la GPL, richiedono che ogni versione ridistribuita del software — anche se modificata — rimanga sotto la stessa licenza. Questo meccanismo garantisce che le libertà originarie non vengano mai rimosse. Ne esistono forme più rigide, che impongono il copyleft a tutto il software derivato, e forme più deboli, come la LGPL o la MPL, pensate soprattutto per le librerie, che permettono di combinare il codice libero con software proprietario.

Dall’altra parte ci sono le licenze permissive, come la MIT, la BSD o la Apache. Queste licenze non impongono vincoli sulle opere derivate e permettono anche l’integrazione del codice all’interno di software chiuso. Sono molto apprezzate nel mondo industriale perché offrono la massima flessibilità, anche se non garantiscono che il codice rimanga libero nel tempo.

Con il passare degli anni, molte licenze hanno subito aggiornamenti importanti. La GPLv3, ad esempio, è stata creata per rispondere a nuove sfide come i brevetti software e la tivoizzazione, una pratica che permette agli utenti di ottenere il codice libero ma impedisce loro di installare versioni modificate sul proprio dispositivo. Inoltre, la GPLv3 migliora la compatibilità con altre licenze, come la Apache 2.0, che era invece incompatibile con la GPLv2.

Alcune licenze si distinguono per obiettivi particolari. L’AGPL, per esempio, estende il copyleft al software utilizzato tramite rete: se un servizio online utilizza codice sotto AGPL, deve rendere disponibile il sorgente anche agli utenti che lo utilizzano via web. La MPL introduce invece il concetto di “secondary license”, che permette di rendere compatibile il proprio codice con licenze della famiglia GPL quando necessario.

Infine, esiste anche la pratica del multi-licensing, in cui un progetto viene distribuito sotto più licenze differenti, spesso una libera e una proprietaria. Questo modello consente agli sviluppatori di finanziare il progetto vendendo versioni commerciali, pur mantenendo una variante libera per la comunità. È un equilibrio tra apertura e sostenibilità economica, adottato in passato da software come Asterisk o Qt.

---
---
# SOOOOOO

# Legal Protection Of Software

La storia della tutela del software è strettamente collegata all’evoluzione dell’informatica. In origine, l’informatica nasce come disciplina accademica, basata sulla condivisione del sapere. n esempio significativo è , creato tra il 1969 e il 1973 ai Bell Labs. Per molti anni AT&T, che deteneva il copyright di Unix, ne permetteva la distribuzione alle università, favorendo la crescita della comunità scientifica, ma nel 1979 decise di impedire che Unix venga usato per insegnare. Così per continuare a formare nuovi programmatori, alcuni studiosi iniziano allora a creare sistemi alternativi liberi da vincoli, come MINIX.

Fino al 1976 il software non poteva essere protetto dal diritto d’autore perché la legge statunitense richiedeva che l’opera fosse leggibile “a occhio nudo”, cosa impossibile per un programma. Con il nuovo Copyright Act del 1976, e poi con gli interventi della commissione CONTU nel 1980, il software viene finalmente riconosciuto come opera letteraria. Da quel momento venne tutelato dal copyright, ma con alcune eccezioni fondamentali per il suo utilizzo, come la possibilità di creare copie di backup o di modificare il programma per esigenze personali.

In Europa dagli anni ’80 diversi Stati iniziarono a introdurre norme specifiche, fino alla direttiva del 1991 che stabilisce che i programmi per computer sono protetti come opere letterarie. La direttiva idice che  si proteggono solo le espressioni del software, non le idee o i principi alla base del suo funzionamento, e gli utenti legittimi hanno diritti minimi irrinunciabili, come studiare il programma o decompilarlo quando ciò è necessario per renderlo interoperabile con altri sistemi.

# Free Software

Il movimento del software libero nasce negli anni ’80. Nel 1984 viene avviato il progetto GNU, con l’obiettivo di creare un sistema operativo completamente libero, basato su quattro libertà fondamentali: eseguire il programma, studiarlo, modificarlo e ridistribuirlo.

Nel 1989 nasce la GNU General Public License (GPL), una licenza che utilizza il diritto d’autore in modo “inverso”: invece di creare monopoli, assicura che il software rimanga libero in ogni futura redistribuzione. Nei primi anni ’90 GNU aveva già sviluppato quasi tutti gli strumenti necessari a un sistema operativo completo, mancava solo un kernel. La soluzione arrivò nel 1991, quando venne rilasciato Linux e poco dopo venne distribuito sotto GPL. L’unione di GNU e Linux diede vita a un nuovo modello di sviluppo, più aperto e collaborativo, basato su contributi spontanei da tutto il mondo e organizzato tramite Internet.

Accanto al mondo GNU/Linux cresce anche quello dei sistemi BSD, eredi del lavoro dell’Università di Berkeley. Dopo anni di dispute legali con AT&T, negli anni ’90 il codice BSD diventa completamente libero e dà vita a progetti indipendenti.

Sul finire degli anni ’90, il movimento del software libero incontra un nuovo ostacolo: la percezione negativa del termine “free software” nel mondo aziendale. Molti pensavano erroneamente che significasse “gratuito”, oppure temevano la rigidità del copyleft. È in questo contesto che nasce l’Open Source Initiative, che propone un nuovo nome e un approccio più pragmatico, basato su una definizione formale dei requisiti di apertura del codice. L’OSI approva molte licenze diverse, favorendo così una grande espansione dell’open source, ma anche generando problemi di compatibilità tra licenze e una crescente difficoltà nella gestione dei progetti.

# Floss Licenses

Le licenze del software libero possono essere copyleft o permissive. Le prime, come la GPL e l’AGPL, garantiscono che il software e le sue modifiche rimangano sempre liberi, mentre quelle permissive, come MIT, BSD e Apache, permettono di usare il codice anche all’interno di programmi proprietari. Esistono anche forme di copyleft più leggere, come la LGPL o la MPL, che offrono maggiore flessibilità.

Le Creative Commons vengono talvolta citate come modello di licenze a vari livelli di apertura, ma sono pensate per opere artistiche o testuali, non per il software. Negli anni, alcune licenze sono state semplificate o aggiornate: la BSD ha eliminato clausole superflue, mentre la GPLv3 ha introdotto maggiore chiarezza, nuove tutele per gli utenti e una migliore compatibilità con la licenza Apache.

---
---
# versione più schematica

---

# **Legal Protection of Software**

**Origini e contesto**

- L’informatica nasce in ambiente accademico, con forte condivisione del sapere.
    
- Unix (1969–1973, Bell Labs) inizialmente distribuito liberamente alle università.
    
- Dal 1979 AT&T vieta l’uso didattico di Unix → nascono alternative libere come **MINIX**.
    

**Evoluzione del diritto d’autore**

- Fino al 1976: il software non è protetto dal copyright perché non è leggibile a occhio nudo.
    
- Copyright Act 1976: il software diventa opera letteraria.
    
- 1980 (CONTU): introdotte eccezioni fondamentali (backup, adattamento per uso personale).
    

**Normativa europea**

- Anni ’80: primi interventi nazionali.
    
- Direttiva 1991 → oggi 2009/24/CE:
    
    - Il software è protetto come opera letteraria.
        
    - Sono protette solo le **espressioni**, non le idee o i principi.
        
    - L’utente legittimo può studiare, osservare e decompilare il programma per ottenere interoperabilità.
        

---

# **Free Software**

**Origini del movimento**

- Anni ’80: nasce il movimento del software libero.
    
- 1984: avvio del progetto **GNU** → obiettivo: creare un sistema operativo libero basato su quattro libertà (esecuzione, studio, modifica, condivisione).
    

**La GPL e l’unione con Linux**

- 1989: nasce la **GNU GPL** → il copyright viene usato per garantire libertà (copyleft).
    
- Primi anni ’90: mancano solo il kernel; nel 1991 arriva **Linux**, poi rilasciato sotto GPL.
    
- GNU + Linux → primo sistema operativo completamente libero, sviluppato in modo aperto e collaborativo attraverso Internet.
    

**Il mondo BSD**

- BSD deriva dai lavori dell’Università di Berkeley.
    
- Dopo dispute legali, negli anni ’90 il codice diventa libero → nascono progetti indipendenti (FreeBSD, NetBSD, OpenBSD).
    

**Nascita dell’Open Source**

- Fine anni ’90: problemi di percezione del termine “free software” nelle aziende.
    
- Nasce l’**Open Source Initiative (OSI)** → approccio pragmatico e definizione formale dell’open source.
    
- Crescono licenze e progetti, ma anche problemi di compatibilità tra licenze.
    

---

# **FLOSS Licenses**

**Tipologie principali**

- **Copyleft**: richiedono che software e derivati restino liberi (GPL, AGPL).
    
- **Permissive**: permettono anche l’uso in software proprietario (MIT, BSD, Apache).
    
- **Copyleft deboli**: permettono maggiore flessibilità (LGPL, MPL).
    

**Creative Commons**

- Citati come modello di licenze modulari, ma non adatti al software.
    
- Usati per opere artistiche e testuali.
    

**Evoluzioni e aggiornamenti**

- Le licenze BSD moderne eliminano clausole superflue.
    
- La **GPLv3** introduce:
    
    - linguaggio più chiaro,
        
    - tutele contro limitazioni imposte dall’hardware,
        
    - compatibilità migliore con Apache 2.0.