# intro
- presentazione del titolo dle paper e degli autori
- magari dico anche un pochino di cosa parla

"Buongiorno a tutti. Oggi vi parlerò di un paper fondamentale per la teoria della scelta sociale, pubblicato da Duggan e Schwartz nel 2000.  
Questo lavoro rappresenta una generalizzazione importante del celebre teorema di Gibbard-Satterthwaite, in quanto ne estende la portata a regole che **ammettono pareggi** e **non richiedono credenze condivise** tra i votanti.  
Vedremo insieme come gli autori riescano a ottenere un risultato di impossibilità estremamente generale, senza appoggiarsi a ipotesi forti come risolutezza o razionalità probabilistica."

# contesto 
- richiamo al gibbard-Satterthwaite
- teorema cosa dice il teorema in breve e quali sono le premesse

Il punto di partenza è il celebre teorema di Gibbard-Satterthwaite. Esso stabilisce che, se si vogliono rispettare la non-dittatorialità e il dominio di ogni preferenza possibile, allora qualsiasi regola di scelta sarà vulnerabile alla manipolazione.  
Ma GS fa delle ipotesi forti: assume che la funzione sia _resolute_, ovvero che produca un solo vincitore anche in caso di pareggio, e che gli agenti abbiano credenze condivise sul meccanismo di tie-breaking.  
Duggan e Schwartz si chiedono: cosa succede se rimuoviamo queste due ipotesi?


# obbiettivo del paper
- Gli autori di questa fonte si propongono di estendere questo risultato eliminando l'assunzione di risolutezza (permettendo pareggi o set di scelta con più membri) e, cosa ancora più importante, senza assumere che gli individui abbiano credenze condivise su come questi pareggi o incertezze vengano risolti (ad esempio, tramite lotterie percepite allo stesso modo da tutti)

"L’obiettivo degli autori è estendere il teorema di GS.  
In pratica, si pongono in un ambiente più generale e realistico, in cui:
- non si richiede che il meccanismo scelga sempre un singolo vincitore,
- non si impone che gli agenti abbiano credenze condivise su come saranno risolti i pareggi.  
    In questo ambiente, riescono comunque a dimostrare un teorema di impossibilità: qualunque regola non dittatoriale sarà manipolabile, anche con queste ipotesi rilassate."
# teorema effettivo
- teorema 
- condizioni 

# Proof
- a lot of things




# Current version of the presentation
---

## 1. INTRODUCTION

### Slide 1 – Title and Authors

- **Paper Title:**  
    _Strategic Manipulability without Resoluteness or Shared Beliefs_
    
- **Authors:**  
    Joel M. Duggan & Lloyd S. Shapley Schwartz
    
- **Publication Year:**  
    2000
    

#### What to say:

> “Good morning everyone. Today I’ll present a paper by Duggan and Schwartz, published in 2000, which extends one of the foundational results in social choice theory—namely the Gibbard‐Satterthwaite theorem—by removing two key assumptions: resoluteness and shared beliefs. We'll see that even in this more general setting, strategic manipulation remains inevitable.”

---

## 2. GOAL OF THE PAPER

### Slide 2 – Main Goal

- **Starting Point:**  
    The classic Gibbard‐Satterthwaite (GS) theorem says that every non‐dictatorial resolute social choice function is manipulable.
    
- **GS Limitations:**
    
    1. Assumes that the rule always selects a **unique winner** (resoluteness).
        
    2. Assumes agents have **shared beliefs** about tie‐breaking.
        
- **Goal of Duggan & Schwartz:**  
    To show that even **without resoluteness** and **without shared beliefs**, strategic manipulation **still cannot be avoided**, unless one allows dictatorship or other undesirable properties.
    

#### What to say:

> “The authors aim to generalize GS by allowing the rule to return ties and by not assuming agents know how ties will be broken. They prove that manipulation is still inevitable unless we sacrifice key democratic principles.”

---

## 3. G‐S THEOREM RECAP

