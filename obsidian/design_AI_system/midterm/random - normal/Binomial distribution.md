Nel PDF su random variables compare la costruzione classica con molti lanci di moneta: hai n prove indipendenti, ciascuna con probabilità p di successo, e vuoi il numero di successi. Questo è il cuore della **binomial distribution**.

La domanda base è: qual è la probabilità di ottenere **esattamente k successi** in n prove? Il PDF la costruisce in due pezzi.

**Primo pezzo:** una sequenza specifica con k successi e n−k insuccessi ha probabilità
$$
p^k(1−p)^{n−k}
$$perché le prove sono indipendenti.

**Secondo pezzo:** bisogna contare **quante** sequenze diverse hanno esattamente kkk successi. Questo numero è
$$
\begin{pmatrix} n \\ k \end{pmatrix}
$$
quindi la probabilità finale
$$
P(X = k) = \begin{pmatrix} n \\ k \end{pmatrix} p^k(1−p)^{n−k}
$$
Questa è la formula della binomiale. Il PDF la deriva proprio contando le possibili disposizioni dei successi tra le nnn prove.

L’intuizione è molto importante:
- $p^k(1−p)^{n−k}=$ probabilità di **una particolare configurazione**;
- $\begin{pmatrix} n \\ k \end{pmatrix} =$ numero di configurazioni possibili;
- il prodotto = probabilità totale di ottenere k successi in qualsiasi ordine.

Il PDF menziona anche la probabilità di ottenere **più di k** successi: si ottiene sommando le probabilità di tutti i casi da k+1 fino a n. Quindi la binomiale non serve solo per “esattamente”, ma anche per eventi come “almeno”, “più di”, “al massimo”, facendo somme di termini binomiali.