## 1. Law of Total Probability: idea intuitiva
La legge della probabilità totale serve quando vuoi calcolare P(E), ma ti viene più facile pensare a E separando il mondo in casi diversi.

Il PDF parte dal caso più semplice: un evento F divide lo spazio campionario in due parti:
- F
- F^c cioè “non F”

Queste due parti sono:
- **mutuamente esclusive**
- e insieme coprono tutto lo spazio campionario.

Quindi ogni volta che succede E, deve succedere in uno di questi due modi:
- E insieme a F
- oppure E insieme a F^c 

Perciò:
$$
P(E)=P(E\ and\ F)+P(E\ and\ F^c)
$$
e usando la chain rule il PDF scrive:
$$
P(E)=P(E \mid F)P(F)+P(E \mid F^c)P(F^c)
$$
Questa è la **Law of Total Probability** nella forma a due casi.

---
## 2. Intuizione vera della formula
Questa formula dice una cosa molto naturale:
la probabilità totale di E è una media pesata della probabilità di E nei vari contesti possibili.
Cioè:
- quanto è probabile E se siamo nel caso F?
- quanto è probabile E se siamo nel caso opposto?
- quanto sono probabili questi due casi?
Poi combini tutto.
Quindi la law of total probability è, in sostanza, una **scomposizione per casi**.

---
## 3. Versione generale
non devi avere per forza solo due casi. Se puoi dividere lo spazio campionario in eventi
$$
B_1,B_2,\dots,B_n
$$
che sono:
- mutuamente esclusivi
- ed esaustivi, cioè coprono tutto lo spazio
allora
$$  
P(E)=\sum_{i=1}^{n} P(E \mid B_i)\,P(B_i)  
$$
Questa è la forma generale della legge della probabilità totale.
#### Significato
Per ogni background event $B_i:$
- guardi quanto è probabile E dentro $B_i$
- lo pesi con quanto è probabile BiB_iBi​
e poi sommi tutto.

---
## 4. Esempio intuitivo
Immagina di voler sapere la probabilità che una persona risulti positiva a un test.
Puoi dividere la popolazione in gruppi:
- alto rischio
- medio rischio
- basso rischio
Il PDF fa proprio un esempio di questo tipo: la probabilità totale di test positivo si ottiene sommando il contributo di ciascun gruppo, cioè
$$
P(E)=P(E∣B_1​)P(B_1​)+P(E∣B_2​)P(B_2​)+P(E∣B_3​)P(B_3​)
$$
dove E è “test positivo” e i $B_i$​ sono i gruppi di rischio.

**se un problema è difficile globalmente, spesso è facile localmente, caso per caso.**

---
## 5. Bayes’ Theorem: a cosa serve
Bayes entra in gioco quando non vuoi solo sapere la probabilità di un’evidenza, ma vuoi fare il contrario:
**data un’evidenza osservata, qual è la probabilità della causa o dello stato nascosto?**
*Bayes ti permette di “invertire” una probabilità condizionata.*
Passi da:
$$
P(E \mid B)
$$
a:
$$
P(B \mid E)
$$
cioè da “probabilità dell’evidenza dato lo stato” a “probabilità dello stato data l’evidenza”.

---
## 6. Formula di Bayes
Il PDF deriva Bayes dalla conditional probability e dalla chain rule, ottenendo:
$$
P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}
$$
Questa è la forma classica di Bayes.
#### Come leggerla 
- $P(B∣E)$: probabilità aggiornata della tua credenza dopo aver visto l’evidenza
- $P(E \mid B)$: quanto l’evidenza è compatibile con l’ipotesi
- $P(B)$: probabilità iniziale dell’ipotesi
- $P(E)$: probabilità totale dell’evidenza

---
## 7. L’interpretazione dei termini
Il PDF dà anche i nomi standard:
- $P(B∣E)$ = **posterior**
- $P(B)$ = **prior**
- $P(E \mid B)$ = spesso chiamata **likelihood**
- $P(E)$ = **normalization constant**
La lettura intuitiva è:
- posterior = likelihood × prior / evidence
cioè:
- nuova credenza = compatibilità dell’evidenza con l’ipotesi × credenza iniziale / probabilità totale dell’evidenza

---
## 8. Cosa fa davvero Bayes
Bayes è utile quando hai:
- una cosa nascosta che vuoi sapere
- una cosa osservabile che dipende da quella cosa nascosta
E vuoi passare dall’osservabile al nascosto.

Il PDF fa esempi molto chiari:
- malattia → risultato del test
- abilità dello studente → risposte date
- posizione del telefono → segnale osservato
In tutti questi casi, spesso è facile sapere:
$$
P(evidenza∣stato)
$$
ma quello che ti interessa davvero è
$$
P(stato∣evidenza)
$$e questo è esattamente ciò che dà Bayes.

---
## 9. Differenza fondamentale: $P(E \mid B)$ non è $P(B \mid E)$
Questo è il punto in cui quasi tutti si confondono all’inizio.
- $P(E \mid B)$: se l’ipotesi B è vera, quanto spesso vedo l’evidenza?
- $P(B \mid E)$: dato che ho visto l’evidenza, quanto è probabile che B sia vera?
Sono due quantità diverse.
E Bayes esiste proprio perché **non puoi scambiarle**.

