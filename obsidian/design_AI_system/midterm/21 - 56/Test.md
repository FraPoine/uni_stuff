### Parte A — Counting e combinatorics

1. Enuncia la **Step Rule of Counting** e spiega in una frase quando si usa.
	- Se un esperimento ha più passi, e:
		- il primo passo ha ***m*** possibilità
		- il secondo ha ***n*** possibilità
		- e così via
		allora il numero totale di esiti è il **prodotto** delle possibilità.
    
2. Due dadi a 6 facce vengono lanciati. Quanti sono gli esiti possibili **se distingui** il primo dado dal secondo?
	- 6 ^ 2
3. Quante stringhe di bit di lunghezza 8:
    - iniziano con `01`
    - oppure finiscono con `10`
    - oppure soddisfano almeno una delle due condizioni?  
        Spiega quale regola di counting usi.

	- Uso la regola del counting con or
	- $| A \ or \ B| = |A| + |B| - |A \ and \ B|$
	- 01xxxxxx 2^6
	- xxxxxx10 2^6
	- 01xxxx10 2^4
	- quindi 2^6 x 2 - 2^4
	
4. Quanti anagrammi distinti si possono formare con la parola **MISSISSIPPI**?
	- ho
		- M 1 
		- I 4
		- S 4
		- P 2
		- totale = 11
		- $\frac{11!}{1!4!4!2!}$
    
5. In quanti modi puoi scegliere 3 oggetti da un insieme di 7 oggetti distinti, senza ordine e senza reinserimento? Scrivi anche la formula generale usata.
	- la formula è
	- $\begin{pmatrix} n\\r \end{pmatrix}  = \frac{n!}{r! (n-r)!}$
	- quindi per prendere 3 oggetti da un insieme di 7 distinti
	- $\begin{pmatrix} 7\\ 3 \end{pmatrix}  = \frac{7!}{3!4!} = 35$
    
6. Hai 10 oggetti distinti da distribuire in 5 contenitori distinti. In quanti modi puoi farlo?
	 - $\begin{pmatrix} 10\\ 5 \end{pmatrix}  = \frac{10!}{5! 5!} = 252$
    
7. Hai 10 oggetti **indistinguibili** da distribuire in 4 contenitori distinti. In quanti modi puoi farlo?
	 - $\begin{pmatrix} n + r -1\\  n \end{pmatrix} =\begin{pmatrix} 13\\3\end{pmatrix}= \frac{13!}{3!(13 - 3)!} = 286$ 
	 - mi riesci a spiegare come mai questa è sbagliata?
		 - $10*9*8*7 = 5040$
### Parte B — Basi della probabilità

8. Definisci:
    - **sample space**
    - **event**  
        e fai un esempio per ciascuno con il lancio di due monete.
	    - il  sample spacel’insieme di tutti i risultati possibili
	    - due lanci di moneta: $S=\{(H,H),(H,T),(T,H),(T,T)\}$
	    - l'event è un sottoinsieme del Sample space
	    - “almeno una testa” su due lanci: $E = \{(H,H),(H,T),(T,H)\}$
        
9. Scrivi la definizione frequentista di probabilità come limite del rapporto tra numero di successi e numero di prove.
	- $P(E)=\lim_{n \to \infty}\frac{\operatorname{count}(E)}{n}$
	- La probabilità di un evento è la sua **frequenza relativa nel lungo periodo**.
    
10. Enuncia i 3 assiomi fondamentali della probabilità presentati nel PDF.
	- Una probabilità non può essere negativa e non può superare 1. $0 ≤ P(E) ≤ 1$
	- Lo spazio campionario completo ha probabilità 1, perché quando fai l’esperimento uno degli esiti possibili deve pur uscire. $P(S) = 1$
	- se due eventi sono mutualmente esclusivi $P(E \ or \ F) = P(E) + P(F)$ cioè se non possono accadere insieme, la probabilità dell’“oppure” è la somma.

11. Se (E) è un evento, qual è la formula per la probabilità del suo complemento (E^c)?
	- $P(E^c) = 1 - P(E)$
    
