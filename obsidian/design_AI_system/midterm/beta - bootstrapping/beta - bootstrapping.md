## 1. Beta distribution
fino a quel punto una probabilità, per esempio la probabilità p che una moneta esca testa, era trattata come un numero fisso tra 0 e 1. 
La nuova idea è: **e se non sapessimo il vero valore di p?**
In quel caso non ha senso usare un solo numero secco; conviene invece usare una **distribuzione di probabilità sopra i possibili valori di p**

La **Beta** serve proprio a questo: 
- rappresenta la nostra credenza su quale possa essere il vero valore di una probabilità sconosciuta. 
Il PDF la presenta come una variabile casuale continua su $[0,1]$, con media e varianza proprie.

L’esempio della moneta con **9 teste su 10 lanci** serve a farti vedere perché una semplice stima 9/10 non basta.
Dire “la probabilità è 0.9” è troppo rigido: quei 10 lanci sono pochi, quindi dovremmo anche rappresentare **quanto siamo incerti**.
La Beta permette esattamente questo: non dice solo “il valore più plausibile è intorno a 0.9”, ma descrive anche quanto siamo concentrati lì attorno e quanta incertezza rimane.

Poi entra **Bayes**. Il PDF mostra che, se prima dei lanci parti con una credenza uniforme su p, allora dopo aver osservato h successi e t fallimenti, la distribuzione aggiornata di p ha forma Beta.

In sostanza, **i dati “piegano” la tua credenza iniziale verso i valori più compatibili** con quello che hai osservato. Per questo, con h teste e t croci, il **posterior** diventa una **Beta** con parametri legati a h+1 e t+1.

La parte “Beta as a prior” aggiunge un’altra idea importante: puoi partire non da una credenza uniforme, ma da una **prior** Beta che rappresenta ciò che pensi prima di vedere i dati. Il PDF la interpreta come se contenesse degli “**imaginary trials**”: una sorta di esperienza fittizia iniziale.

Quando poi osservi dati veri, aggiorni semplicemente i parametri. Il vantaggio enorme è che una prior Beta aggiornata con dati binomiali resta ancora una Beta: questa proprietà si chiama **conjugate prior**.

---
## 2. Adding random variables: la convoluzione
La seconda parte cambia tema: non si studia più una probabilità incerta, ma la **somma di variabili casuali**.

Il nome tecnico è **convolution**

ma il senso semplice è: “se conosco come si comportano X e Y, come si comporta X+Y?"
Il punto chiave è che non si sommano le PDF o le PMF in modo diretto; bisogna considerare **tutti i modi possibili** in cui X e Y possono combinarsi per produrre lo stesso totale.

L’esempio mentale più semplice è quello dei dadi. Per sapere la probabilità che X+Y=7, devi contare tutte le coppie che danno 7: (1,6),(2,5),…,(6,1).
Questa è l’idea della convoluzione nel caso discreto: sommare le probabilità di tutte le decomposizioni possibili del totale. Il PDF generalizza questa idea in una formula.

Poi il PDF raccoglie alcuni risultati molto utili: la somma di due **Poisson indipendenti** è ancora Poisson; la somma di due **Binomiali indipendenti con la stessa probabilità p** è ancora Binomiale; la somma di due **Normali indipendenti** è ancora Normale; 

**la somma di due Uniformi(0,1) ha invece una densità triangolare.**

Il messaggio profondo è che alcune famiglie di distribuzioni sono “stabili” rispetto alla somma, e questo torna continuamente in probabilità e statistica.

---
## 3. Central Limit Theorem
Il **Teorema del Limite Centrale** dice che, se prendi tante variabili IID e le sommi o ne fai la media, il risultato tende a comportarsi come una **normale**, anche se le singole variabili di partenza non erano normali.
due versioni: per la **somma** e per la **media campionaria**.

Anche se i pezzi di partenza sono “strani”, la loro somma tende ad assumere una forma regolare, a campana. Il PDF lo mostra con l’esempio della somma di **100 variabili uniformi**: una singola uniforme non ha forma normale, ma la somma di molte uniformi sì, approssimativamente.
Questo non è un trucco speciale delle uniformi: succede molto in generale, purché la distribuzione di partenza abbia media e varianza finite.

Questa parte serve tantissimo perché giustifica perché in statistica compare così spesso la distribuzione normale. Non perché il mondo sia davvero gaussianissimo ovunque, ma perché **somme e medie di molte osservazioni** tendono a diventarlo.

Il PDF collega anche questa idea all’uso della normale per approssimare variabili discrete, spiegando la **continuity correction**: quando usi una distribuzione continua per approssimare una discreta, devi correggere leggermente gli estremi dell’intervallo.