---
## 10. Bayes + Law of Total Probability
Nella formula classica di Bayes compare $P(E)$, che a volte non conosci direttamente.
Il PDF mostra allora la forma “Bayes + total probability”:
$$
P(B \mid E)=\frac{P(E \mid B)\,P(B)}{P(E \mid B)\,P(B)+P(E \mid B^c)\,P(B^c)}
$$Questa viene fuori sostituendo nel denominatore la law of total probability nel caso a due eventi.
Più in generale, se hai molti casi $B_1,\dots,B_n$ allora:
$$
P(B_i \mid E)=\frac{P(E \mid B_i)\,P(B_i)}{\sum_{j=1}^{n} P(E \mid B_j)\,P(B_j)}
$$Anche questa forma è esplicitamente discussa nel PDF nella parte “Bayes with the General Law of Total Probability”

---
## 11. Esempio classico del PDF: test medico
Il PDF fa un esempio di test diagnostico con questi numeri:
- probabilità naturale della malattia: 0.13
- probabilità di test positivo dato malattia: 0.92
- probabilità di test positivo dato assenza di malattia: 0.10
vuoi sapere 
$$
P(malattia \mid test \ positivo)
$$
Applicando Bayes
$$
P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}
$$
io, non avendo ovviamente P(E) passo a Bayes + total probability
$$
P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E \mid B)P(B) + P(E \mid B^c)P(B^c)}
$$
quindi
$$
\begin{matrix}
	P(I \mid E) = \frac{P(E \mid I)P(I)}{P(E \mid I)P(I) + P(E \mid I^c)P(I^c)} \\
	P(I \mid E) = \frac{(0,92)(0.13)}{(0.92)(0.13) + (0.10)(1-0.13)}\\
	= 0.5789
\end{matrix}
$$---
## 12. Perché questo risultato sorprende

Se il test è “molto buono” e il risultato è positivo, allora la persona quasi certamente ha la malattia

Ma Bayes mostra che non basta conoscere la qualità del test. Devi considerare anche quanto la malattia è frequente nella popolazione, cioè il **prior**.

Se la malattia è relativamente rara, anche un piccolo tasso di falsi positivi può pesare tanto.

Questa è una lezione profondissima:  
**l’evidenza conta, ma conta anche il contesto di base.**

---
## 13. Intuizione con le frequenze naturali
Il PDF dà anche un’intuizione molto bella usando una popolazione immaginaria di 1000 persone. In quel ragionamento:
- alcune persone hanno davvero la malattia e testano positivo
- altre non ce l’hanno ma testano comunque positivo
Poi guardi solo il gruppo dei positivi e ti chiedi:  
tra questi positivi, quanti sono veramente malati?

Questo rende Bayes molto più intuitivo, perché smetti di vedere solo formule e inizi a vedere **conteggi reali di persone**.

Ed è esattamente questo il significato di $P(B \mid E)$):  
tra quelli che mostrano l’evidenza E, qual è la frazione che ha davvero la causa B?

---
## 14. Unknown normalization constant
Il PDF conclude con un problema pratico: e se P(E) non è noto?

Una strategia è calcolarlo con la law of total probability.

Un’altra idea mostrata nel PDF è che, se confronti due ipotesi concorrenti, la costante P(E) si può cancellare nei rapporti. 
Per esempio, confrontando:
$$
\frac{P(B∣E)}{P(B^c∣E)}​
$$
e sostituendo Bayes sopra e sotto, P(E) sparisce.
Questo è utile perché a volte non ti serve il valore assoluto del posterior, ma solo sapere quale ipotesi è più plausibile e di quanto.

---
## 15. Relazione tra Total Probability e Bayes
Questi due strumenti sono strettamente collegati.
La **Law of Total Probability** serve a calcolare la probabilità dell’evidenza:
$$
P(E)
$$
Bayes poi usa proprio quella quantità per normalizzare l’aggiornamento:
$$
P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}
$$Quindi puoi pensarla così:

- **Total Probability**: “quanto è probabile osservare questa evidenza in generale?”
- **Bayes**: “ora che ho osservato questa evidenza, come aggiorno la mia credenza sull’ipotesi?”

---
## 16. L’intuizione finale da portarti a casa
La legge della probabilità totale dice:
- per capire un evento, scomponilo in casi.
Bayes dice:
- se osservi un risultato, puoi risalire a quanto diventano credibili le cause possibili.
Insieme, ti permettono di passare da un ragionamento “statico” a un ragionamento **inferenziale**. Ed è proprio per questo che sono così centrali in probabilità, statistica e AI.

--- 
## 17. Le formule da sapere davvero

Quelle essenziali di questa parte sono:
$$
P(E) = P(E \mid F)P(F) + P(E \mid F^c)P(F^c)
$$
$$
P(E) = \sum_{i=1}^{n} P(E \mid B_i)P(B_i)
$$
$$
P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}
$$
$$
P(B \mid E) =
\frac{P(E \mid B)P(B)}
{P(E \mid B)P(B) + P(E \mid B^c)P(B^c)}
$$
e, nel caso generale,
$$
P(B_i \mid E) =
\frac{P(E \mid B_i)P(B_i)}
{\sum_{j=1}^{n} P(E \mid B_j)P(B_j)}
$$
---
