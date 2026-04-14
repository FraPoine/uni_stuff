## 1. Prima idea: la probabilità parla sempre di un esperimento

Nel PDF la probabilità non viene mai trattata “nel vuoto”. Prima devi fissare il contesto, cioè l’**esperimento**. Per esempio:
- lanciare una moneta
- lanciare due monete
- tirare un dado
- contare quante email ricevi in un giorno
Questo è importante perché una probabilità ha senso solo rispetto a un certo insieme di risultati possibili.
---
## 2. Sample space: l’insieme di tutti i risultati possibili
Lo **sample space**, indicato con **S**, è l’insieme di tutti i possibili esiti dell’esperimento. Il PDF dà esempi molto semplici:
- moneta: $S=\{Heads,Tails\}$
- due lanci di moneta: $S=\{(H,H),(H,T),(T,H),(T,T)\}$
- dado a 6 facce: $S=\{1,2,3,4,5,6\}$
*Lo spazio campionario è il “mondo completo” dei risultati ammessi.*
Se sbagli a definire **S**, rischi di sbagliare tutto il problema.

---
## 3. Event: il sottoinsieme che ci interessa
Un **evento**, indicato con **E**, è un sottoinsieme di **S**. In simboli:
$$
E \subseteq S
$$
Questo vuol dire che un evento non è altro che una collezione di esiti che per noi hanno un certo significato. 
Esempi dal PDF:
- “esce testa” su una moneta: $E=\{Heads\}$
- “almeno una testa” su due lanci: $E = \{(H,H),(H,T),(T,H)\}$
- “il dado fa 3 o meno”: $E = \{1,2,3\}$
Lo spazio campionario è tutto ciò che può accadere.  
L’evento è la parte di quello spazio che stai osservando.

---
## 4. Definizione di probabilità: idea frequentista
Il PDF dà una definizione formale di probabilità basata sulle frequenze. In pratica:
$$
P(E)=\lim_{n \to \infty}\frac{\operatorname{count}(E)}{n}
$$
se ripeti l’esperimento tantissime volte, la frazione di volte in cui succede l’evento **E** tende alla sua vera probabilità.

*La probabilità di un evento è la sua **frequenza relativa nel lungo periodo**.*

---
## 5. Probabilità come misura di incertezza
*la probabilità non va vista solo come “caso naturale”, ma anche come **linguaggio per esprimere incertezza**.*

Questa idea è fondamentale per machine learning e AI:
- la probabilità non è solo “giochi d’azzardo”
- è uno strumento per ragionare sotto incertezza
---
## 6. Da dove arrivano le probabilità
Il PDF dice che in pratica le probabilità possono arrivare da fonti diverse:
- da calcoli matematici
- da dati osservati
- da simulazioni
- da credenze iniziali o assunzioni
Questa osservazione è molto utile perché ti fa capire che non sempre una probabilità si ottiene nello stesso modo.

---
## 7. Probabilità e percentuali
Il PDF ricorda anche una cosa banale ma importante: una probabilità è un numero tra 0 e 1, mentre la percentuale è la stessa cosa moltiplicata per 100. Quindi:
- probabilità 0.32
- percentuale 32%
---
## 8. Gli assiomi della probabilità
### Axioma 1
$$
0 ≤ P(E) ≤ 1
$$
Una probabilità non può essere negativa e non può superare 1.

### Axioma 2
$$
P(S) = 1
$$
Lo spazio campionario completo ha probabilità 1, perché quando fai l’esperimento uno degli esiti possibili deve pur uscire.

### Axioma 3 
se due eventi sono mutualmente esclusivi 
$$
P(E \ or \ F) = P(E) + P(F)
$$
cioè se non possono accadere insieme, la probabilità dell’“oppure” è la somma.

#### Intuizione
Questi tre assiomi sono le regole minime da cui si costruisce tutta la teoria della probabilità.

---
## 9. Due identità molto importanti
Dal PDF seguono subito alcune conseguenze utili.
### Complemento
$$
P(E^c) = 1 - P(E)
$$
dove $E^c$ significa “evento opposto”, cioè “E non accade”.

Questo è utilissimo negli esercizi, perché a volte è molto più facile calcolare la probabilità del contrario.

### Monotonicità
se $E \subseteq F$
$$
P(E) ≤ P(F)
$$
Ha senso: se E è contenuto in F, allora F è un evento almeno grande quanto E.

---
## 10. Quando gli esiti sono equally likely
se tutti gli esiti dello spazio campionario sono **equiprobabili**, allora la probabilità si può calcolare contando
$$
P(E) = \frac{|E|}{|S|}
$$
dove:
- $∣E∣$= numero di esiti favorevoli
- $∣S∣$= numero di esiti possibili totali
#### Questa formula vale solo in un caso speciale
Vale solo quando gli esiti di **S** hanno davvero tutti la stessa probabilità.
Questo è uno degli **errori più frequenti**negli esercizi: usare $∣E∣/∣S∣$ anche quando gli esiti non sono equiprobabili.

---
## 11. Esempio classico: somma di due dadi uguale a 7

Il PDF usa il caso dei due dadi. Se definisci bene lo spazio campionario come tutte le coppie ordinate:
$$
(1,1),(1,2),\dots,(6,6)
$$allora gli esiti possibili sono 36 e sono tutti equiprobabili. Gli esiti favorevoli alla somma 7 sono 6:
$$
(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)
$$
Quindi:
$$
P(E) = \frac{|E|}{|S|} = P(somma = 7) = \frac6{36} = \frac16
$$
Il PDF sottolinea anche una soluzione sbagliata: prendere come sample space le somme da 2 a 12. Quello sarebbe un errore, perché le somme non sono tutte ugualmente probabili. Il 7 esce molto più spesso del 2.

**Non basta scegliere uno spazio campionario “comodo”.**  
**Devi sceglierne uno in cui il tuo metodo di calcolo sia valido.**

---
## 12. La vera abilità in questa parte
Secondo me, in questa sezione devi imparare soprattutto a fare tre cose.
1. **definire bene il sample space**.  
2. **definire l’evento come sottoinsieme del sample space**.  
3. capire **se puoi usare la formula $∣E∣/∣S∣$ oppure no.

---
## 13. Errori tipici
Gli errori più comuni in questa parte sono questi.

Il primo è confondere un evento con un singolo esito. Un evento può anche contenere molti esiti.

Il secondo è definire male lo spazio campionario. Se scegli un sample space non adatto, poi tutte le probabilità escono distorte.

Il terzo è usare la formula degli esiti equiprobabili quando in realtà gli esiti non sono equiprobabili.

Il quarto è dimenticare il complemento, che spesso è il modo più semplice per chiudere un esercizio. Tutti questi punti sono impliciti o espliciti negli esempi iniziali del PDF.

---
## 14. Formula sheet minimo da sapere

Per questa parte, ricorderei soprattutto queste formule:
#### Evento
$$
E \subseteq S
$$
#### Probabilità
$$
P(E) = \lim_{n \to \infty} \frac{\text{count}(E)}{n}
$$
#### Axioma 1 della probabilità
$$
0 \leq P(E) \leq 1
$$
#### Axioma 2 della probabilità
$$
P(S) = 1
$$
#### Complemento
$$
P(E^c) = 1 - P(E)
$$
#### Equally likely
*Se gli esiti sono equiprobabili:*
$$
P(E) = \frac{|E|}{|S|}
$$