Esempi applicativi.
Uno riguarda la somma di 10 dadi, approssimata con una normale; 
un altro riguarda il numero di prove necessarie per stimare una media con una certa precisione e confidenza. 
Questi esempi servono a mostrarti che il CLT non è solo teoria elegante: è uno strumento pratico per fare stime e probabilità quando il calcolo esatto sarebbe scomodo.

#### Central Limit Theorem (sum version)
Siano$(X_1, X_2, \dots, X_n)$ variabili casuali **IID**
(independent and identically distributed).
Se
$$
\mu = E[X_i]
\qquad \text{e} \qquad
\sigma^2 = \mathrm{Var}(X_i),
$$
allora, per $(n \to \infty)$,
$$
\sum_{i=1}^{n} X_i \approx \mathcal{N}(n\mu,\, n\sigma^2).
$$
Quindi la somma di \(n\) variabili IID tende ad essere approssimativamente normale,
con:
- **media**: $(n\mu)$
- **varianza**: $(n\sigma^2)$

#### Central Limit Theorem (average version)
Siano$(X_1, X_2, \dots, X_n)$ variabili casuali **IID**
(independent and identically distributed).
Se
$$
\mu = E[X_i]
\qquad \text{e} \qquad
\sigma^2 = \mathrm{Var}(X_i),
$$
allora, per $(n \to \infty)$,
$$
\frac{1}{n}​∑_{i=1}^n​Xi​≈N(\mu,\frac{\sigma^2}{n})
$$
Quindi la somma di \(n\) variabili IID tende ad essere approssimativamente normale,
con:
- **media**: $(\mu)$
- **varianza**: $(\frac{\sigma^2}{n})$

#### In una frase
- **Somma**: centro in $n\mu$, dispersione $n\sigma^2$
- **Media**: centro in $\mu$, dispersione $\frac{\sigma^2}{n}$

La **continuity correction** è una piccola correzione che usi quando approssimi una variabile **discreta** con una distribuzione **continua**, di solito la normale

Per esempio, se X può assumere solo valori interi e vuoi approssimare
$$
P(X≤25)
$$
con una normale Y, non scrivi P(Y≤25), ma
$$
P(Y<25.5)
$$
Perché la normale è continua, quindi per rappresentare bene tutti i valori interi fino a 25 devi prendere il confine tra 25 e 26, cioè **25.5**.
In pratica
- P(X≤k)≈P(Y<k+0.5)
- P(X≥k)≈P(Y>k−0.5)

---
## 4. Sampling: dal campione alla popolazione
hai una **popolazione grande** e non puoi osservare tutti, quindi prendi un **campione casuale**
L’esempio è la felicità in Bhutan: non puoi chiedere a tutti, quindi osservi solo un sottoinsieme casuale di persone.

Le osservazioni X1,…,Xn​ vengono trattate come IID provenienti da una distribuzione sottostante F, che ha una vera media μ e una vera varianza σ^2, ignote.

due stimatori: la **sample mean** $\bar X$ e la **sample variance** $S^2$. L’idea qui è semplice: visto che non conosci la media e la varianza vere della popolazione, usi le loro versioni campionarie come “migliori stime disponibili”.
Sono stime buone?
La risposta è sì, nel senso che sono **unbiased estimators**: se ripetessi il processo di campionamento tante volte, in media otterresti proprio i valori veri che stai cercando di stimare.

La **sample mean** è:
$$
\bar X = \frac1n \sum^n_{i=1}X_i
$$
- cioè fai la somma di tutte le osservazioni del campione e poi dividi per il numero totale di osservazioni n

La **sample variance**
$$
S^2=\frac1{n−1}\sum_{​i=1}^n​(Xi​−\bar X) \ con\ \bar X = \frac1n \sum^n_{i=1}X_i
$$
La varianza vera della popolazione dovrebbe misurare quanto i dati stanno lontani dalla **vera media** μ.
Però noi μ non la conosciamo, quindi nel campione usiamo Xˉ, cioè la **media del campione**.
se mettessi n al denominatore, la stima tenderebbe a venire **troppo piccola**: infatti Xˉ è stata calcolata dagli stessi dati, quindi in un certo senso “si adatta” al campione e riduce artificialmente le distanze quadratiche. Usare n−1 serve a correggere questo effetto.

## 5. Standard error
**formula approssimata** dello standard error della media campionaria
$$
SE(\bar X) \sim \sqrt{\frac{S^2}n} = \frac{S}{\sqrt{n}}
$$
dove:
- Xˉ è la **media campionaria**
- S^2 è la **varianza campionaria**
- S è la **deviazione standard campionaria**
- n è la **dimensione del campione**.
- 
Lo **standard error della media** misura **quanto la media campionaria Xˉ tende a variare da campione a campione**.  
Quindi non misura la dispersione dei dati singoli, ma la **dispersione della stima della media**.

