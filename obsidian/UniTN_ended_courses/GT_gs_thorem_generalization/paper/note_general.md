# theorem 

### Elementi chiave
Vengono definiti gli elementi del modello: 
- n è il numero di individui, 
- A è un insieme di alternative (con |A| ≥ 3), 
- C è la procedura di scelta sociale, una funzione che prende in input 
- un profilo di preferenze (P) e restituisce un 
- sottoinsieme non vuoto e numerabile di A (C(P) ⊆ A).

Un profilo (P) è un elenco ordinato delle preferenze lineari (asimmetriche, transitive, connesse) di ciascun individuo sull'insieme A.

Una variante i-esima di un profilo P è un profilo P' dove solo le preferenze dell'individuo i (P'i) sono cambiate rispetto a P (P'j = Pj per tutti j ≠ i).

Una X-lotteria è una distribuzione di probabilità sugli elementi di un insieme X.

Un rappresentante di una preferenza Pi in un insieme X è una funzione di utilità u che rispetta l'ordinamento di Pi sugli elementi di X (se x è preferito a y secondo Pi, allora l'utilità di x è maggiore dell'utilità di y).

### enunciato
Il teorema afferma che, assumendo che l'insieme di alternative A abbia almeno 3 elementi (|A| ≥ 3) e che la procedura C produca sempre un risultato che è un sottoinsieme non vuoto e numerabile di A (C(P) ⊆ A), allora le seguenti quattro condizioni sono inconsistenti (cioè, non possono essere soddisfatte contemporaneamente da nessuna procedura C):

### Le Quattro Condizioni Inconsistenti

M= (Nonmanipolabilità): Questa è la condizione chiave che generalizza il concetto di non-manipolabilità. Afferma che non esiste alcun profilo P, alcun individuo i, e alcuna variante P' di P (ottenuta cambiando solo la preferenza di i) tali che: per ogni possibile lotteria (l) sul set di risultato originale (C(P)) e per ogni possibile lotteria (l') sul set di risultato modificato (C(P')), esista qualche rappresentante di utilità (u) della vera preferenza di i (Pi) sull'unione dei due set (C(P) ∪ C(P')) tale che l'utilità attesa della lotteria l' sia strettamente maggiore dell'utilità attesa della lotteria l. In termini più semplici, una procedura è manipolabile sotto M= solo se cambiare preferenza porta a un risultato universalmente migliore per l'individuo che manipola, indipendentemente dalle sue precise credenze (rappresentate dalle lotterie) sulla risoluzione dei pareggi, purché queste credenze assegnino probabilità positive solo agli elementi nei set di scelta effettivi. Questa condizione è più debole rispetto alle definizioni di non-manipolabilità in lavori precedenti che assumevano credenze condivise o lotterie specifiche associate ai set di scelta

CS (Sovranità dei Cittadini): Per ogni alternativa x in A, esiste almeno un profilo di preferenze P tale che x è incluso nel set di scelta C(P)

- Questo significa che ogni alternativa è almeno potenzialmente eleggibile. Gli autori notano che questa è una versione più debole rispetto a una condizione che richiederebbe che {x} sia il solo elemento scelto

D= (Non-dittatorialità): Non esiste alcun individuo i tale che, per ogni alternativa x e per ogni profilo P, il set di scelta C(P) sia sempre il singleton {x} se x è l'alternativa preferita da i (se x è "atop Pi")
- In altre parole, nessun individuo può da solo determinare l'unico vincitore imponendo la propria prima scelta. Anche questa è una versione più debole rispetto a una condizione che richiederebbe che x sia semplicemente incluso in C(P) quando è atop Pi

RR (Risolutezza Residua): Questa è una condizione molto specifica di risolutezza. Se le preferenze di tutti gli individui tranne, forse, uno sono le stesse (con x primo e y secondo), e la preferenza dell'individuo rimanente (i) è o uguale a quella degli altri o la stessa ma con x e y scambiati, allora il set di scelta C(P) deve essere un singleton (cioè, contenere un solo elemento)

- Questa condizione impone un minimo livello di risolutezza in circostanze molto specifiche. Gli autori argomentano che un certo grado, seppur minimo, di risolutezza (come imposto da RR) è necessario per evitare che procedure banali (come quella che sceglie sempre l'intero set A) soddisfino le altre condizioni

### contesto e confronto
Il capitolo 2, pur enunciando il teorema, inizia anche a confrontare le condizioni utilizzate con quelle di lavori precedenti. Viene evidenziato come la formulazione di M= sia più debole rispetto ad altre (come quelle di Zeckhauser, Gibbard, Feldman) perché richiede che la manipolazione sia profittevole per ogni lotteria sui set di scelta, non solo per una lotteria specifica o condivisa

Vengono presentate versioni più forti di CS e D+ (CS+ e D+) che potrebbero emergere se si rinunciasse completamente a RR, ma gli autori spiegano perché hanno scelto le versioni più deboli CS e D+ insieme a RR per ottenere il loro risultato

- La scelta di RR è giustificata come il prezzo da pagare per mantenere CS e D+ il più deboli possibile


