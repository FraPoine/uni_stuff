## Idea generale del PDF
Il problema centrale è:
- se lancio una moneta n volte, qual è la probabilità di ottenere esattamente k teste?
Il PDF parte da esempi semplici e poi arriva alla formula generale. Alla fine mostra anche come calcolare la probabilità di ottenere **più di  k teste**.

## 1. Setup del problema
Il PDF considera:
- n = numero di lanci
- p = probabilità che un singolo lancio dia testa
- 1−p= probabilità che un singolo lancio dia croce
Non assume per forza una moneta equa: se la moneta è equa, allora p=0.5, ma la trattazione resta generale.

---
## 2. Warm-up: casi semplici
Prima di arrivare a “esattamente k teste”, il PDF fa alcuni casi facili.
#### Tutte teste
Se fai n lanci e vuoi che escano tutte teste, allora ogni lancio deve dare testa, quindi:
$$
P(tutte \ teste) = p^n
$$
Per esempio, con n=10 e p=0.6:
$$
P(10 \ teste) = 0.6^{10}
$$
#### Tutte croci
allo stesso modo 
$$
P(tutte \ croci) = (1-p)^n
$$Perché ogni lancio deve dare croce.
#### Prima k teste, poi n−k croci
Se imponi un ordine preciso, tipo:
- prime k posizioni = testa
- restanti n−k = croce
allora la probabilità è:
$$
p^k(1-p)^{n-k}
$$Perché moltiplichi k fattori p e n−k fattori 1−p

----
## 3. Il punto cruciale: “esattamente k teste”
La domanda **“esattamente k teste”** non significa:
- le prime k sono teste e le altre no
ma significa
- in tutto ci sono k teste, in qualunque posizione
Quindi non c’è **una sola sequenza**, ma molte. Per esempio, con n=10 e k=4, vanno bene tutte le sequenze con 4 H e 6 T, in qualsiasi ordine.

---
## 4. Quante sequenze ci sono?
il problema diventa di **counting/combinatorics**:
quanti modi ci sono di disporre k teste e n−k croci?
la risposta è:
$$  
\begin{pmatrix}  
n\\  
k  
\end{pmatrix}  = \frac{n!}{k! (n-k)!}
$$
per esempio con n = 10 e k = 4:
$$  
\begin{pmatrix}  
10\\  
4  
\end{pmatrix}  = \frac{10!}{4! (10-4)!}
= 210
$$cioè ci sono 210 sequenze diverse con 4 teste e 6 croci.

È come scegliere **quali 4 posizioni** tra le 10 saranno occupate dalle teste.

---
## 5. Probabilità di una singola sequenza con k teste
Ora il PDF prende una sequenza specifica, tipo:
$$
T,H,T,T,H,T,T,H,H,T
$$
Questa sequenza ha:
- 4 teste
- 6 croci
Dato che i lanci sono indipendenti, la probabilità di quella precisa sequenza è:
$$
p^k(1-p)^{n-k} 
$$
che in questo caso è:
$$
p^4(1-p)^6
$$
Punto importante
Tutte le sequenze con lo stesso numero di teste hanno la **stessa probabilità**, perché contengono lo stesso numero di fattori p e 1−p.

---
## 6. Formula finale: probabilità di esattamente k teste
A questo punto il PDF combina le due idee:
- ci sono $\begin{pmatrix} n \\ k \end{pmatrix}$ sequenze valide
- ciascuna ha probabilità $p^k(1-p)^{n-k}$
e siccome questi casi sono mutualmente esclusivi, si possono sommare. Otteniamo:
$$
P(exactly \ k \ heads) = 
\begin{pmatrix}
n \\ k
\end{pmatrix}
p^k(1-p)^{n-k}
$$
**formula centrale**

---
# 7. Esempio numerico del PDF
Il PDF fa l’esempio con:
- n=10
- k=4
- p=0.6
Allora:
$$
P(exactly \ 4 \ heads) = 
\begin{pmatrix}
10 \\ 4
\end{pmatrix}
0.6^4(1-0.6)^{10-4} = 
0.111
$$
Quindi la probabilità di ottenere esattamente 4 teste in 10 lanci, con probabilità di testa 0.6 a ogni lancio, è circa **0.111**, cioè **11.1%**

---
## 8. “More than k heads”
Nell’ultima parte, il PDF passa alla probabilità di ottenere **più di k** teste.
Questo significa sommare tutti i casi:
$$
k+1,k+2,\dots,n
$$
perciò;
$$
P(\text{more than } k \text{ heads})=\sum_{i=k+1}^{n} P(\text{exactly } i \text{ heads})
$$
e sostituendo la formula di prima:
$$
P(\text{more than } k \text{ heads})=\sum_{i=k+1}^{n} 
\begin{pmatrix}
n \\ i
\end{pmatrix}
p^i(1-p)^{n-i}
$$
#### Intuizione
“Più di k” è un evento composto da tanti casi separati:
- esattamente k+1
- esattamente k+2
- …
- esattamente n
e questi casi non possono verificarsi insieme, quindi le probabilità si sommano.

---
## 9. Perché questa parte è importante
Il PDF sottolinea che questa derivazione va molto oltre le monete. Lo stesso schema vale per situazioni come:
- numero di votanti che scelgono un candidato
- numero di persone che contraggono una malattia
- numero di utenti che cliccano un annuncio
cioè tutti i casi in cui hai:
- n prove
- indipendenti
- ciascuna con due esiti
- probabilità di “successo” uguale a p
Questa è esattamente la struttura della **binomiale**.

---
## 10. Cosa devi capire davvero
Il cuore della sezione è questo passaggio logico:
#### Caso 1: una sequenza specifica
Per una sequenza fissata con k teste:
$$
p^k(1-p)^{n-k}
$$
#### Caso 2: qualunque sequenza con k teste
ci sono
$$
\begin{pmatrix}
n \\ k
\end{pmatrix}
$$
sequenze di quel tipo.
#### Qundi
$$
P(exactly \ k \ heads) = 
\begin{pmatrix}
n \\ k
\end{pmatrix}
p^k(1-p)^{n-k}
$$Questo è davvero tutto il meccanismo.

---
## 12. Riassunto finale super compatto
una sequenza specifica con k teste ha probabilità
$$
p^k(1-p)^{n-k}
$$
il numero di sequenze con esattamente k teste è
$$
\begin{pmatrix}
n \\ k
\end{pmatrix}
$$
quindi
$$
P(exactly \ k \ heads) = 
\begin{pmatrix}
n \\ k
\end{pmatrix}
p^k(1-p)^{n-k}
$$
e
$$
P(\text{more than } k \text{ heads})=\sum_{i=k+1}^{n} P(\text{exactly } i \text{ heads})
$$
Tutto questo è il contenuto matematico centrale della sezione “Many Coin Flips”.