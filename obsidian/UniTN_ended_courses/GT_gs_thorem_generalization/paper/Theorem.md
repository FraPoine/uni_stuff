Se ci sono almeno 3 alternative (|A| ≥ 3), allora **non esiste** una funzione di scelta sociale (C) che soddisfi **contemporaneamente** le seguenti 4 condizioni:
1. **M═ (Non-manipolabilità):** Nessun individuo può migliorare il risultato **cambiando strategicamente le proprie preferenze**, per **ogni rappresentazione** coerente dei propri gusti (cioè anche se le preferenze non sono descritte da una funzione di utilità unica).
2. **CS (Citizens’ Sovereignty):** Ogni alternativa può essere vincente in qualche profilo.
3. **D═ (Nondittatorietà):** Nessun individuo impone sempre la propria prima scelta.
4. **RR (Residual Resoluteness):** In alcuni casi specifici, il meccanismo sceglie esattamente **una** alternativa (serve per costruire la contraddizione).


OK

# Dimostrazione

## 🎯 **Obiettivo della dimostrazione**

Mostrare che non può esistere una funzione di scelta C che soddisfi **simultaneamente**:

1. **M═**: non-manipolabilità forte (nessuno può migliorare il risultato cambiando preferenze),
2. **CS**: ogni alternativa può vincere,
3. **D═**: nessuno detta sempre il risultato,
4. **RR**: in alcuni profili ben costruiti, il meccanismo è risoluto.

---
### 📘 Il gioco: **Il Club della Pizza**

Tre amici (Anna, Beatrice, Carlo) devono decidere quale pizza ordinare.
Le pizze disponibili sono:
- **Margherita (a)**
- **Peperoni (b)**
- **Vegetarian pizza (c)**

Le regole:
- Il gruppo decide usando una **regola di scelta collettiva** C (che può restituire anche due o tre pizze, cioè pareggi).
- Ogni persona può dichiarare le proprie preferenze in ordine (es. a ≻ b ≻ c).

Il risultato sarà **un insieme** di pizze (es. {a, b}), e poi si tira a sorte quale verrà scelta davvero. 
Ma ogni persona **valuta** questo risultato considerando **tutte le possibili lotterie** sull’insieme.

---
## 🪜 **Passo 1: costruzione della relazione sociale F**

L'idea è: dai risultati della funzione C(P), costruiamo una **relazione F(P)** tra **coppie di alternative** (tipo “a è socialmente preferita a b”).

In pratica:
- Se **ogni rappresentante possibile** delle preferenze individuali compatibili con il profilo P **preferisce ogni lotteria su a a ogni lotteria su b**, allora diciamo che **a F(P) b**.

Nell’esempio:
- Se ogni persona mette **Margherita ≻ Diavola**, e la regola produce solo Margherita o la preferisce in ogni lotteria, allora "a F(P) b".

➡️ F(P) è una **relazione sociale su A × A**.

---
## 🪜 **Passo 2: proprietà di F (derivate da M═)**

Usando il fatto che C soddisfa M═, gli autori dimostrano che F(P) ha **proprietà molto forti**, simili a quelle della relazione sociale in **Arrow**:

| Proprietà                                         | Significato                                                                                  |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Asimmetria (S═)**                               | Se a F(P) b, allora non b F(P) a                                                             |
| **IIA** (indipendenza da alternative irrilevanti) | Se due profili differiscono solo su preferenze per c ≠ a, b, allora F tra a e b resta uguale |
| **Unanimità**                                     | Se tutti preferiscono a ≻ b, allora a F(P) b                                                 |
| **Non-blocco**                                    | Nessun gruppo può sempre impedire che una certa alternativa venga scelta                     |
| **Transitività**                                  | Se a F b e b F c ⇒ a F c                                                                     |

---
## 🪜 **Passo 3: contraddizione**

Gli autori usano un profilo specifico (grazie a **Residual Resoluteness**) per far partire la costruzione di F.

Poi, con vari **lemmi** (Unanimity Lemma, Topset Lemma, Dominance Lemma…), dimostrano che:

- Se C soddisfa M═, CS, D═, RR,
    
- Allora la relazione F(P) ha proprietà che portano a una **contraddizione logica** (come nei teoremi di Arrow).
    

🧨 **Conclusione**: non può esistere tale funzione CCC.  
Quindi, almeno una delle ipotesi M═, CS, D═, RR **deve fallire**.

---
## 🎮 **Traduzione finale nel gioco della pizza**

Immagina che la regola di voto dei tre amici:

- A volte restituisca un pareggio,
- Nessuno sia un dittatore,
- Nessuno possa manipolare il risultato.

Se così fosse, allora la loro scelta collettiva **rispetterebbe sempre** le preferenze collettive come se fosse un decisore razionale perfetto…

⚠️ Ma questo è **matematicamente impossibile**, perché porta a una relazione collettiva **contraddittoria** (come preferire a ≻ b ≻ c ≻ a), nota come **ciclo di Condorcet**.

