La dimostrazione non mostra un caso specifico di manipolazione, ma piuttosto dimostra che le quattro condizioni elencate sopra non possono logicamente coesistere. Se assumiamo che esistano tutte e quattro, si arriva a una contraddizione. La strategia della dimostrazione è la seguente:

1. Definire una "Preferenza Sociale" Astratta (F): Il teorema introduce una relazione astratta, F(P), che rappresenta una forma di "preferenza sociale" basata sulle scelte di C. xF(P)y significa che x è socialmente preferito a y. Questa relazione è definita in base a quando un singolo elemento (x) viene scelto (C(P') = {x}) in specifici "profili gemelli" (P') che mantengono le preferenze relative tra x e y

2. Derivare Conseguenze dalla Non-manipolabilità (M=) e dalle altre condizioni: Questo è il passo più tecnico e cruciale. La condizione M= (Non-manipolabilità), insieme alle altre condizioni, permette di dedurre proprietà fondamentali sulla funzione C e sulla relazione F.

	- M=-Lemma (Il primo e più importante passo): Questo lemma è il ponte tra la condizione M= e le proprietà successive. In termini semplici, stabilisce che se un'alternativa x viene scelta dopo una manipolazione (cioè, dopo che un individuo i ha cambiato la sua preferenza da Pi a P'i, e x è in C(P')), allora quella stessa alternativa x (o qualcosa che per i è peggio o meglio di x, a seconda del contesto) doveva essere inclusa nell'insieme di scelta originale C(P).
	- Esempio intuitivo del M=-Lemma: Immagina di avere una torta (x) e un biscotto (y). La regola di scelta (C) decide se ti dà un pezzo di torta, un biscotto, o entrambi. Se la regola è non-manipolabile (M=), e tu cambi la tua preferenza in modo che ti venga dato un pezzo di torta (x in C(P')), allora il M=-Lemma implica che, nella situazione originale (prima del cambio di preferenza), dovevi già avere una possibilità di ottenere la torta (x in C(P)) o qualcosa che, dal tuo punto di vista, era paragonabile o meno desiderabile. 
	- Questo è cruciale perché limita quanto il tuo "rapporto" con l'alternativa scelta possa cambiare a seguito di una misrappresentazione.

- **Topset**: Se un sottoinsieme di alternative X è un "top set" (cioè, tutti preferiscono le alternative in X a tutte quelle fuori X), allora C(P) deve essere contenuto in X. In altre parole, la scelta non può includere qualcosa che tutti considerano peggiore di ogni alternativa in X. Questo si dimostra usando il M=-Lemma e la Risolutezza Residua (RR)

- **Dominance**: Se un'alternativa x è l'unica scelta (C(P) = {x}), allora x domina socialmente qualsiasi altra alternativa y (cioè, xF(P)y). Anche questo si dimostra usando il M=-Lemma, Topset e RR

- **Unanimity (U)**: Se tutti preferiscono x a y (xPi y per tutti gli i), allora x socialmente domina y (xF(P)y)

- **Nonblocker (B=)**: Nessun individuo può, tramite la sua preferenza, "bloccare" una dominanza sociale. Questa condizione si basa sulla Non-dittatorialità (D=), M=-Lemma, Topset e RR

- **Transitivity (T)**: Se x domina y e y domina z, allora x deve dominare z

1. Raggiungere una Controddizione: Dopo aver derivato queste proprietà della relazione F (chiamate Asimmetria/S=, Indipendenza dalle Alternative Irrilevanti/IIA, Unanimità/U, Nonblocker/B=, e Transitività/T), il teorema fa riferimento a risultati preesistenti nella teoria della scelta sociale (simili al Teorema di Impossibilità di Arrow) che dimostrano che queste proprietà sono inconsistenti quando ci sono almeno 3 alternative In sintesi, il "trucco" della dimostrazione è questo:
	- Si parte assumendo che esista una procedura di scelta sociale che sia Non-manipolabile e che soddisfi le altre tre condizioni (CS, D=, RR)
	- Da queste quattro assunzioni, si deduce che una "preferenza sociale" astratta (F) deve esibire una serie di proprietà logiche (come unanimità, transitività, non-dittatorialità implicita)
	- Si sa da altri teoremi (come quello di Arrow) che queste proprietà non possono coesistere
	- Poiché abbiamo dedotto una contraddizione dalle nostre assunzioni iniziali, le assunzioni stesse devono essere false.
	- Di conseguenza, le quattro condizioni (M=, CS, D=, RR) non possono essere tutte vere contemporaneamente

Dato che CS (ogni alternativa è eleggibile), D= (nessun dittatore) e RR (una leggera forma di risolutezza) sono considerate condizioni ragionevoli per un sistema di scelta sociale, la conclusione inevitabile è che la Non-manipolabilità (M=) deve essere falsa

Questo significa che la manipolabilità strategica è, in ultima analisi, inevitabile


### **Perché sono inconsistenti?**

- Arrow dimostra che **se (U), (IIA), (P) e (T) valgono**, allora **esiste necessariamente un dittatore** (violando ND).
    
- **L’IIA** è la condizione più controversa: richiede che la scelta tra xx e yy dipenda **solo** da come gli individui ordinano xx e yy, ignorando altre alternative. Ciò elimina meccanismi come i punteggi (es. Borda).
    
- **Transitività** + **IIA** implicano che il sistema deve essere "localmente rigido", ma l’unico modo per garantirlo è concentrare il potere in un singolo individuo (dittatore).
    

### **Esempio** (per l’inconsistenza):

Supponiamo 3 votanti con preferenze:

1. A>B>C
    
2. B>C>A
    
3. C>A>B
    

- Se rispetti **Unanimità**, B>C (perché 1 e 2 preferiscono B a C).
    
- Ma per **IIA**, la scelta tra A e B deve ignorare C. Tuttavia, non esiste un ordine sociale transitivo che soddisfi tutte le coppie senza contraddizioni o dittatura.
    

### **Conclusione**:

Non esiste un sistema "perfetto" che rispetti tutte queste condizioni insieme. Ogni metodo di voto (maggioranza, Borda, etc.) **fallisce almeno un criterio**.