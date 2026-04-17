	## 1. Counting: l’idea di fondo

Il counting serve a rispondere a domande del tipo:
- quante possibilità ci sono?
- quante configurazioni diverse posso ottenere?
- quante scelte, sequenze, assegnazioni o casi esistono?

*quando un processo si può vedere come **una sequenza di passi**, spesso si **moltiplica***

*quando un risultato può arrivare da **casi alternativi**, spesso si **somma***

---
## 2. Product rule / Step rule

Se un esperimento ha più passi, e:
- il primo passo ha ***m*** possibilità
- il secondo ha ***n*** possibilità
- e così via
allora il numero totale di esiti è il **prodotto** delle possibilità.
Il PDF la chiama **Step Rule of Counting** o **Product Rule**.
*Ogni scelta del primo passo si combina con **tutte** le scelte del secondo.*

---
## 3. Counting con “or”: quando si somma
Se un risultato può avvenire in **modo A oppure modo B**, allora spesso si usa la somma. Però bisogna stare attenti a non contare due volte gli stessi casi. Il PDF distingue due situazioni.
### 3.2 Inclusion-Exclusion
Se A e B **si sovrappongono**, non puoi fare solo la somma, perché la parte comune verrebbe contata due volte.
Formula:
- ***∣A or B∣=∣A∣+∣B∣−∣A and B∣***
---
## 4. Overcounting and correcting
A volte il modo più semplice per contare è:
1. contare troppo
2. correggere dopo
spesso è più facile generare tutti i casi in modo “rilassato”, poi togliere i duplicati o dividere per il numero di volte in cui ogni caso è stato contato.
### Due modi di correggere
- **sottrazione**, se sai quanti casi “di troppo” hai contato
- **divisione**, se ogni oggetto è stato contato lo stesso numero di volte
---
## 5. Combinatorics: i “modelli standard”
Il PDF poi passa da counting “grezzo” a formule standard di combinatoria. In pratica ti dice:
- certi problemi ricorrono sempre; conviene riconoscerli subito e applicare la formula giusta.
I casi principali sono:
- permutazioni di oggetti distinti
- permutazioni con oggetti indistinguibili
- combinazioni
- bucketing con oggetti distinti
- bucketing con oggetti indistinguibili
- bucketing in contenitori di dimensione fissa
---
## 6. Permutations of distinct objects
Qui conta **l’ordine**.
Se hai n oggetti tutti diversi, il numero di ordinamenti possibili è: ***n!***
Per il primo posto hai n scelte, per il secondo n−1, poi n−2, ecc.

---
## 7. Permutations with indistinct objects
Qui l’ordine conta, **ma alcuni oggetti sono uguali**.
Se hai n oggetti in totale, con gruppi di indistinguibili di dimensione n1,n2,…,nr, allora: 
$$
\frac{n!}{n_1!n_2!...n_r!}
$$
n! tratta tutto come distinto e quindi **overcounta**.
Esempio:
$$
\frac{5!}{3!2!} = \frac{120}{12} = 10
$$
---
## 8. Combinations
Qui **l’ordine non conta**.
Scegli r oggetti da n oggetti distinti, senza rimpiazzo:
$$  
\begin{pmatrix}  n\\  r  \end{pmatrix}  = \frac{n!}{r! (n-r)!}
$$
Prima conteresti gli ordinamenti, ma poi ti accorgi che ogni gruppo di r elementi è stato contato r! volte, una per ogni ordine interno.
### Differenza chiave con permutazioni
- **permutazione**: ABC e CBA sono diversi
- **combinazione**: ABC e CBA sono la stessa scelta

