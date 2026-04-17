## Esercizi

### Parte A — Beta distribution

**1. Parametri della Beta**  
Hai osservato 7 successi e 3 fallimenti in un processo binario.  
Assumendo prior uniforme, scrivi la distribuzione posterior di (X), cioè trova i parametri (a) e (b) della Beta.

- con **prior uniforme** stai usando $Beta(1,1)$
- dopo aver osservato h successi e t fallimenti, la posterior diventa
	- $X∼Beta(h+1,t+1)$
- a=h+1,b=t+1
- a = 8 e b = 4
- $X∼Beta(8,4)$

**2. Media della Beta**  
Se $(X \sim \text{Beta}(5,3))$, calcola:
- $(E[X])$
	- $E[X] = \frac{a}{a+b} = \frac58 = 0.625$
- interpreta il risultato in parole semplici.
	- se x rappresenta una probabilità sconosciuta, la tua credenza media su quella probabilità è circa 0.625

**3. Varianza della Beta**  
Se ($X \sim \text{Beta}(5,3)), calcola (\mathrm{Var}(X)).$
- $Var(X)=\frac{ab}{(a+b)^2(a+b+1)}​. = \frac{15}{(25+9+30)9} = 0.026$

**4. Posterior dopo lanci di moneta**  
Una moneta viene lanciata 10 volte e si osservano 9 teste e 1 croce.  
Assumendo prior uniforme:
- scrivi la forma del posterior
- indica quale valore di (p) appare più plausibile
- spiega perché il posterior in (p=1) vale 0.

- con **prior uniforme** sto usando $Beta(1,1)$
- $X∼Beta(h+1,t+1)$ quindi:
	- $X∣H=9,T=1∼Beta(10,2)$
- il valore più plausibile è 0.9 perchè ho avuto 9 teste
- la densità ha forma
	- $f(x∣H=9,T=1)=Kx^9(1−x)$
- se x = 1 il fattore 1-x va a 0 quindi la densità va a 0

**5. Prior Beta non uniforme** 
Supponi di partire da una prior $(X \sim \text{Beta}(4,2))$.
Poi osservi 3 successi e 5 fallimenti.
Trova la nuova posterior.
- con prior non uniforme $X∼Beta(a+h,b+t)$
- quindi $X∼Beta(4+3,2+5)=Beta(7,7)$

**6. Prior come “imaginary trials”**  
Nel PDF si dice che una prior Beta può essere vista come se contenesse prove immaginarie.  
Per $(X \sim \text{Beta}(6,4))$:

- quante “imaginary heads” contiene?
- quante “imaginary tails” contiene?
- prior $X \sim \text{Beta}(a,b)X$ si interpreta come:
	- **a−1** successi immaginari
	- **b−1** fallimenti immaginari
- quindi
	- **imaginary heads** =6−1=5
	- **imaginary tails** =4−1=3
---

### Parte B — Somma di variabili casuali

**7. Somma di due dadi**  
Due dadi equi e indipendenti vengono lanciati.  
Calcola (P(X+Y=8)) usando l’idea della convoluzione discreta, cioè contando tutti i casi possibili che danno 8.
- li elenco
- {(2,6)(6,2)(3,5)(5,3),(4,4)}
- i casi favorevoli sono 5

**8. Formula della convoluzione discreta**  
Scrivi la formula generale per (P(X+Y=n)) nel caso discreto.  
Poi spiegala a parole, senza simboli tecnici.
- $P(X+Y=n)=\Sigma_{i=-∞}​^{∞}P(X=i,Y=n−i)$
- e, se X e Y sono **indipendenti**, diventa:
	- $P(X+Y=n)=\Sigma_{i=-∞}​^{∞}P(X=i)P(Y=n−i)$
- per sapere la probabilità che la somma valga n, devi considerare **tutti i modi possibili** in cui X e Y possono sommarsi a n.
- Per esempio, se vuoi X+Y=8, i casi possibili sono:
	- X=0,Y=8
	- X=1,Y=7
	- X=2,Y=6
	- …
	- X=8,Y=0
- Se X e Y sono indipendenti, la probabilità di ciascun caso si spezza in prodotto:
	- $P(X=i,Y=n−i)=P(X=i)P(Y=n−i)$

**9. Somma di Poisson**  
Se $(X \sim \text{Poi}(2))$ e $(Y \sim \text{Poi}(5))$, indipendenti:

- qual è la distribuzione di (X+Y)?
- qual è $(P(X+Y=3))$?
	- **la somma di due Poisson indipendenti è ancora una Poisson**,
		- $X+Y∼Poi(λ1​+λ2​) = Poi(7)$
	- $Z = X+Y$
	- La formula della PMF della Poisson è
		- $P(Z=n)=e^{-\lambda}\frac{\lambda^n}{n!}$
	- con $\lambda = 7, n=3$
		- $P(X + +Y =3)=e^{-7}\frac{7^3}{3!} = 0.0521$
	- 

**10. Somma di Binomiali**  
Se $(X \sim \text{Bin}(4,0.3))$ e $(Y \sim \text{Bin}(6,0.3))$, indipendenti:
- qual è la distribuzione di (X+Y)?
	- **la somma di due variabili binomiali indipendenti con la stessa probabilità di successo p è ancora una binomiale**, con numero di prove uguale alla somma delle prove.
	- X conta i successi in 4 prove con probabilità 0.3
	- Y conta i successi in 6 prove con probabilità 0.3
	- X+Y∼Bin(10,0.3)

**11. Somma di Normali**  
Se $(X \sim N(2, 1.5)) e (Y \sim N(4, 3.5))$, indipendenti, trova la distribuzione di (X+Y).  
Attenzione: nel PDF il secondo parametro è la varianza.
- se $X \sim N(\mu_1,\sigma_1^2)$ e $Y \sim N(\mu_2,\sigma_2^2)$ sono indipendenti, allora
- $X+Y∼N(μ_1​+μ_2​, σ_1^2​+σ_2^2​)$
- quindi con 
	- $(X \sim N(2, 1.5)) e (Y \sim N(4, 3.5))$
	- $X+Y∼N(6,5)$

**12. Somma di Uniformi**  
Se (X) e (Y) sono indipendenti e uniformi in $([0,1])$, scrivi la densità di (X+Y) nei tre casi:
- $(0<n\le1)$
- $(1<n\le2)$
- altrimenti.

- Z = X+Y
- formula di convoluzione per variabili continue 
	- $fZ​(n)=∫_{−∞}^+∞​fX​(n−i)fY​(i)di$
- Siccome $X\sim \text{Uni}(0,1)$ e $Y\sim \text{Uni}(0,1)$, vale:
$$
\begin{matrix}
fX​(x)=1\ se\ 0≤x≤1,\ 0 \ altrimenti \\ fY(y)=1\ se\ 0≤y≤1, \ 0 \ altrimenti
\end{matrix}
$$
- Quindi dentro l’integrale il prodotto vale 1 solo quando contemporaneamente:
	- i è tra 0 e 1 
	- n - i è tra 0 e 1
- quindi
	- 0≤n−i≤1
	- n−1≤i≤n
- facciamo i casi
	- $(0<n\le1)$
		- intersezione è tra 0 e n quindi la lunghezza è n
	- $(1<n\le2)$
		- l'intersezione è tra n-1 e 1 quinid la lunghezza è 1- (n-1) = 2-n
	- altrimenti.
		- non può succedere, perché somma di due numeri tra 0 e 1 non può essere né negativa né maggiore di 2. Quindi è 0

---

### Parte C — Central Limit Theorem

**13. Formula del CLT per la somma**  
Enuncia la versione del CLT per la somma di variabili IID:  
$\sum_{i=1}^n X_i$
specificando media e varianza approssimate.

- la media della somma è **nμ**;
- la varianza della somma è **nσ^2**.
-  $μ=E[Xi]$ e $\sigma^2=\mathrm{Var}(X_i)$)
- $i=1∑n​Xi​≈N(nμ,nσ^2).$

- Central Limit Theorem CLT
	- Let be $X_1,X_2,\dots,X_n$ independent and identically distributed random variables.
	- the sum of these random variables approaches a normal as $n \Rightarrow \infty$
	- IID --> **Independent and Identically Distributed**.
	- anche se una singola variabile casuale **non** è distribuita normalmente, quando prendi **molte copie IID** di quella variabile e le **sommi** oppure ne fai la **media**, il risultato tende ad avere una forma **circa normale**.
	- per il CLT serve 
		- la **somma** di tante osservazioni tende a una normale
		- anche la **media campionaria** tende a una normale
		- $\Sigma_{i=1}^n​Xi​$
		- si comporta approssimativamente come una normale con media nμ e varianza $n\sigma^2$, dove $μ=E[Xi]$ e $\sigma^2=\mathrm{Var}(X_i)$)

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

