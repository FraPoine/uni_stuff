
## **beliefs: Gibbard-Satterthwaite generalized**


Abstract
The Gibbard-Satterthwaite Theorem on the manipulability of social-choice rules assumes resoluteness: there are no ties, no multi-member choice sets.
#### Intro
Social choice
	allow strategic manipulation
	the proftable misrepresentation of someone's preference

The Gibbard-Satterthwaite Theorem (GS) is often said to show that manipulability is inescapable. 

Manipulability is little affected by ties or beliefs about them

Cerchiamo di capire bene cosa dice il teorema
-  riguarda le procedure di scelta sociale che, partendo dalle preferenze degli individui su un insieme di alternative, selezionano un unico vincitore
- Il teorema si applica quando l'insieme di alternative (A) contiene almeno tre elementi (|A| ≥ 3)
- 3 conclusioni (pensavo fossero 4)
	1. Sovranità dei Cittadini (Citizens' Sovereignty - CS): La procedura può selezionare qualsiasi alternativa dall'insieme A.
	2. Non-dittatura (Nondictatorship): Nessun singolo individuo ha il potere di determinare da solo l'esito della scelta sociale per qualsiasi combinazione di preferenze
	3. Risoluzione (Resoluteness): La procedura di scelta sociale seleziona sempre e solo singoli membri di A, non sottoinsiemi. In altre parole, non ammette parità (o "tie")
- La conclusione del Teorema di Gibbard-Satterthwaite è che, sotto queste tre condizioni, la procedura di scelta sociale deve essere manipolabile
- La **Manipolabilità strategica** significa che esiste almeno una situazione (un profilo di preferenze) in cui un individuo può ottenere un risultato che considera migliore (secondo la sua vera preferenza) dichiarando strategicamente una preferenza non veritiera

#### THEOREM
integer n. Denote 1, 2, . . . , n by i
set A, j elements of A by x, y, z, nonempty countable subsets of A by
X,Y.
A profile is an ordered n-tuple of linear orderings of A denoted P = (P1,...,Pn), P'=(P1',...,Pn'), etc.
An i-variant of P is any P' with P'j = Pj for all j != i.
An X-lottery is any λ : X --> (0, 1] with Σ_{x∈X} λ(x) = 1. 
A representative of Pi in X is any u : X-->R with u(x) > u(y)<-->xPiy for all x,y ∈ X.
function C

#### Effective theorem
assuming that mod A is grater equal then 3, and C tourn every P into a nonempty countable C(P) included in A, 4 condition are inconsistent.
	\M --> Nonmanipulability
		for no P, i, and i-variant P' of P is this true: for every C(P')-lottery λ', some representative u of Pi in C(P) U C(P') has Σ_{x∈C(P')} λ'(x)u(x) > Σ_{x∈C(P)} λ(x)u(x) 
	CS --> Citizens' sovereignty
		For all x, some P has x ∈ C(P)
	\D --> Non-dictatorship
		No i is such that, for all x and P, {x} = C(P) if x is a top P_i
	RR --> Residual Resoluteness
		if all P_{j != i} are the same, with x first and y second, and if P_i is either the same as them or else the same but with y first and x second, then C(P) is a singleton

Cosa rappresentano queste condizion
	**non manipolabilità**
		per nessun profilo di preferenze P, nessun individuo i, e nessuna variante P' si verifica quanto segue: per ogni lotteria possibile l sull'insieme di scelta originale C(P) e ogni lotteria possibile l' sull'insieme di scelta risultante dalla manipolazione C(P'), esiste qualche funzione di utilità u che rappresenta la vera preferenza Pi dell'individuo i (definita sull'unione dei due insiemi C(P) ∪ C(P')) tale che l'utilità attesa di l' (basata su C(P')) sia maggiore dell'utilità attesa di l (basata su C(P))
		**In parole più semplici:**
		un cambiamento di preferenza è profittevole (e quindi la procedura è manipolabile) solo se, considerando tutti i modi possibili in cui le incertezze (parità) nei due insiemi di scelta (originale e manipolato) potrebbero risolversi, esiste almeno un modo di interpretare la vera preferenza dell'individuo (tramite utilità) che rende l'insieme manipolato preferibile all'originale
	**Sovranità dei Cittadini**
		richiede che per ogni alternativa x nell'insieme A, esista almeno un profilo di preferenze P tale che x appartenga all'insieme di scelta C(P)
		**Essenzialmente**, afferma che ogni alternativa in A può essere un risultato della procedura di scelta sociale, per qualche combinazione di preferenze
		da distinguere con una versione più forte, vedere più avanti se serve
	**Non-dittatura**
		stabilisce che non esiste nessun individuo i con la proprietà che: per ogni alternativa x e per ogni profilo di preferenze P, l'insieme di scelta C(P) sia esattamente {x} se x è l'alternativa in cima alla preferenza di i (x è "atop Pi")
		**In sostanza**
		nessun singolo individuo ha il potere di determinare da solo il risultato unico della procedura per qualsiasi configurazione di preferenze
		da distinguere con una versione più forte, vedere più avanti se serve
	**Risoluzione Residua**
		forma indebolita dell'assunzione di "risolutezza" (assenza di parità) presente nel teorema GS originale
		afferma che in situazioni molto specifiche, l'insieme di scelta deve essere un singolo elemento
		in particolare, se le preferenze di tutti gli individui tranne uno sono identiche, con un'alternativa x al primo posto e un'alternativa y al secondo posto, e la preferenza dell'individuo restante i è o identica a quella degli altri o identica ma con y al primo posto e x al secondo, allora l'insieme di scelta C(P) deve essere un singleton

La condizione di non malipolabilità regge sul test della manapolabilità, più forte è il test più deboli sono le condizioni???
**e cosa vuol dire questa cosa?**
Un "test di manipolabilità" è il metodo o criterio specifico utilizzato per determinare se una procedura è manipolabile. È il meccanismo che definisce cosa si intende concretamente per "manipolabile"

Il contesto è quello delle procedure di scelta sociale che, a differenza del Teorema di Gibbard-Satterthwaite (GS) originale che assumeva sempre un unico vincitore ("risolutezza"), possono produrre un insieme di alternative scelte (permettendo parità)

Quando l'esito non è un singolo vincitore, definire cosa significhi "manipolare in modo profittevole" diventa complesso

### Test di manipolabilità utilizzato 
1. si considera una situazione P (Profilo di preferenze) in cui un individuo I cambia una sua preferenza, ottenendo un profilo P' che è un profilo variante di I
2. Questo cambiamento fa passare l'insieme delle alternative scelte dalla procedura da C(P) (l'insieme originale) a C(P') (l'insieme dopo il cambio)
3. La fonte considera che l'incertezza (le parità) negli insiemi C(P) e C(P') possa essere risolta tramite lotterie sulle alternative presenti in quegli insiemi. Una lotteria l su un insieme X assegna una probabilità a ciascun elemento di X tale che la somma sia 1.
4. Il test di manipolabilità (quello che, se superato, rende la procedura manipolabile secondo la definizione della fonte) verifica se esiste la possibilità che il nuovo insieme C(P') sia considerato migliore dell'insieme originale C(P) secondo la vera preferenza Pi dell'individuo i.
5. Per fare questo confronto, la fonte usa il concetto di utilità attesa. Si considera una funzione di utilità u che "rappresenta" la vera preferenza Pi dell'individuo su un insieme di alternative (assegna numeri reali alle alternative in modo coerente con Pi). L'utilità attesa di una lotteria è la somma delle utilità di ciascuna alternativa moltiplicata per la sua probabilità nella lotteria.
6. Il test di manipolabilità (quello che fa fallire M=) è superato SE esiste un profilo P, un individuo i, e un profilo P' tali che:
	- Per ogni possibile lotteria l sull'insieme originale C(P)
	- E per ogni possibile lotteria l' sull'insieme manipolato C(P')
	- Esiste qualche funzione di utilità u che rappresenta la vera preferenza Pi dell'individuo
	- Tale che l'utilità attesa di l' (ottenuta dopo la manipolazione) è maggiore dell'utilità attesa di l (ottenuta prima)

Formalmente, nella fonte, questo test (quello che rende la procedura manipolabile e fa fallire M=) è descritto dalla parte successiva ai due punti nella definizione di M=: "for every C(P)-lottery l and every C(P')-lottery l', some representative u of Pi... has ExpectedUtility(l') > ExpectedUtility(l)"

La forza del test si basa su quanto è difficile per una procedura superarlo (cioè, essere dichiarata "manipolabile" secondo quel test)