12. In uno spazio campionario con esiti equiprobabili, come si calcola (P(E))? Poi applicalo al caso:  
    “somma di due dadi uguale a 7”.
	- la probabilità quando gli esiti sono equally likely è $P(E) = \frac{|E|}{|S|}$
	- $P(E) = \frac{|E|}{|S|} = P(somma = 7) = \frac6{36} = \frac16$
    
### Parte C — Many coin flips

13. Un coin flip ha probabilità di testa (p). Se lanci la moneta (n) volte, qual è la probabilità di ottenere:
- tutte teste
	- $p^n$
- tutte croci?
	- $(1-p)^n$
    

14. Con (n=10) e (p=0.6), qual è la probabilità di ottenere la sequenza:  
    `H H H H T T T T T T`?
	- $0.6^4(1-0.6)^{10-4}= 0.00053$
    
15. Scrivi la formula generale della probabilità di ottenere **esattamente (k) teste** in (n) lanci con probabilità di testa (p).
	- $\begin{pmatrix} n\\ k  \end{pmatrix}  = \frac{n!}{k! (n-k)!}$
    
16. Spiega perché nella formula di “esattamente (k) teste” compare il coefficiente binomiale (\binom{n}{k}).
	- esattamente k testi non significa le prime k sono teste e le altre no ma significa che ci sono k teste in qualunque posizione, quindi non c’è **una sola sequenza**, ma molte
    
17. Calcola la probabilità di ottenere **esattamente 4 teste** in 10 lanci con (p=0.6).
	- $\begin{pmatrix} 10\\  4  \end{pmatrix}  = \frac{10!}{4! (10-4)!} 0.6^4(1-0.6)^{10-4} = 0.111$
    
18. Scrivi la formula della probabilità di ottenere **più di (k) teste** in (n) lanci.
	- $P(\text{more than } k \text{ heads})=\sum_{i=k+1}^{n} \begin{pmatrix}n \\ i \end{pmatrix}p^i(1-p)^{n-i}$
19. Con (n=10) e (p=0.6), scrivi esplicitamente la somma da usare per calcolare (P(\text{più di 4 teste})). Non serve svolgerla.
	- $\sum_{i=4+1}^{10} \begin{pmatrix}10 \\ i \end{pmatrix}^i(1-0.6)^{10-i}$
    
20. Vero o falso, con breve motivazione:  
    “La probabilità di ottenere esattamente 4 teste in 10 lanci è uguale alla probabilità della sola sequenza `H H H H T T T T T T`.”
	- falso, la sequenza mostrata è unica, invece eventi con 4 teste su 10 lanci sono tanti, o almeno più di uno

## Mini parte orale

21. Qual è la differenza tra:
- una **specifica sequenza** di lanci
	- questa è unica
- l’evento “**esattamente (k) teste**”?
	- sono molte
22. Qual è la differenza tra:
- **permutations of distinct objects**
	- Qui conta **l’ordine**.
	- Se hai n oggetti tutti diversi, il numero di ordinamenti possibili è: ***n!***
	- Per il primo posto hai n scelte, per il secondo n−1, poi n−2, ecc.
- **permutations of indistinct objects**
	- Qui l’ordine conta, **ma alcuni oggetti sono uguali**. 
	- Se hai n oggetti in totale, con gruppi di indistinguibili di dimensione n1,n2,…,nr, allora: n! tratta tutto come distinto e quindi **overcounta**. $\frac{n!}{n_1!n_2!...n_r!}$
- **combinations**?
	- Qui **l’ordine non conta**.
	- Scegli r oggetti da n oggetti distinti, senza rimpiazzo:
	- $\begin{pmatrix}  n\\  r  \end{pmatrix}  = \frac{n!}{r! (n-r)!}$
    
23. Perché nei problemi di probabilità saper contare bene è fondamentale? Rispondi in 3–5 righe.
    - Il counting serve a rispondere a domande del tipo:
		- quante possibilità ci sono?
		- quante configurazioni diverse posso ottenere?
		- quante scelte, sequenze, assegnazioni o casi esistono?
