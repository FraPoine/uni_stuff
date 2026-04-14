## Esercizi

### 1. Random variables

**Esercizio 1**
Lanci 3 monete e definisci X = numero di teste ottenute
- Quali valori può assumere X?
	- {0,1,2,3}
- L’evento X=2 cosa significa in parole?
	- nei 3 lanci di monete è uscito testa esattamente 2 volte
- L’evento X<2 quali valori di X include?
	- {0,1}
- X è una variabile aleatoria discreta o continua?
	- discreta

---

**Esercizio 2**  
Lanci un dado a 6 facce e definisci (Y) = valore uscito.

1. Scrivi il supporto di (Y).
	- il supporto è l'insieme dei valori possibili {1,2,3,4,5,6}
    
2. Descrivi a parole gli eventi:
    - (Y=4)
	    - sul dado esce la faccia 4
    
    - $(Y\geq 5)$
	    - sul dado esce la faccia 5 o 6
        
    - $(Y\neq 2)$
	    - sul dado esce una faccia diversa da 2
        

---

**Esercizio 3**  
Definisci (Z) come “tempo di attesa, in minuti, del prossimo autobus”.

1. (Z) è discreta o continua?
	- discreta
    
2. Quale dei seguenti è un evento?
    - (Z)
    - (Z=5) <== questo qua
    - (P(Z=5))
        

---
### 2. PMF Probability mass function

**Esercizio 4**  
Una variabile discreta (X) ha la seguente PMF:

$P(X=0)=0.2,\quad P(X=1)=0.5,\quad P(X=2)=0.3$
1. Verifica che sia una PMF valida.
	- è valida perchè la somma delle probabilità è 0
2. Calcola (P(X<2)).
	- 0.2 + 0.5 = 0.7
    
3. Calcola $(P(X\geq 1))$.
	- 0.5 + 0.3 = 0.8
    

---

**Esercizio 5**  
Sia (X) il risultato di un dado equo.

1. Scrivi la PMF di (X).
	- $P(X = x) = \frac16\ per\ x = 1,\dots,6.$
    
2. Calcola (P(X=3)).
	- = 1/6
    
3. Calcola $(P(X\leq 4))$.
	- 2/3
    
4. Calcola (P(X>4)).
	- 1/3

---

**Esercizio 6**  
Sia (S) la somma di due dadi equi.

1. Qual è il supporto di (S)?
	- {2,3,4,5,6,7,8,9,10,11,12}
    
2. Calcola (P(S=2)).
	- 1/36
    
3. Calcola (P(S=7)).
	- 1/6
    
4. Calcola (P(S=12)).
	- 1/36
    
5. Quale valore ha PMF massima?
	- il 7
    

---

**Esercizio 7**  
Una variabile (X) ha:
$P(X=1)=a,\quad P(X=2)=2a,\quad P(X=3)=3a$
1. Trova (a).
    - a +2a +3a = 1 
    - 6a =1 
    - a = 1/6
2. Calcola $(P(X\ge 2))$.
	- 5/6
3. Calcola (P(X<3)).
	- 1/2
    

---

### 3. Expectation
**Esercizio 8**  
Per la variabile
$P(X=0)=0.2,\quad P(X=1)=0.5,\quad P(X=2)=0.3$  

calcola $(E[X])$.
- L’**expectation** è il riassunto più importante di una random variable
- la **media pesata** dei valori possibili, dove ogni valore è pesato con la sua probabilità
- $(E[X])= 1.1$.

---

**Esercizio 9**  
Sia (X) il risultato di un dado equo.
1. Calcola $(E[X])$.
	- 3.5
2. Il valore atteso coincide sempre con un valore che può uscire davvero? Spiega.
	- no, il valore atteso è il valore che ripetendo l'esperimento moltissime volte dovremmo ottenere
    

---

**Esercizio 10**  
Sia (S) la somma di due dadi equi.

1. Sapendo che il valore atteso di un dado è (3.5), usa la linearità dell’aspettativa per calcolare (E[S]).
	- linearità dell'aspettativa
		- $E[aX + b] = aE[X]+b$
		- $E[X + Y] = E[X]+E[Y]$
	- $E[3.5 + 3.5] = 7$
    
2. Senza fare tutta la PMF, quanto vale$(E[2S+1])$?
	- = 15

---

**Esercizio 11**  
Una variabile (X) ha PMF:

$P(X=1)=0.4,\quad P(X=3)=0.6$

1. Calcola (E[X]).
	- 0.4 + 1.8 = 2.2
    
2. Calcola (E[2X]).
	- 4.4
    
3. Verifica che (E[2X]=2E[X]).
	- per la linearità dell'aspettativa
		- $E[aX + b] = aE[X]+b$
    

---

**Esercizio 12**  
Sia (X) una variabile con

$P(X=0)=0.1,\quad P(X=2)=0.4,\quad P(X=5)=0.5$

calcola:
1. (E[X])
	- 2.5 + 0.8 = 3.3
2. (E[X^2])
	- 3.3^2

---

### 4. Variance e standard deviation

**Esercizio 13**  
Per la variabile

$P(X=0)=0.2,\quad P(X=1)=0.5,\quad P(X=2)=0.3$

calcola:

1. (E[X])
	- 0.5 + 0.6 = 1.1
    
2. (E[X^2])
	- $E[g(X)] = \sum_x g(x)P(X=x)$
	- 0.5 + 4 x 0.3= 1.7
    
3. $(\mathrm{Var}(X))$
	- Se l’aspettativa ti dice il **centro** della distribuzione, la **varianza** ti dice quanto i valori sono **sparsi** attorno a quel centro. I
	- $Var(X) = E [(X - μ)^2]$
	- con µ = $E[X]$ 
	- $Var(X) = E[X^2] - E[X]^2$
	- 1.7 - 1.21 = 0.49
    