---

## 🔒 **1. M═-Lemma (Manipolazione bloccata)**

### 🎯 **Cosa dice**:

Se l’individuo ii cambia le preferenze da PiP_i a Pi′P_i', allora:

- **(1)** Nessuna alternativa che peggiora nella sua scala di preferenze può entrare in C(P′) senza esserlo già in C(P);
- **(2)** Nessuna alternativa che migliora può sparire da C(P′) se era in C(P).

### 🍕 **Nel Club della Pizza**:

Anna dice la verità: a≻b≻c, e C(P) = {a, b}.  
Se dichiara Pi′=c≻a≻b, allora **non può ottenere c da sola**, perché sarebbe **peggiorata**.  
E se prima aveva b nel set, **non può perderlo** perché ha solo spostato c in alto (cioè migliorato c).

**➡️ Questo lemma impedisce che Anna "guadagni" cambiando l’ordine delle sue preferenze.**

---

## 🔝 **2. Topset Lemma**

### 🎯 **Cosa dice**:

Se l’insieme delle alternative X⊆AX \subseteq A è il **top set** per qualcuno (cioè tutte le migliori secondo lui), e una è già dentro C(P), allora **tutte** devono essere incluse.

### 🍕 **Nel Club della Pizza**:

Supponiamo Carlo ha preferenze a≻b≻c e dice che il suo top set è {a, b}.  
Se C(P) include a, **deve includere anche b**, altrimenti il meccanismo ignora la parte “alta” delle sue preferenze.

**➡️ Questo forza C(P) a rispettare la “coerenza del top” secondo i votanti.**

---

## 🏆 **3. Dominance Lemma**

### 🎯 **Cosa dice**:

Se a è preferita a b da **tutti**, e b ∈ C(P), allora **a deve essere in C(P)**.

### 🍕 **Nel Club della Pizza**:

Tutti preferiscono Margherita (a) alla Vegetariana (c), ma il set C(P) include c?  
Allora **deve includere anche a**, altrimenti il meccanismo va contro l’unanimità.

**➡️ C serve ad assicurare che nessuna “inferiore” batta una “superiore” a livello collettivo.**

---

## 🚫 **4. 3-Undomination Lemma**

### 🎯 **Cosa dice**:

Nessuna alternativa può **dominare tutte le altre** secondo la relazione F(P).

### 🍕 **Nel Club della Pizza**:

Supponiamo Beatrice vuole sempre Vegetariana (c), e le sue preferenze sono c≻a≻b.  
Ma se **c** è sempre scelta anche se tutti gli altri non la vogliono, allora c **domina** tutte.  
Il lemma dice: **non può esistere un’alternativa così dominante**.

**➡️ Questo protegge il meccanismo dal rischio di "favoritismi permanenti".**

---

## ✅ **5. Unanimity Lemma**

### 🎯 **Cosa dice**:

Se **tutti** preferiscono a ≻ b, allora a F(P) b (cioè socialmente a è meglio di b).

### 🍕 **Nel Club della Pizza**:

Se tutti dicono a ≻ b, allora Margherita deve **essere socialmente preferita** a Diavola.

**➡️ La regola rispetta il principio democratico: se tutti sono d’accordo, si segue la loro opinione.**

---

## 🧱 **6. Nonblocker Lemma**

### 🎯 **Cosa dice**:

Nessun gruppo può **escludere sistematicamente** un’alternativa.

### 🍕 **Nel Club della Pizza**:

Se ogni volta che Carlo **odia** la Diavola (b), questa sparisce da C(P), allora Carlo è un “bloccante”.  
Il lemma dice: **non può esserci un individuo così potente da escludere sempre un’alternativa**.

**➡️ Protegge il pluralismo: tutte le alternative devono poter vincere.**

---

## 🔁 **7. Transitivity Lemma**

### 🎯 **Cosa dice**:

Se a F(P) b e b F(P) c, allora a F(P) c.

### 🍕 **Nel Club della Pizza**:

Se il gruppo preferisce a alla b, e b alla c, allora **deve preferire a alla c**.

**➡️ Questa proprietà logica (tipica della razionalità) è la chiave della contraddizione: se tutte queste regole valgono, si arriva a un ciclo impossibile.**

---

## 🔚 **Conclusione nel contesto del gioco**

Tutti questi lemmi dicono che se il meccanismo:
- evita la manipolazione (M═),
- è aperto e non dittatoriale (CS, D═),
- e coerente in certi casi (RR),


allora **la relazione sociale F che ne deriva è troppo perfetta**, **troppo razionale** → porta a contraddizione (come dire a ≻ b ≻ c ≻ a).

**➡️ Quindi almeno una delle condizioni deve cadere.**



# Relaxations

## 🔧 **Cosa si intende per “relaxation”?**

Significa: **possiamo allentare (rilassare)** alcune delle ipotesi del teorema (come M═, CS, D═, RR), rendendole **meno restrittive**, e **ottenere comunque la stessa conclusione di impossibilità**.

---