## Parte D — Conditional probability + independence

24. Scrivi la definizione di probabilità condizionata (P(E \mid F)). Spiega a parole che cosa significa.
	- **qual è la probabilità che succeda E, sapendo che è già successo F?**
	- **probabilità di E dato F**
	- quando osservi F, entri nel “mondo” in cui F è già accaduto, quindi il tuo spazio dei possibili risultati si restringe.
    
25. Ricava dalla definizione di probabilità condizionata la **chain rule** per due eventi:  
    [  
    P(E \cap F)=P(E \mid F)P(F)  
    ]  
    e scrivi anche la forma equivalente con (P(F \mid E)).
	- $P(E\ |\ F) = \frac{P(E\ and\ F)}{P(F)}$
	- purché P(E) > 0
	- qua mi dai una mano tu e mi dai la risposta
    
26. Che cosa significa che due eventi (E) e (F) sono **indipendenti**?  
    Scrivi:
- la definizione in termini di condizionale
- la formula equivalente per l’intersezione.
	- Due eventi sono indipendenti se sapere che uno è successo **non cambia** la tua credenza sull’altro. Il PDF lo definisce proprio così.
	- $P(E\ |\ F) = P(E)$
	- osservare F non ti dà informazione utile su E.
	- $P(E\ and\ F)=P(E)P(F)$ viene dalla conditional probability
	- $P(E∣F) = \frac{P(E\ and\ F)}{P(F)}$
	- se l’indipendenza dice che $P(E \mid F) = P(E)$, allora ottieni:
	- $P(E\ and\ F)=P(E)P(F)$
	
27. Vero o falso, con breve spiegazione:  
    se (E) e (F) sono indipendenti, allora  
	- $P(E \mid F)=P(E).$
		- vero, per definizione sapere che succede uno **non cambia** la probabilità dell’altro
    
28. Vero o falso, con breve spiegazione:  
    se (E) e (F) sono mutuamente esclusivi, allora sono indipendenti.
	- falso, mutualmente esclusivi significa che
	- $P(E\ and \ F) = 0$
    
29. Se (P(E)=0.4), (P(F)=0.5) e (E,F) sono indipendenti, calcola:
	- $(P(E \cap F))$
		- $P(E \ and\ F) = P(E)P(F)$ = $0.4 * 0.5 = 0.2$
	- $(P(E \mid F)).$
		- P(E) = 0.4
    
30. Se $(P(E \cap F)=0.18)\ e\ (P(F)=0.3)$, calcola $(P(E \mid F))$. Poi spiega se da questi soli dati puoi concludere che (E) e (F) siano indipendenti.
	- $P(E∣F) = \frac{P(E\ and\ F)}{P(F)}$ 
	- $P(E∣F) = \frac{0.18}{0.3} =0.6$
	- so solo che non sono mutualmente esclusivi ma non posso dire se sono indipendenti

    
31. Scrivi la chain rule per tre eventi:  
	- $P(E_1 \cap E_2 \cap E_3)=\dots$
		- generalizzazione della chain rule 
		- $P(E_1​,\dots,E_n​)=P(E_1​)P(E_2​∣E_1​)\dots P(E_n​∣E_1​,\dots,E_n−1​)$
		- quindi
		- $P(E_1,E_2,E_3) = P(E_1)P(E_2 \mid E_1)P(E_3 \mid E_2, E_1)$

32. Che cosa vuol dire **conditional independence**?  
    Scrivi una formula del tipo “(E_1,E_2,E_3) sono indipendenti dato (F)”.
	- Due o più eventi possono essere indipendenti **solo dopo aver fissato una certa informazione di contesto**. Questo si chiama **conditional independence**.
	- $P(E1​,E2​,E3​∣F)=P(E1​∣F)P(E2​∣F)P(E3​∣F)$

## Parte E — Total probability + Bayes

