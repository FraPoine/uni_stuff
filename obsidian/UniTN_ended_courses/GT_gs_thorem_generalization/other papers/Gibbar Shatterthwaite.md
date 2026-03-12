Il **Teorema di Gibbard-Satterthwaite** è un risultato fondamentale nel campo delle elezioni e della teoria della scelta sociale. In sintesi, dice che, in determinate condizioni, **non è possibile avere un sistema di voto (una "regola di voto" o "procedura di scelta sociale") che sia allo stesso tempo "perfetto" e immune alla "manipolazione"**.

Vediamo le condizioni e cosa significa "manipolazione":

1. **Condizione sui candidati:** Ci devono essere **almeno tre candidati** tra cui scegliere. Se ce ne sono solo due, la situazione è diversa.
2. **Condizione sulla regola di voto:**
    - Deve essere **"onto"**: questo significa che ogni candidato può _potenzialmente_ vincere l'elezione, a seconda di come votano le persone. Nessun candidato è escluso a priori dalla possibilità di vincere.
    - Deve essere **"non-dittatoriale"**: questo significa che **nessun singolo elettore ha il potere assoluto** di determinare il vincitore indipendentemente da come votano tutti gli altri. Le preferenze di un singolo individuo non possono da sole stabilire il risultato finale.

**Cosa implica il teorema?**

Se una regola di voto soddisfa queste condizioni (almeno 3 candidati, è onto e non-dittatoriale), allora il teorema GS ci dice che **esisterà sempre almeno una situazione** (cioè, un insieme di voti da parte degli elettori, chiamato "profilo di preferenze") in cui **un elettore ha un incentivo a non votare secondo le sue vere preferenze**.

Questo agire in modo non sincero è la **"manipolazione"**. Un elettore "manipola" quando decide di non presentare la sua vera classifica dei candidati, ma ne presenta un'altra diversa, con l'obiettivo di ottenere un risultato finale che preferisce.

Il teorema garantisce che, per qualsiasi regola di voto che rispetta le condizioni, ci sarà _qualche_ scenario in cui la manipolazione è possibile e vantaggiosa per l'elettore che la mette in atto. Implica "l'ubiquità dei manipolatori".

**Esempio Semplice (Questo esempio non è presente direttamente nel testo delle fonti fornite, ma lo costruisco per illustrare il concetto del teorema):**

Immagina un'elezione con 3 candidati: Aldo (A), Bruno (B), e Carlo (C). Usiamo la regola di voto della **Pluralità** (vince chi prende più voti di "primo posto"). Questa regola è menzionata nelle fonti. Supponiamo ci siano 3 elettori con le seguenti preferenze **veritiere**:

- **Elettore 1:** A è il migliore, poi B, poi C (A > B > C)
- **Elettore 2:** C è il migliore, poi A, poi B (C > A > B)
- **Elettore 3:** B è il migliore, poi C, poi A (B > C > A)

Se tutti votano onestamente (cioè, indicano il loro candidato preferito come primo):

- Elettore 1 vota per A (primo posto)
- Elettore 2 vota per C (primo posto)
- Elettore 3 vota per B (primo posto)

Risultato: A prende 1 voto, B prende 1 voto, C prende 1 voto. C'è una parità. Per semplicità, ipotizziamo una regola di spareggio alfabetico A > B > C (la gestione dei pareggi è un tema complesso non esplicitamente coperto in dettaglio per l'esempio dal testo, che però ne parla in altri contesti). In questo caso, **Aldo (A) vince**.

Ora, consideriamo l'Elettore 2. La sua vera preferenza è C > A > B. Il vincitore attuale è A, che per l'Elettore 2 è la sua seconda scelta. Lui preferirebbe C, ma anche B sarebbe peggio di A secondo la sua vera preferenza. Tuttavia, l'Elettore 2 vede che il suo candidato preferito (C) non vince. Potrebbe cercare di manipolare?

Supponiamo che l'Elettore 2 menta sulla sua preferenza e metta A al primo posto invece di C. La sua preferenza votata (non veritiera) diventa A > C > B, mentre gli altri votano onestamente:

- Elettore 1 vota per A (veritiero)
- **Elettore 2 vota per A (manipolato)**
- Elettore 3 vota per B (veritiero)

Risultato: A prende 2 voti, B prende 1 voto, C prende 0 voti. **Aldo (A) vince** di nuovo. Questo tentativo di manipolazione non ha cambiato il risultato finale, che rimane A, e l'Elettore 2 non ha ottenuto un risultato migliore (voleva C, o A andava bene come seconda scelta, ma non ha migliorato nulla).

Proviamo un'altra manipolazione per l'Elettore 2. E se votasse per B (la sua ultima scelta) per provare a impedire la vittoria di A e magari far vincere C (la sua prima scelta), o almeno la sua seconda scelta (A)? No, votare per B farebbe vincere A ancora più facilmente se Elettore 3 vota B.

Troviamo un esempio migliore:

- Elettore 1: A > B > C
- Elettore 2: C > B > A
- Elettore 3: B > C > A

Voto sincero: A (1), C (1), B (1). Spareggio A>B>C: **A vince**. L'Elettore 2 preferisce C > B > A. Il vincitore è A, la sua ultima scelta. Se l'Elettore 2 vota B (la sua seconda scelta) invece di C:

- Elettore 1: A > B > C (sincero)
- **Elettore 2: B > C > A (manipolato)**
- Elettore 3: B > C > A (sincero)

Voto: A (1), B (2), C (0). **Bruno (B) vince**. L'Elettore 2 preferiva B (nuovo risultato) alla sua ultima scelta A (vecchio risultato). **Ha migliorato il risultato per sé stesso mentendo sul suo voto**. Questa è manipolazione.

L'esempio mostra che per la Pluralità (una regola onto e non-dittatoriale con 3 candidati), esiste almeno una situazione specifica (il secondo "profilo di preferenze" che ho inventato) in cui un elettore può manipolare il risultato a proprio vantaggio.

Il Teorema di Gibbard-Satterthwaite non dice che la manipolazione è _sempre_ possibile per _tutti_ gli elettori in _ogni_ situazione. Dice che per qualsiasi regola di voto con quelle proprietà (almeno 3 candidati, onto, non-dittatoriale), **esiste almeno una situazione in cui la manipolazione è possibile per almeno un elettore**. In altre parole, non esiste una regola di voto "perfetta" che sia immune alla manipolazione in tutti gli scenari possibili.

Le fonti indicano che il lavoro presentato nel documento si basa su questo teorema e studia specificamente l'interazione strategica che si crea quando ci sono **più elettori che _potrebbero_ manipolare** (i "GS-manipulators") in un'elezione.


## **Cerchiamo di capirci qualcosa**