### Slide 3 – The Gibbard‐Satterthwaite Theorem

- **GS Assumptions:**
    
    1. **Resoluteness:** The social choice function always picks **one** winner.
        
    2. n≥2n \geq 2, ∣A∣≥3|A| \geq 3 alternatives.
        
    3. **Non‐dictatorship:** No single agent always determines the outcome.
        
    4. **Complete preferences:** Agents rank all alternatives.
        
- **Conclusion:**  
    Any rule that satisfies these is **manipulable**: some agent can benefit by lying about their preferences.
    

#### What to say:

> “This is a classical impossibility result: if you want a resolute, non‐dictatorial system, there will always be someone who can benefit from strategic voting.”

---

## 4. USEFUL DEFINITIONS

### Slide 4 – Alternatives, Profiles, and Social Choice

- **Alternatives (A):**  
    Finite set of outcomes (e.g., a, b, c).
    
- **Profile (P):**  
    Collection of all agents’ preference orders:  
    P=(P1,P2,...,Pn)P = (P_1, P_2, ..., P_n)
    
- **Social choice function (C):**  
    A rule C:Profiles→P(A)∖{∅}C: \text{Profiles} \to \mathcal{P}(A) \setminus \{\emptyset\},  
    returning a **nonempty subset** of alternatives (may be a singleton or a tie).
    

#### What to say:

> “Once we fix everyone's preferences, the rule C(P)C(P) gives us the set of winning alternatives.”

---

### Slide 5 – Lotteries and Expected Utility

- **Lottery over X⊆AX \subseteq A:**  
    A probability distribution p∈Δ(X)p \in \Delta(X) (e.g., 50% on a, 50% on b).
    
- **Δ(X)\Delta(X):**  
    The set of all lotteries over X.
    
- **Utility representation:**  
    A function uiu_i is **compatible** with PiP_i if  
    x≻iy⇒ui(x)>ui(y)x \succ_i y \Rightarrow u_i(x) > u_i(y).
    
- **Expected utility:**  
    For p∈Δ(X)p \in \Delta(X),
    
    ui(p)=∑x∈Xp(x) ui(x) u_i(p) = \sum_{x \in X} p(x)\,u_i(x)

#### What to say:

> “When the rule returns a set of winners, agents assess the outcome based on all possible lotteries over that set, using expected utility from some compatible representation.”

---

### Slide 6 – Basic Conditions

- **Citizens’ Sovereignty (CS):**  
    Every alternative can win in some profile.  
    ∀x∈A,  ∃P:x∈C(P)\forall x \in A,\; \exists P: x \in C(P)
    
- **Non‐Dictatorship (D═):**  
    No agent always has their top choice selected, regardless of others.
    
- **Residual Resoluteness (RR):**  
    There exists **some** profile P∗P^* such that C(P∗)={x}C(P^*) = \{x\}.
    

#### What to say:

> “These conditions ensure the rule is democratic (no dictatorship), open (every outcome can win), and at least sometimes resolute.”

---

## 5. THEOREM + CONDITIONS

### Slide 7 – The M═ Condition