33. Enuncia la **law of total probability** nel caso semplice con un evento (B) e il suo complemento:  
	$P(E)=\dots$
	- Ledue parti sono:
		- **mutuamente esclusive**
		- e insieme coprono tutto lo spazio campionario.
	- Quindi ogni volta che succede E, deve succedere in uno di questi due modi:
		- E insieme a F
		- oppure E insieme a F^c 
	- quindi $P(E)=P(E\ and\ F)+P(E\ and\ F_c)$
	- e usando la chain rule il PDF scrive:
		- $P(E)=P(E \mid F)P(F)+P(E \mid F_c)P(F_c)$
    
34. Enuncia la versione generale della law of total probability usando eventi $(B_1,\dots,B_n)$ mutuamente esclusivi che coprono tutto lo sample space.
	- $P(E)=\sum_{i=1}^{n} P(E \mid B_i)\,P(B_i)$  
    
35. Scrivi la formula classica di **Bayes**:  
	$P(B \mid E)=\dots$
    e indica il significato di:
	- posterior
	- prior
	- evidence / normalization constant.
		- $P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}$
		- $P(B∣E)$ = **posterior**
		- $P(B)$ = **prior**
		- $P(E \mid B)$ = **likelihood**
		- $P(E)$ = **normalization constant**
    
36. Spiega perché Bayes è utile quando vuoi inferire una causa non osservabile a partire da un’evidenza osservabile. Fai un esempio.
	- Bayes è utile quando hai:
		- una cosa nascosta che vuoi sapere
		- una cosa osservabile che dipende da quella cosa nascosta
	- E vuoi passare dall’osservabile al nascosto.
		- malattia → risultato del test
		- abilità dello studente → risposte date
		- posizione del telefono → segnale osservato
    
37. Scrivi Bayes combinato con la law of total probability:  
    $P(B_i \mid E)=\dots$
	- $P(B \mid E)=\frac{P(E \mid B)\,P(B)}{P(E \mid B)\,P(B)+P(E \mid B^c)\,P(B^c)}$
	- più in generale, se hai molti casi 
	- $P(B_i \mid E)=\frac{P(E \mid B_i)\,P(B_i)}{\sum_{j=1}^{n} P(E \mid B_j)\,P(B_j)}$
    
38. Problema numerico.  
    Sia:
- $(P(I)=0.13)$
- $(P(+ \mid I)=0.92)$
- $(P(+ \mid I^c)=0.10)$
Calcola:
- $(P(+))$ con la law of total probability
- $(P(I \mid +))$ con Bayes.
	- $P(E)=P(E \mid F)P(F)+P(E \mid F_c)P(F_c)$
	- $P(+)=P(+ \mid I)P(I)+P(+ \mid I^c)(1-P(I)) =$
	- $P(+)=0.92 * 0.13 + 0.1 * 0.87 = 0.2066$
	- $P(B \mid E) = \frac{P(E \mid B)P(B)}{P(E)}$
	- $P(I \mid +) = \frac{P(+ \mid I)P(I)}{P(+)} =$
	- $P(I \mid +) = \frac{0.92 * 0.13}{0.2} = 0.58$

39. Nel problema del test medico sopra, spiega perché (P(+ \mid I)) e (P(I \mid +)) **non** sono la stessa cosa.
	- $P(E \mid B)$: se l’ipotesi B è vera, quanto spesso vedo l’evidenza?
	- $P(B \mid E)$: dato che ho visto l’evidenza, quanto è probabile che B sia vera?
    
40. Vero o falso, con breve motivazione:  
    “Se un test è molto accurato, allora la probabilità di avere la malattia dato un test positivo è necessariamente molto alta.”
	- no, dipende da quanto è rara la malattia
    
41. Domanda concettuale finale:  
    quando in Bayes il denominatore (P(E)) non è dato esplicitamente, qual è la strategia standard per calcolarlo?
	- si fa Bayes + Law of Total Probability
	- $P(B \mid E)=\frac{P(E \mid B)\,P(B)}{P(E \mid B)\,P(B)+P(E \mid B^c)\,P(B^c)}$
    