**14. Formula del CLT per la media**  
Enuncia la versione del CLT per la media campionaria:  
$\frac{1}{n}\sum_{i=1}^n X_i$
specificando media e varianza approssimate.

- #### Central Limit Theorem (average version)
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

**15. Somma di 10 dadi con CLT**  
Sia $(X=X_1+\dots+X_{10})$, dove ogni $(X_i)$ è il risultato di un dado equo.  
Usa i valori dati nel PDF:
- $(E[X_i]=3.5)$
- $(\mathrm{Var}(X_i)=35/12)$
Trova la distribuzione normale approssimante di (X).
- **PMF** = Probability Mass Function, per variabili **discrete**
- **PDF** = Probability Density Function, per variabili **continue**

- $E[X_i]=\mu$
-  $\mathrm{Var}(X_i)=35/12$
- n =  10
$$
\sum_{i=1}^{n} X_i \approx \mathcal{N}(n\mu,\, n\sigma^2) = 
\mathcal{N}(35,29.17)
$$
**16. Continuity correction**  
Nel problema precedente, vuoi approssimare $(P(X\le 25))$.  
Quale correzione di continuità devi usare? 
Scrivi il passaggio corretto con la variabile normale approssimante (Y).

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

**17. Probabilità di vincita** 
Nel gioco dei 10 dadi del PDF, vinci se $(X\le 25)$ oppure $(X\ge 45)$.  
Senza rifare tutti i conti numerici finali, imposta correttamente il calcolo con il CLT e la continuity correction.

Usa i valori dati nel PDF:
- $(E[X_i]=3.5)$
- $(\mathrm{Var}(X_i)=35/12)$
quindi, per il CLT, la somma X si approssima con una normale Y tale che
$$
Y \sim \mathcal{N}(35,29.17)
$$
L'evento vinco 
- X≤25 oppure X≥45
- P(vinco)=P(X≤25 or X≥45)
- X≤25 diventa Y<25.5
- X≥45 diventa Y>44.5
quindi
- P(vinco)≈P(Y<25.5)+P(Y>44.5)
$$
P(Y<25.5)=Φ(\frac{25.5−35}{\sqrt{29.2}}​) \ e\ P(Y<25.5)=Φ(\frac{44.5−35}{\sqrt{29.2}}​)
$$
- setup finale
$$
P(vinco)=Φ(\frac{25.5−35}{\sqrt{29.2}}​) +[1-Φ(\frac{44.5−35}{\sqrt{29.2}}​)]
$$


---

### Parte D — Sampling e standard error

**18. Media campionaria**  
Scrivi la formula della sample mean $(\bar X)$ per un campione $(X_1,\dots,X_n)$.  
Poi spiega che cosa sta stimando.
- $\bar X = \frac1n \sum^n_{i=1}X_i$
- cioè fai la somma di tutte le osservazioni del campione e poi dividi per il numero totale di osservazioni n

**19. Varianza campionaria**  
Scrivi la formula della sample variance (S^2).  
Perché compare (n-1) al denominatore invece di (n)? Rispondi in modo concettuale.

La **sample variance**
$$
S^2=\frac1{n−1}\sum_{​i=1}^n​(Xi​−\bar X) \ con\ \bar X = \frac1n \sum^n_{i=1}X_i
$$
La varianza vera della popolazione dovrebbe misurare quanto i dati stanno lontani dalla **vera media** μ.
Però noi μ non la conosciamo, quindi nel campione usiamo Xˉ, cioè la **media del campione**.
se mettessi n al denominatore, la stima tenderebbe a venire **troppo piccola**: infatti Xˉ è stata calcolata dagli stessi dati, quindi in un certo senso “si adatta” al campione e riduce artificialmente le distanze quadratiche. Usare n−1 serve a correggere questo effetto.



**20. Unbiased estimator**  
Che cosa significa dire che $(\bar X)$ è un estimatore unbiased di $(\mu)$?  
E che cosa significa dire che $(S^2)$ è un estimatore unbiased di $(\sigma^2)$?
- Uno stimatore è **unbiased** se, **in media**, indovina il valore vero del parametro.
- se ripetessi il campionamento tante volte e ogni volta ricalcolassi lo stimatore, la **media dei valori ottenuti** sarebbe proprio il parametro vero.

