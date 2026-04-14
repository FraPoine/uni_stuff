L’altro PDF è dedicato alla **normal distribution**, che viene presentata come la variabile aleatoria continua più importante. È parametrizzata da media μ\muμ e varianza $\sigma^2$, e si scrive:
$$
X \sim N(μ,\sigma^2)
$$
Il testo sottolinea che la normale compare spesso in natura e che è centrale in probabilità e statistica.

La sua **PDF** è
$$
f_X(x) = \frac{1}{(σ√(2π))} · e^{- \frac{(x - μ)^2}{2σ^2} }
$$
La forma è la classica “campana”. Il picco sta attorno alla media μ, e la larghezza è controllata da σ: più grande è σ, più la curva è larga e schiacciata; più piccolo è σ, più è stretta e appuntita. Inoltre, per definizione,
$$
E[X] = \mu, \space Var(X) = \sigma^2
$$
Per una variabile continua, la probabilità non si legge da una PMF ma dalla **CDF**. Il PDF spiega che per la normale non esiste una forma chiusa semplice dell’integrale della PDF, quindi si usa la funzione della **normale standard**. La CDF viene scritta come
$$
F_X(x) = \Phi(\frac{x - \mu}{\sigma})
$$
dove Φ è la CDF della normale standard.

Il passaggio chiave è la **standardizzazione**:
$$
Z = \frac{X - \mu}{\sigma}
$$
Se $X \sim N(μ,\sigma^2)$, allora $Z \sim N(0,1)$. Questo è fondamentale, perché trasforma qualunque normale in una standard normal, per cui si possono usare tabelle o software. Quasi tutti gli esercizi sulla normale passano da qui.

l PDF mostra anche la regola del circa **68%**: la probabilità che una variabile normale cada entro una deviazione standard dalla media è circa:
$$
P(μ−σ<X<μ+σ)≈0.683.
$$
Questa è una regola molto utile per farsi intuizione sulla dispersione della normale.

Infine, il testo fa vedere come calcolare probabilità pratiche, per esempio P(X>0) oppure P(2<X<5), trasformando tutto in probabilità su Z e poi usando Φ. Mostra anche che in Python, con `scipy`, si può calcolare la CDF direttamente, ricordando però che la libreria usa la **standard deviation** come parametro, non la varianza.