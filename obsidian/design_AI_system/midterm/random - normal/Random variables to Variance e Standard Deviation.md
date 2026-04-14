## 1. Random variables
Una **random variable** è una variabile che assume un valore in modo probabilistico. Il PDF la presenta come un oggetto fondamentale della probabilità: un po’ come una variabile in programmazione, ma il suo valore non è fissato in anticipo. Per esempio, se lanci 3 monete e chiami Y il **numero di teste**, allora Y può valere 0,1,2,3. Quindi la random variable non è il singolo esito, ma una funzione che associa a ogni esito un numero.
### Differenza tra **evento** e **random variable**.
- La **random variable** è l’oggetto, per esempio Y= “numero di teste in 3 lanci”.
- Un evento è una condizione sul suo valore, per esempio $Y=1$, oppure $Y<2$, oppure$X>Y$.  
    Quindi la probabilità si assegna agli **eventi**, non direttamente alla variabile in astratto. Quando scrivi $P(Y=1)$, stai parlando dell’evento “Y assume valore 1”.
### Due grandi famiglie
- **discrete random variables**, che assumono valori discreti, tipicamente interi;
- **continuous random variables**, che possono assumere valori reali in un intervallo.  
    Nei tuoi due PDF, la parte iniziale sviluppa soprattutto l’intuizione con le variabili **discrete**, e la normale è invece il grande esempio di variabile **continua**.

Le proprietà principali che il PDF associa a una random variable sono:
- **supporto** o insieme dei valori possibili;
- **distribution function**: PMF se è discreta, PDF se è continua;
- **expectation**: A weighted average
- **variance**: A measure of spread
- **standard deviation**: The square root of variance
- **mode**: The most likely value of the random variable

---
## 2. Probability Mass Function (PMF)
Per una variabile discreta, la domanda fondamentale è: **quanto è probabile ogni valore possibile?** La risposta è la **probability mass function**, cioè la PMF.
Formalmente, la PMF assegna a ogni valore x la probabilità P(X=x). In altre parole, ti dice quanta “massa di probabilità” cade su ciascun valore possibile.

Un esempio semplice del PDF è il lancio di un dado. Se X è il valore del dado, allora
$$
	P(X = x) = \frac16\ per\ x = 1,\dots,6.
$$
quindi tutti i valori hanno la stessa probabilità.
Un esempio più interessante è la somma di due dadi: se Y è la somma, i valori centrali come 7 sono più probabili dei valori estremi come 2 o 12, perché ci sono più modi per ottenerli. Quindi la PMF non è uniforme

**le probabilità della PMF devono sommare a 1:**
$$
\sum_k P(X = k) = 1.
$$
I valori possibili della random varible coprono tutto lo spazio dei casi possibili, e due valori diversi non possono accadere contemporaneamente. Quindi la probabilità totale deve essere tutta distribuita tra i valori possibili.

C’è anche un’idea molto utile: una PMF può essere approssimata da dati reali. Se raccogli molti campioni di una variabile discreta e fai un istogramma normalizzato, le frequenze relative approssimano la PMF. Nel PDF questo viene mostrato con la somma di due dadi simulata 10.000 volte. Quindi la PMF può essere vista sia come oggetto teorico sia come limite di frequenze osservate.

---
## 3. Expectation
L’**expectation** è il riassunto più importante di una random variable. Il PDF la definisce come la **media pesata** dei valori possibili, dove ogni valore è pesato con la sua probabilità:
$$
E [X] = \sum_k xP(X=x)
$$
Questa formula non dice quale valore vedrai in un singolo esperimento; dice piuttosto qual è il valore medio che osserveresti se ripetessi l’esperimento moltissime volte

Per esempio, se X è la somma di due dadi, il PDF mostra che
$$
E[X] = 7
$$
Questo non significa che esca sempre 7. Significa che 7 è il “centro medio” della distribuzione. È il valore attorno a cui si bilanciano tutti gli esiti, tenendo conto delle loro probabilità.

Una proprietà cruciale è la **linearità dell’aspettativa**:
$$
E[aX + b] = aE[X]+b
$$
e ancora più importante
$$
E[X + Y] = E[X]+E[Y]
$$
Questa proprietà vale anche se X e Y **non sono indipendenti**. È una delle regole più potenti di tutta la probabilità, perché permette di calcolare la media di somme complicate senza dover trovare tutta la distribuzione della somma.

Il testo introduce anche LOTUS, la **Law of the Unconscious Statistician**:
$$
E[g(X)] = \sum_x g(x)P(X=x)
$$
Serve quando vuoi il valore atteso di una funzione della variabile, per esempio $E[X^2]$. Ti basta applicare la funzione ai valori e poi fare la stessa media pesata. Questa formula diventa fondamentale subito dopo, quando si passa alla varianza.

---
## 4. Variance e Standard Deviation
Se l’aspettativa ti dice il **centro** della distribuzione, la **varianza** ti dice quanto i valori sono **sparsi** attorno a quel centro. Il PDF la definisce come:
$$
Var(X) = E [(X - μ)^2]
$$
dove $μ = E[X].$ Quindi: prendi la distanza dalla media, la elevi al quadrato, e poi fai la media pesata di queste distanze quadratiche.

L’idea intuitiva è semplice:
- se i valori sono molto vicini alla media, la varianza è piccola;
- se i valori sono molto dispersi, la varianza è grande.  
    Nel PDF questa intuizione viene spiegata anche con l’esempio di diversi gruppi di correttori: due gruppi possono avere la stessa media, ma uno può essere molto più “sparso” dell’altro. La varianza serve proprio a distinguere casi del genere.

Il PDF usa anche una formula equivalente, spesso più comoda da calcolare:
$$
Var(X) = E[X^2] - E[X]^2
$$
Questa forma è importantissima negli esercizi: prima trovi $E[X]$, poi trovi $E[X^2]$ usando LOTUS, e infine fai la differenza.

La **standard deviation** è semplicemente la radice quadrata della varianza. Serve perché la varianza è espressa in unità al quadrato, mentre la deviazione standard torna nelle unità originali della variabile. Per questo è più interpretabile. Se la variabile è misurata in punti, la deviazione standard sarà ancora in punti, non in punti quadrati.