- Dire che $\bar X$ è un estimatore unbiased di μ significa:
$$
E[\bar X] = \mu
$$
la **media campionaria** non è perfetta in ogni singolo campione, però **non ha un errore sistematico** verso l’alto o verso il basso. A volte sovrastima, a volte sottostima, ma mediamente centra μ.
Dire che S^2 è un estimatore unbiased di σ^2 significa:
$$
E[S^2] = \sigma^2
$$
la **varianza campionaria** con il denominatore n−1 è costruita proprio in modo che, mediando su tantissimi campioni possibili, restituisca la **vera varianza della popolazione**.



**21. Standard error**  
Scrivi la formula approssimata dello standard error della media campionaria usando (S^2).  
Poi spiega che cosa misura.

- **formula approssimata** dello standard error della media campionaria
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

**22. Effetto della dimensione del campione**  
Se lasci invariata la variabilità dei dati ma quadruplichi (n), come cambia approssimativamente lo standard error?

partendo da
$$
SE(\bar X) \sim \sqrt{\frac{S^2}n} = \frac{S}{\sqrt{n}}
$$
Quadruplichiamo n
$$
SE(\bar X) \sim \sqrt{\frac{S^2}{4n}} = \frac{S}{2\sqrt{n}}
$$
Quindi il nuovo standard error è **la metà** di quello iniziale

quando il campione diventa 4 volte più grande, la media campionaria diventa **più precisa**, e la sua incertezza si **dimezza**.

---

### Parte E — Bootstrap

**23. Idea del bootstrap**  
Spiega in 4–5 righe che cos’è il bootstrap e qual è la sua idea fondamentale.  
Usa solo i concetti del PDF.

l **bootstrap** è una tecnica computazionale usata per stimare la distribuzione di una statistica quando la distribuzione vera dei dati è sconosciuta. L’idea è trattare il campione osservato come una buona approssimazione della distribuzione sottostante. Poi si generano molti **resampling** della stessa dimensione del campione originale e si ricalcola ogni volta la statistica di interesse. Guardando come varia questa statistica nei resampling, possiamo stimarne la variabilità e quindi l’incertezza.


**24. Procedura bootstrap**  
Hai un campione di dimensione (n=100).  
Descrivi i passaggi per stimare via bootstrap la distribuzione della sample mean.  
Il punto chiave: di che dimensione devono essere i resampling?

1. Parti dal campione osservato di 100 dati. Questo campione viene usato come miglior approssimazione della distribuzione vera sconosciuta.
2. Generi un **bootstrap sample** estraendo **con rimpiazzo** da quei 100 valori.  Siccome è con rimpiazzo, alcuni valori possono comparire più volte e altri possono non comparire.
3. Il bootstrap sample deve avere **la stessa dimensione del campione originale**, quindi ancora **100 osservazioni**. Questo è fondamentale perché vogliamo imitare la variabilità della statistica per campioni della stessa taglia dell’esperimento originale.
4. Su questo nuovo campione calcoli la **sample mean**.
5. Ripeti il procedimento molte volte, ottenendo tante medie bootstrap.
6. L’insieme di tutte queste medie bootstrap approssima la **distribuzione della sample mean**. Da lì puoi stimare variabilità, standard error o intervalli.

**25. Bootstrap e assunzioni**  
Il PDF dice che il bootstrap funziona bene in molti casi, ma può essere problematico in altri.  
Indica due situazioni in cui può funzionare peggio.

Il bootstrap può funzionare peggio in due casi principali:
- **Quando la distribuzione ha code lunghe (long tails).**  
	- In questo caso il campione osservato può non rappresentare bene gli eventi estremi, quindi i resampling bootstrap rischiano di dare una stima poco affidabile della variabilità reale.
- Quando i dati non sono IID
	- cioè non sono indipendenti e identicamente distribuiti. Il bootstrap standard assume proprio IID; se le osservazioni sono dipendenti tra loro o provengono da distribuzioni diverse, il resampling dal campione non riproduce bene la struttura vera dei dati.
---

### Parte F — Bootstrap p-value

**26. Null hypothesis**  
Nel test bootstrap per confrontare Bhutan e Nepal, qual è l’ipotesi nulla?  
Scrivila in parole semplici.