- **Definition of M═:**  
    For any agent ii, any profile P=(Pi,P−i)P = (P_i, P_{-i}), and any deviation Pi′P_i',  
    the agent cannot improve **for any compatible utility function** and **any lottery** over the outcomes:
    
    ui(q)≤ui(p),∀ui compatible,  ∀p∈Δ(C(P)),  q∈Δ(C(P′)) u_i(q) \le u_i(p), \quad \forall u_i \text{ compatible},\; \forall p \in \Delta(C(P)),\; q \in \Delta(C(P'))

#### What to say:

> “M═ is a very strong form of strategy‐proofness: the agent can’t improve their expected outcome in **any** way, no matter how they evaluate it.”

---

### Slide 8 – Summary of All 4 Conditions

|**Condition**|**Meaning**|
|---|---|
|**M═**|No agent can benefit by misreporting (under any utility/lottery)|
|**CS**|All alternatives are possible winners|
|**D═**|No agent is a dictator|
|**RR**|Some profile yields a unique winner|

---

### Slide 9 – The Main Theorem

> **Theorem (Duggan & Schwartz, 2000):**  
> If ∣A∣≥3|A| \ge 3, then no social choice function CC satisfies **all** of:
> 
> 1. **M═** (strong strategy‐proofness)
>     
> 2. **CS** (citizens’ sovereignty)
>     
> 3. **D═** (non‐dictatorship)
>     
> 4. **RR** (resoluteness in at least one profile)
>     

---

## 6. GAME PRESENTATION

### Slide 10 – Pizza Club Game

- **Players:** Anna, Beatrice, Carlo
    
- **Alternatives:**
    
    - aa = Margherita
        
    - bb = Diavola
        
    - cc = Vegetarian
        
- **Social choice rule CC:** returns sets of pizzas; if a tie occurs, a pizza is selected at random.
    
- **Sample preferences:**
    
    - Anna: a≻b≻ca \succ b \succ c
        
    - Beatrice: b≻c≻ab \succ c \succ a
        
    - Carlo: b≻a≻cb \succ a \succ c
        

---

## 7. PROOF OF THE THEOREM

### Slide 11 – Construction of the Relation F(P)F(P)

- From C(P)C(P), define a binary relation F(P)F(P) over alternatives.
    
- x F(P) yx\,F(P)\,y: means that society prefers x to y.
    
- Use the M═ condition to derive properties:
    
    - Asymmetry
        
    - Independence of irrelevant alternatives (IIA)
        
    - Unanimity
        
    - Non‐blocker
        
    - Transitivity
        

---

### Slide 12 – Supporting Lemmas

- **M═‐Lemma**: if a better-ranked option disappears or a worse one appears, M═ is violated.
    
- **Topset Lemma**: if a top set of an agent partially appears in C(P)C(P), then all of it must appear.
    
- **Dominance Lemma**: if everyone prefers a to b, b can’t win unless a does too.
    
- **Unanimity, Nonblocker, Transitivity**: together these show that F behaves too rationally.
    

---

### Slide 13 – Contradiction

- The properties of F contradict known impossibility theorems (e.g., Arrow).
    
- So our initial assumption — that CC satisfies all four conditions — must be false.
    
- ⇒ Strategic manipulation is unavoidable.
    

---

## 8. COMPARISON WITH G‐S

### Slide 14 – Comparison Table

|Feature|Gibbard‐Satterthwaite|Duggan & Schwartz|
|---|---|---|
|Output|Single winner|Set of winners allowed|
|Tie-breaking|Assumed known|All lotteries considered|
|Beliefs|Shared beliefs required|No beliefs assumed|
|Utilities|Single known utility|All compatible utilities|
|Strategy|Compare single outcomes|Compare lotteries|

---

## 9. RELAXATIONS

### Slide 15 – Relaxing RR and Beliefs

- **RR** can be **constructed**: just assume a unanimous profile with one preferred alternative.
    
- **Beliefs**: not needed at all — M═ handles all lotteries, even under complete uncertainty.
    

---

### Slide 16 – Relaxing M═ and Countability

- **M═** can be weakened to:
    
    - **Maximin**: avoid worst outcome
        
    - **Maximax**: hope for best outcome
        
- Even then, the impossibility remains.
    
- **Countability of C(P)C(P)**: not required — only finite lotteries matter.
    

---

## 10. CONCLUSION

### Slide 17 – Key Takeaways

- Even without resoluteness and beliefs, strategic manipulation is **inevitable**.
    
- Implication: avoiding manipulation in social choice requires giving up something else — e.g., full sovereignty, non‐dictatorship, or robustness.
    
- Future directions: incomplete preferences, sequential voting, bounded manipulation.
    

---

### Slide 18 – Thank You / Questions

> “I hope this gave you a clear picture of Duggan & Schwartz’s contribution and how it generalizes Gibbard‐Satterthwaite. I’ll be happy to take any questions!”

---