In parole semplici:
- se lo standard error è **piccolo**, la tua media campionaria è **più precisa**
- se lo standard error è **grande**, la tua media campionaria è **più instabile**


Una volta che hai detto $\bar X$ è una buona stima di μ”, nasce una nuova domanda: **quanto può oscillare $\bar X$ da campione a campione?**
Qui entra lo **standard error**. Il PDF lo definisce come la deviazione standard della media campionaria: in parole povere, è una misura di quanto la tua stima della media sia instabile. Più è piccolo, più la tua media campionaria è precisa.

Il testo sottolinea che lo standard error è ciò che usi per riportare l’**incertezza** delle stime nei lavori scientifici, per esempio nelle barre d’errore.

Inoltre mostra l’approssimazione $\mathrm{Std}(\bar X)\approx \sqrt{S^2/n}$
Quindi, a parità di variabilità dei dati, aumentando nnn lo standard error diminuisce. Questo riflette un’idea intuitiva: con più osservazioni, la media campionaria diventa più stabile.

---
## 6. Bootstrapping
La parte finale del PDF introduce il **bootstrap**, che è una tecnica computazionale per studiare la distribuzione di una statistica quando non vogliamo o non possiamo derivarla a mano.

L’idea base del testo è molto pratica: se conoscessimo la distribuzione vera F, potremmo simulare tanti campioni nuovi e vedere come varia la statistica che ci interessa. Siccome però F non la conosciamo, la sostituiamo con la **migliore approssimazione disponibile**, cioè il campione osservato stesso.

Il procedimento è: 
- dal campione costruisci una stima della distribuzione sottostante;
- poi fai tanti **resampling** della stessa dimensione del campione originale;
- su ogni resample ricalcoli la statistica desiderata;
- infine guardi come questa statistica varia da resample a resample.
In questo modo ottieni una stima della distribuzione della statistica stessa.

Il PDF insiste sul fatto che i resampling devono avere la **stessa dimensione** del campione originale, altrimenti la variabilità della statistica non sarebbe comparabile.

Il senso intuitivo del bootstrap è: “non posso rifare davvero l’esperimento sul mondo, quindi lo rifaccio molte volte sul miglior surrogato del mondo che possiedo: il mio campione”.

Il PDF dice anche che il metodo ha solide basi teoriche, ma può degradare quando la distribuzione ha **code molto pesanti** o quando le osservazioni non sono **IID**.

## 7. p-value con bootstrap
L’ultimo esempio confronta la felicità media in **Bhutan** e **Nepal**. 
Supponi di osservare che il Nepal ha una media di felicità leggermente più alta, per esempio di 0.5 punti. 
La domanda scientifica è: **questa differenza è reale o potrebbe essere uscita solo per caso?**

Il PDF risponde con il linguaggio dell’**ipotesi nulla**: sotto la null hypothesis, non c’è alcuna differenza vera tra le due distribuzioni; la differenza osservata è dovuta al campionamento casuale.

Per calcolare il **p-value**, il PDF unisce i dati dei due gruppi in un unico campione, perché sotto l’ipotesi nulla entrambi i gruppi proverrebbero dalla stessa distribuzione.
Poi fa bootstrap da questa distribuzione comune, ricrea molte coppie di campioni della stessa dimensione degli originali, e ogni volta misura la differenza tra le medie.
Il p-value è la frazione di simulazioni in cui la differenza simulata è almeno estrema quanto quella osservata

Il vantaggio, sottolineato dal PDF, è che così **non devi assumere una forma parametrica**, per esempio non devi dire che la felicità segue una gaussiana.
Per questo il bootstrap viene presentato come uno strumento più flessibile del classico t-test in molti contesti moderni.

## Riassunto
- La **Beta** ti dice come rappresentare l’incertezza su una probabilità sconosciuta.  
- La **convoluzione** ti dice come ottenere la distribuzione di una somma di variabili casuali.  
- Il **CLT** spiega perché somme e medie di molte osservazioni diventano circa normali.  
- Il **sampling** ti insegna a stimare media e varianza della popolazione a partire da un campione.  
- Lo **standard error** misura l’incertezza della media campionaria.  
- Il **bootstrap** usa resampling dal campione per capire quanto una statistica sia variabile.  
- Il **bootstrap p-value** serve a capire se una differenza osservata tra gruppi è plausibile sotto l’ipotesi nulla.