- Ipotesi nulla $H_0$​:
	- non c’è una vera differenza tra Bhutan e Nepal nella distribuzione della felicità, quindi la differenza osservata tra le due medie è dovuta solo al caso, cioè al campionamento.
$$
H0​: F_{Bhutan​}=F_{Nepal}
$$
cioè i due campioni vengono dalla **stessa distribuzione**.

**27. Perché si uniscono i campioni?**  
Nel bootstrap p-value, sotto l’ipotesi nulla i dati dei due gruppi vengono messi insieme.  
Spiega perché ha senso farlo.
- sotto l’ipotesi nulla i due gruppi non sono davvero diversi.
- per Bhutan e Nepal, la null hypothesis dice proprio che **non c’è differenza tra la distribuzione della felicità nei due paesi** e che l’eventuale differenza osservata tra le medie è dovuta solo al caso campionario. Per questo il testo costruisce una **distribuzione unica comune** usando **tutti** i dati dei due gruppi insieme.

**28. Definizione di p-value bootstrap**  
Supponi che la differenza osservata tra le medie sia (0.5).  
Dopo molti resampling sotto l’ipotesi nulla, in 37 casi su 1000 la differenza simulata è almeno (0.5).  
Qual è il p-value approssimato?  
Come lo interpreteresti?
$$
p-value≈\frac{numero\ di\ simulazioni\ almeno\ cosi'\ estreme}{numero\ totale\ di\ simulazioni}​
$$

- p-value = 37/1000 = 0.037
- Significa che, **se davvero l’ipotesi nulla fosse vera** e i due gruppi avessero in realtà la stessa distribuzione, una differenza tra le medie **grande almeno quanto 0.5** comparirebbe per puro caso circa nel **3.7%** dei casi.
- Dato che **0.037 è piccolo**, i dati forniscono **evidenza contro l’ipotesi nulla**.
- Se usi la soglia classica del 5%, allora diresti che il risultato è **statisticamente significativo al livello 0.05**.
- “Sotto l’ipotesi nulla, osservare una differenza di almeno 0.5 è abbastanza raro, circa il 3.7% delle volte.”

---

### Due esercizi finali misti

**29. Dal dato alla Beta**  
Un farmaco viene dato a 8 pazienti e 6 guariscono.  
Assumendo prior uniforme:
- scrivi la posterior Beta
- calcola la sua media
- spiega perché questa media non è esattamente (6/8).

- prior uniforme =Beta(1,1)
- dopo aver osservato h successi e t fallimenti, la posterior diventa
	- $X∼Beta(h+1,t+1) = Beta(7,3)$

- media di beta 
	- $E[X] = \frac{a}{a+b} = \frac7{7+3} = 0.7$

- perchè non 6/8
	- Però noi non stiamo usando semplicemente la frequenza osservata come stima puntuale: stiamo usando una **posterior Beta**, cioè una distribuzione che rappresenta la nostra incertezza sulla vera probabilità di guarigione.
	- Con prior uniforme, dopo 6 successi e 2 fallimenti otteniamo $\text{Beta}(7,3)$, e la **media** di questa distribuzione è 0.7
	- Questa differenza nasce dal fatto che la posterior non è un singolo numero ma una **distribuzione**: media e valore più plausibile non devono coincidere.




**30. Dal campione all’incertezza**  
Hai un campione IID di (n=64) osservazioni con varianza campionaria (S^2=16).  
Calcola lo standard error della media campionaria.  
Poi spiega cosa dice questo numero sulla precisione di $(\bar X)$.
$$
SE(\bar X) \sim \sqrt{\frac{S^2}n} = \frac{S}{\sqrt{n}}
= \sqrt{\frac{16}{64}} = 1/2 = 0.5
$$

Questo numero misura **quanto è precisa la media campionaria** come stima della media vera.  
Dire che lo standard error è **0.5** vuol dire che, se ripetessimo molte volte il campionamento con n=64, la media campionaria $\bar X$ tenderebbe a oscillare attorno alla media vera con una dispersione di circa **0.5** unità. Più lo standard error è piccolo, più la stima è precisa.

Lo standard error della media campionaria è 0.5, quindi la stima $\bar X$ ha un’incertezza relativamente contenuta: la media campionaria è abbastanza precisa come stima della media della popolazione.