---
## 9. Bucketing with distinct objects
Qui assegni oggetti distinti a contenitori distinti.
Se hai:
- n oggetti distinti
- r bucket distinti
e ogni oggetto può andare in qualunque bucket, allora:
$$
r^n
$$
### Quando usarla
Quando stai facendo **assegnazioni indipendenti**:
- studenti a gruppi
- file a cartelle
- palline numerate in scatole etichettate
---
## 10. Bucketing with indistinct objects: stars and bars
Qui gli oggetti sono indistinguibili.
In quanti modi posso distribuire n oggetti uguali in r contenitori distinti?
$$
\begin{pmatrix}  
n + r -1\\  
n 
\end{pmatrix}
$$
Equivalente
$$
\begin{pmatrix}  
n + r -1\\  
r -1
\end{pmatrix}
$$
### Esempio
10 milioni da investire in 4 aziende, in blocchi da 1 milione:
$$
\begin{pmatrix}  
n + r -1\\  
n
\end{pmatrix}
= 
\begin{pmatrix}  
10 + 4 -1\\  
10
\end{pmatrix}
= 
\begin{pmatrix}  
13\\  
10
\end{pmatrix}
=  
\frac{13!}{10!(13 - 10)!} = 286
$$
Equivalente a 
$$
\begin{pmatrix}  
n + r -1\\  
r -1
\end{pmatrix}
= 
\begin{pmatrix}  
10 + 4 -1\\  
3
\end{pmatrix}
=
\begin{pmatrix}  
13\\  
3
\end{pmatrix}
= \frac{13!}{3!(13 - 3)!} = 286
$$
---
## 11. Fixed-sized containers / Multinomial coefficient
Qui hai oggetti distinti, ma i gruppi devono avere dimensioni già fissate.
Se devi dividere n oggetti distinti in r gruppi di dimensione:
- n1, n2, ..., nr
- n1 + n2 + ... + nr = n
il numero di modi è:
$$
\frac{n!}{n_1!n_2!\dots n_r!}
$$
Questo è il **coefficiente multinomiale**.
### Esempio del PDF
13 server distinti da distribuire in 3 datacenter con:
- 6 posti
- 4 posti
- 3 posti
Allora 
$$
\frac{13!}{6!4!3!} = 60060
$$
Puoi vederlo così:
- scegli i 6 del gruppo A
- poi i 4 del gruppo B tra i rimanenti
- gli ultimi 3 vanno al gruppo C

oppure usi direttamente la formula multinomiale.

---
## 12. Come riconoscere quale formula usare
## A. L’ordine conta?
- sì → pensa a **permutazioni**
- no → pensa a **combinazioni**
## B. Gli oggetti sono tutti distinti?
- sì → formula standard
- no → devi correggere per gli indistinguibili
## C. Stai facendo una sequenza di scelte?
- sì → spesso **product rule**
## D. Stai unendo casi alternativi?
- sì → **sum rule** o **inclusion-exclusion**
## E. Stai distribuendo oggetti in contenitori?
- oggetti distinti → $r^n$
- oggetti uguali → stars and bars
- gruppi con taglia fissata → multinomiale

---
## 13. Gli errori più comuni
Gli errori classici in questa parte sono:
### 1. Confondere permutazioni e combinazioni
Esempio:
- codice PIN → ordine conta
- scegliere 3 persone → ordine non conta
### 2. Sommare quando in realtà bisogna moltiplicare
“prima questo, poi quello” quasi sempre significa prodotto.
### 3. Dimenticare le sovrapposizioni
Nei problemi con “A oppure B”, controlla sempre se A e B si intersecano.
### 4. Trattare oggetti uguali come diversi
Questo porta a overcounting.
### 5. Non distinguere tra:
- oggetti distinti / indistinguibili
- contenitori distinti / indistinguibili
- ordine sì / ordine no

---
# 14. Mini-riassunto formula-sheet
  
Le formule essenziali di questa parte sono:  
#### Product rule  
$$  
m \cdot n  
$$ 
#### Mutually exclusive  
$$  
|A \cup B| = |A| + |B|  
$$  
#### Inclusion-exclusion  
$$  
|A \cup B| = |A| + |B| - |A \cap B|  
$$  
#### Permutazioni distinte  
$$  
n!  
$$  
#### Permutazioni con ripetizioni  
$$  
\frac{n!}{n_1!n_2!\cdots n_r!}  
$$  
#### Combinazioni  
$$  
{n \choose r} = \frac{n!}{r!(n-r)!}  
$$
#### Bucketing distinti  
$$  
r^n  
$$
#### Stars and bars  
$$  
{n+r-1 \choose n}  
$$
#### Multinomiale  
$$  
\frac{n!}{n_1!n_2!\cdots n_r!}  
$$