4. $(\mathrm{Std}(X))$
	- è semplicemente la radice quadrata della varianza 
	- 0.7
    

---

**Esercizio 14**  
Sia (X) il risultato di un dado equo.

1. Calcola (E[X]).
    
2. Calcola (E[X^2]).
    
3. $Calcola (\mathrm{Var}(X)).$
    
4. $Calcola (\mathrm{Std}(X)).$
    

---

**Esercizio 15**  
Una variabile (X) ha:

[  
P(X=1)=0.5,\quad P(X=5)=0.5  
]

1. Calcola (E[X]).
    
2. Calcola (\mathrm{Var}(X)).
    
3. La distribuzione è molto concentrata o molto dispersa? Spiega.
    

---

**Esercizio 16**  
Due variabili hanno entrambe media (10).

- La prima ha valori quasi sempre vicini a 10.
    
- La seconda assume spesso valori 2 e 18.
    

Quale ha varianza maggiore? Perché?

---

### 5. Binomial distribution

**Esercizio 17**  
Una moneta equa viene lanciata 5 volte. Sia (X) = numero di teste.

1. Di che distribuzione si tratta?
    
2. Quali sono (n) e (p)?
    
3. Calcola (P(X=0)).
    
4. Calcola (P(X=5)).
    

---

**Esercizio 18**  
Una moneta equa viene lanciata 4 volte. Calcola:

1. (P(X=2))
    
2. (P(X=3))
    
3. (P(X\ge 3))
    

dove (X) è il numero di teste.

---

**Esercizio 19**  
Una moneta ha probabilità di testa (p=0.6). Viene lanciata 10 volte. Sia (X\sim \mathrm{Bin}(10,0.6)).

Calcola:

1. (P(X=4))
    
2. (P(X=6))
    
3. (P(X>6))
    

---

**Esercizio 20**  
In un test a scelta multipla ogni domanda ha probabilità (0.25) di essere risposta correttamente a caso.  
Uno studente risponde a caso a 8 domande. Sia (X) = numero di risposte corrette.

1. Che distribuzione ha (X)?
    
2. Calcola (P(X=0)).
    
3. Calcola (P(X=2)).
    
4. Calcola (P(X\ge 1)).
    

---

**Esercizio 21**  
Una fabbrica produce pezzi difettosi con probabilità (0.1). Si prendono 6 pezzi indipendenti. Sia (X) = numero di pezzi difettosi.

1. Calcola (P(X=1)).
    
2. Calcola (P(X=2)).
    
3. Calcola (P(X\le 1)).
    

---

**Esercizio 22**  
Per (X\sim \mathrm{Bin}(n,p)), con (n=12) e (p=0.3), calcola il valore atteso:  
[  
E[X]  
]

---

### 6. Normal distribution

**Esercizio 23**  
Sia (X\sim N(10,4)).

1. Qual è la media?
    
2. Qual è la varianza?
    
3. Qual è la deviazione standard?
    

---

**Esercizio 24**  
Sia (X\sim N(\mu,\sigma^2)) con (\mu=50) e (\sigma=8).

1. Standardizza il valore (x=58), cioè calcola  
    [  
    z=\frac{x-\mu}{\sigma}  
    ]
    
2. Standardizza (x=42).
    

---

**Esercizio 25**  
Sia (X\sim N(100,25)).

1. Scrivi la distribuzione della variabile standardizzata  
    [  
    Z=\frac{X-100}{5}  
    ]
    
2. Quanto vale (P(X\le 100)) per simmetria?
    

---

**Esercizio 26**  
Sia (X\sim N(20,9)).

Usa la standardizzazione per trasformare:

1. (P(X\le 23))
    
2. (P(X>17))
    
3. (P(17<X<23))
    

in probabilità su una standard normal (Z\sim N(0,1)).  
Non serve calcolare il numero finale, basta impostarle bene.

---

**Esercizio 27**  
Sia (X\sim N(30,16)).

1. Calcola gli z-score di (26) e (34).
    
2. Quale probabilità rappresenta:  
    [  
    P(26<X<34)  
    ]  
    scritta in termini di (\Phi)?
    

---

**Esercizio 28**  
Una variabile normale ha media (12) e deviazione standard (3).

1. Scrivi l’intervallo “entro una deviazione standard dalla media”.
    
2. Secondo la regola vista nel PDF, circa quale probabilità cade in quell’intervallo?
    

---

## Mini blocco misto

**Esercizio 29**  
Sia (X) una variabile discreta con

[  
P(X=0)=0.25,\quad P(X=1)=0.5,\quad P(X=2)=0.25  
]

calcola:

1. (E[X])
    
2. (E[X^2])
    
3. (\mathrm{Var}(X))
    

---

**Esercizio 30**  
Una moneta equa viene lanciata 3 volte. Sia (X) = numero di teste.

1. Scrivi la PMF completa di (X).
    
2. Calcola (E[X]).
    
3. Quale distribuzione è?
    

---

**Esercizio 31**  
Sia (X\sim \mathrm{Bin}(5,0.5)).

1. Calcola (P(X=2)).
    
2. Calcola (P(X\le 2)).
    
3. Calcola (E[X]).
    

---

**Esercizio 32**  
Sia (X\sim N(40, 36)).

1. Qual è (\sigma)?
    
2. Standardizza (x=46).
    
3. Standardizza (x=34).
    
4. Quale dei due valori è sopra la media?
    

---

Se vuoi, nel messaggio dopo ti mando anche le **soluzioni complete**, oppure possiamo farli **uno alla volta** come se fosse una verifica.