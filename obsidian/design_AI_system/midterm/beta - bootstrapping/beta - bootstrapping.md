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

## 3. Central Limit Theorem