## 🔍 **Struttura del capitolo “Relaxations”**

Il capitolo mostra che il teorema principale **continua a valere anche se**:

### 1. 📉 **RR (Residual Resoluteness) è sostituita da un’assunzione tecnica più debole**

> Serve solo a iniziare la costruzione della relazione F(P).

🧠 **Idea:**  
Nel teorema principale, RR serve solo per far sì che **in almeno un caso** il set C(P) abbia un solo elemento.  
Ma possiamo ottenere lo stesso effetto **con una costruzione ad hoc**, **senza assumere RR in modo esplicito**.

📦 **Relaxation:** invece di postulare che esiste un profilo con C(P)={a}C(P) = \{a\}C(P)={a}, possiamo semplicemente **costruirlo** noi.

🍕 **Nel Club della Pizza:**  
Non serve sapere che Margherita è scelta da sola in qualche caso. Basta **costruire un profilo in cui ciò accade**, e usarlo per iniziare la logica della dimostrazione.

✅ Risultato: **non serve RR** come ipotesi autonoma. È “costruibile”.

---

### 2. 🎲 **M═ può essere sostituita da una versione più debole**

#### 💡 Versioni deboli di M═:

- **Maximin-respecting**:  
    L’agente si concentra sulla **peggiore** alternativa nel set C(P)C(P)C(P), e vuole evitarla.  
    ⇒ Non manipola se, anche cambiando preferenze, **la peggiore alternativa possibile non migliora**.
    
- **Maximax-respecting**:  
    L’agente si concentra sulla **migliore** alternativa nel set C(P)C(P)C(P), e spera nel meglio.  
    ⇒ Non manipola se, anche cambiando preferenze, **la migliore alternativa possibile non migliora**.
    

📦 **Relaxation:**  
M═, che è una condizione **fortissima** (nessuna funzione d’utilità compatibile deve guadagnare), può essere **indebolita** a queste due versioni **estremamente semplici**, e **l’impossibilità vale ancora**.

🍕 **Nel Club della Pizza:**  
Se Anna spera solo di evitare la pizza che odia (c) (maximin), oppure spera solo che le capiti quella che ama (a) (maximax), **anche così non può manipolare**. Ma il teorema resta **valido anche in questi casi ridotti**!

✅ Risultato: **basta evitare manipolabilità anche solo da parte di agenti “ottimisti” o “pessimisti”**, e la contraddizione esiste lo stesso.

---

### 3. 🧠 **Nessun bisogno di credenze soggettive (come in Gibbard 1977)**

📦 **Relaxation:**  
A differenza di Gibbard (1977), che assume che gli agenti abbiano **credenze probabilistiche ben definite** sui risultati in caso di pareggio, qui:

- **non si assume alcuna credenza condivisa**,
    
- e neanche alcuna credenza personale!
    

🍕 **Nel Club della Pizza:**  
Anna non ha bisogno di sapere “quanto è probabile che vinca Margherita se c’è pareggio” → **si proteggono tutti i casi possibili**.

✅ Risultato: il teorema vale **senza richiedere conoscenze o assunzioni psicologiche** sugli agenti.

---

### 4. 🔢 **C(P) può essere un insieme anche non numerabile**

> (cioè possiamo rilassare l’ipotesi che il set di vincitori sia numerabile)

📦 **Relaxation:**  
Nella formulazione originale, gli autori assumevano che C(P)C(P)C(P) fosse **numerabile** (cioè contabile), per evitare problemi con l’integrale dell’utilità attesa.

Ma in realtà, nel loro argomento usano solo **lotterie finite**, quindi **non serve davvero l’ipotesi di numerabilità**.

🍕 **Nel Club della Pizza:**  
Anche se il set di vincitori potesse contenere infinite pizze (😵), il ragionamento si applicherebbe **comunque**, perché **consideriamo solo combinazioni finite di preferenze**.

✅ Risultato: la numerabilità non è necessaria.

---

## ✅ **Conclusione del capitolo**

📌 Anche se indeboliamo:

- la non-manipolabilità (M═),
    
- la coerenza parziale (RR),
    
- le assunzioni sulle credenze,
    
- o la struttura tecnica del set dei vincitori,
    

👉 **il teorema continua a valere.**

🔒 **L’impossibilità è estremamente robusta.** Non possiamo evitare la manipolabilità nemmeno in scenari **molto deboli e realistici**.

---

## 🎓 Riassunto slide-friendly

### ✂️ Relaxations – anche con ipotesi più deboli, l’impossibilità regge:

|**Ipotesi**|**Relaxed in...**|**Effetto**|
|---|---|---|
|RR (resolutezza)|Profilo costruito ad hoc|Non serve ipotesi RR globale|
|M═|Maximin / Maximax|Anche agenti ottimisti/pessimisti non possono manipolare|
|Credenze|Nessuna credenza soggettiva|Ancora più generale di Gibbard 1977|
|Numerabilità|Solo lotterie finite bastano|C(P) può anche essere non contabile|
