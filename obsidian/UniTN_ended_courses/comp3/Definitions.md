### 1. Computable
 A language L is **computable** (or finite) if:
There exists a Turing machine M such that:
- For every input string w, M **halts** and:     
	- **Accepts** w if w ∈ L
	- **Rejects** w if w ∉ L
---
### 2. Language 
**language** is simply a **set of strings** over some finite alphabet.

---
### 3. Deterministic Turing Machine
A **Deterministic Turing Machine** is a theoretical model of computation where:
- **At any point**, given the current **state** and the **symbol under the tape head**,  
there is **exactly one** action the machine can take:
- Write a symbol on the tape (possibly the same as before)
- Move the tape head **left** or **right**
- Go to a **new state**
---
### 4. Recursive (or computable)
A ***language L*** over an alphabet Σ is **recursive** (also called **decidable** or **computable**) if:
There exists a Turing machine M such that for every string w∈Σ*:
- M **halts** in a finite number of steps, and
- **Accepts** w if w ∈ L
- **Rejects** w if w ∉ L

A ***property P*** is **recursive** if the set of all objects having P is a **recursive set** — meaning:
There exists a Turing machine that **halts on all inputs** and:
- Accepts if the object has property P
- Rejects if the object does not have property P
---
### 5. Recursively enumerable 
A language (or set) is **recursively enumerable** if there exists a **Turing machine** that will:
- **Accept** any string that belongs to the language (i.e., halt and say "yes"),
- But may **not halt** (i.e., loop forever) on strings **not** in the language.
---
### 6. Busy Beaver
Among all TMs on alphabet {0, 1} and with n = |Q| states (not counting the halting one) that halt when run on an empty (i.e., all-zero) tape:
- let Σ(n) be the largest number of (not necessarily consecutive) ones left by any machine upon halting
- let S(n) be the largest number of steps performed by any such machine before halting
Function Σ(n) is known as the ***busy beaver*** function for n states, and the machine that achieves it is called the Busy Beaver for n states.

Both functions grow very rapidly with n, and their values are only known for n ≤ 5. The current Busy Beaver candidate with n = 6 states writes more than 10 ↑↑ 15 ones before halting after more than 10 ↑↑ 15 step.

The function S(n) is not computable.
**Proof**
- Suppose that S(n) is computable. 
- Then, we could create a TM to compute HALTε (the variant with empty input) on a machine encoded in string s as follows:
- on input s
	- count the number n of states of Ms 
	- compute l <-- S(n)
	- emulate Ms for at most l steps
	- if the emulation halts before l steps
		- then Ms clearly halts: accept and halt
		- else Ms takes longer than the BB: reject and halt

---
 ### 7. pigeonhole principle

 Se metti più oggetti che contenitori, allora almeno un contenitore deve contenere almeno due oggetti.
 
---
### 8. UTM  (Universal Turing machine)
 It is possible to envision a TM U that takes another TM M as input on its tape, properly encoded, together with an input string s for M, and simulates M step by step on input s. Such machine is called a Universal Turing machine (UTM).

---
### 9. The Church-Turing thesis
*Turing machines are at least as powerful as every physically realizable model of computation.*

---
### 10. UC (uncomputable function)
Given an alphabet Σ and an encoding α 7 → Mα of TMs in that alphabet, the function
- UC(a)=
	- 0 if Ma(a) = 1
	- 1 otherwise 
	- ∀ a ∈  Σ*
Is uncomputable

**Proof**
- Let M be any TM
- and let m ∈ Σ* be its encoding 
	- (i.e., M = Mm)
- By definition, UC(m) differs from M(m)
	- the former outputs 1 if and only if the latter outputs anything else, or does not terminate

---
### 11. halting problem
Given an alphabet Σ and a encoding α → Mα of TMs in that alphabet, the function:
- HALT(s,t) = 
	- 0 if Ms(t) = ∞
	- 1 otherwise
		- ∀(s,t) ∈ Σ* X Σ*
*(i.e., which returns 1 if and only if machine Ms halts on input t) is uncomputable.*

**Proof**
Lets proceed by contradiction
- Suppose that we have a machine H which compute HALTS(s,t)
- Then we could use H to compute function UC
- For convenience, let us compute UC using a machine with two tapes.
	- The first one is read-only and contains the input string a ∈  Σ*, 
	- while the second will be used as a work tape.
- To compute UC the machine will perform the following steps
	1. create two copies of the input string a onto the work tape, separated by a blank
	2. Execute H (which exists by hypothesis) on the work tape, therefore calculating whether the computation Ma(a) would terminate or not.
		- If the output of H is 0, than we know that the computation of Ma(a) wouldn't terminate, therefore, by definition of function UC, we can output 1 and terminate
		- if the output of H is 1, then we know for sure that the computation Ma(a) would terminate, and we can emulate it with a UTM U, and inverting the result using UC, with the following steps
			1. As in the first step, create two copies of the input string a onto the work tape, separated by blank
			2. execute the UTM U on the work tape, therby emulating the computation Ma(a)
			3. At the end, if the output of the emulation was 1, then replace it by a 0, 
				- if it was something different replace it with 1
- this machine would be able to compute UC by simply applying its definition, but we know that UC is not computable by a TM
- all steps, apart from H, are already known and computable
- *we must conclude that H cannot exists*

---
### 12. Semantic and Trivial
A property is **semantic** if its value is shared by all TMs recognizing the same language:
- if L(M) = L(M′ ), then P (M) = P (M′ ).

We define a property as **trivial** if all TMs have it, or if no TM has it


---
### 13. Rice's Theorem
***All non-trivial semantic properties of TMs are undecidable.***

**Proof**
Let’s work by contradiction via reduction from the *Halting Problem*
- Suppose that a non-trivial semantic property P is decidable;
- this means that there is a TM Mp that can be run on the encoding of any TM M and returns 1 if M has property P, 0 otherwise.
- Let us assume that the empty language ∅ does not have the property P
- Given the strings s,t  ∈  Σ*, we can then check whether Ms(t) halts by building the following auxiliary TM N' that, on input u, work as follows:
	1. move the input u onto an auxiliary tape for later use, and replace it with t
	2. execute Ms on input t
	3. when the simulation halts (which, as we know, might not happen), restore the original input u on the tape by copying it back from the auxiliary tape
	4. run N on the original input u
- The machine N' we just defined accepts the same language as N if Ms(t) halts, otherwise it runs forever, therefore accepting the empty language.
- Running on hypothetical decision procedure Mp on machine N' we obtain
	- yes if Ms(t) halts --> since in this case L(N ) = L(N ′)) 
	- no if doesn't halts --> (and thus the empty language, which doesn’t have the property P , is recognized.)

---
14. Savitch's Theorem
15. Kolmogorov complexity
16. smallest UTM
17. Why introduce non-deterministic Turing machines, if they are not practical computational models?
18. Why do we require reductions to carry out in polynomial time?
19. Reduction
20. Polinomial time
---
### 21. P
- ***P =U DTIME (n^k)*** 
	- with k form 0 to ∞
- in other words, we say that a language L ∈ Σ* is polynomial-time write L ∈ P, if there are a machine M and a polynomial p(n) such that for every input string x
	- x ∈ L  <==> M(x) = 1 ∧ tM(x) ≤ p(|x|)

---
### 22. NP
- we say that a language L ⊆ Σ* is of class NP, and write L ∈ NP, if there is a TM M and two polynomials p(n) and q(n) such that for every input string x
	- x ∈ L <==>  ∃c ∈ Σ^{q(|x|)} : M(x, c) = 1 ∧ tM(x, c) ≤ p(|x|).
- Basically, the two polynomials are needed to bound both the size of certificate c and the execution time of M.
- **NP-hard**:
	-  A language L is said to be NP-hard if for every language L′ ∈ NP we have that L′ ≤p L.
- **NP-complete**:
	- A language L ∈ NP that is NP-hard is said to be NP-complete
---
### 23. coNP
The **symmetric** class to **NP** is called **coNP**: the class of languages that have a polynomially verifiable certificate for strings that do not belong to the language. 
- coNP = {L ⊆ Σ∗ : L̄ ∈ NP}

---
24. CONNECTED
25. PRIME 
---
### 26. SATISFIABILITY or SAT
Given a Boolean expression f (x1 , . . . , xn ) (usually in conjunctive
normal form, CNF ) involving n variables, is there a truth assignment to the variables that satisfies (i.e., makes true) the formula ?

---
### 27. CNF-SAT
- Given a Boolean expression f (x1, . . . , xn) (usually in conjunctive normal form, CNF3) involving n variables, is there a truth assignment to the variables that satisfies (i.e., makes true) the formula4?

---
### 28. 3-SAT

**Lets start from k-CNF**
- (k-CNF). If all clauses of a CNF formula have at most k literals in them, then we say that the formula is k-CNF (conjunctive normal form with k-literal clauses)
- Given k ∈ N, the language k-SAT is the set of all (encodings of ) satisfiable k − CNF formulas.
- Given k ∈ N
	- k-SAT ≤p SAT.
- SAT ≤p 3-SAT
- 3-SAT is NP-complete.

---
### 29. CLIQUE
- Given an encoding of graph G and a number k, does G contain k nodes that are all connected to each other?
- If G ∈ CLIQUE, then there is a list of k interconnected nodes; given that list, we could easily verify that G contains all edges between them. The list contains k integers from 1 to the number of nodes in G (which is polynomial with respect to the size of G’s representation) and requires a presumably quadratic or cubic time to be checked

---
### 30. VERTEX COVER
- Given an undirected graph G = (V, E) and an integer k ∈ N, is there a vertex subset V ′ ⊆ V of size (at most) k such that every edge in E has at least one endpoint in V ′?
- VERTEX COVER is NP-complete.

---
### 31. TRAVELING SALESMAN PROBLEM TSP
- Given a complete, undirected graph G = (V, E), with numeric costs associated to edges (c : E → N) and a budget k, is there a Hamiltonian cycle in G with overall cost not greater than k?
***TSP is NP-complete***
**Proof**
- We already know that TSP ∈ NP.
- To prove completeness, let us reduce HAMILTONIAN CYCLE to TSP. 
- Given the undirected graph G = (V, E), let us assign cost 1 to all its edges, then complete it adding all missing edges with cost 2.
- Clearly the original graph G has a Hamiltonian cycle if and only if the complete version has an Hamiltonian cycle with cost |V|

---
### 32. INDSET
- Given an encoding of graph G and a number k, does G contain k nodes that are all disconnected from each other8?

---
33. INTEGRAL LINEAR PROGRAMMIN (ILP)
---
### 34. VERTEX COLORING
Given an undirected graph G = (V, E) and an integer k ∈ N, is there an assignment from V to {1, . . . , k} (“k colors”) such that two connected vertices have different colors?

***VERTEX COLORING is NP-complete.***

**Proof**
Lets start from a 3-CNF formula f and build a graph that is 3 colorable if and only if f is satisfiable 

- I will need some separate *gadgets* that capture the semantics of a 3-CNF formula 
- the first *gadget* will be a triangle, with, on the three vertex, T true, F false, B base.
	- Among the three colors, the one that will be assigned to node T will be considered to correspond to assigning the value true to a node.
		- same for F
	- the three nodes are used to force specific values upon other nodes of the graph
- the second set of gadget is meant to assign a node to every literal in the formula
	- for every variable xi, there will be two nodes: xi and ¬xi
	- since we are interested to assigning them truth values xi, er connect all of them to node B, so that they are forved to assume either the *true* or the *false* **color**.
	- Furthermore, we connect node xi and ¬xi to force them to take different colors.
- Next, every 3-literal clause is represented by an OR gadget, whose exit node is forced to have color true by being connected to B and to F.
- the three entry nodes of the gadget is 3-colorable if and only if at least one of the literal nodes it is connected to is not false colored.
- By construction, if f is a satisfiable 3-CNF formula, then is possible to color the literl nodes so that every OR gadget has at least one true-colored node at its input and therefore the graph will be colorable.
- if otherwise, f is not satisfiable then every coloring of the literal nodes will result in an OR gadget connected to three false-colored literals, and therefore will not be colorable 

#### 3-VERTEX COLORING 

---
35. SET COVER
36. TAUTOLOGY
---
### 37. DTIME
Let f: N --> N be any computable function. 
we say that a language L ⊆ Σ* is of class DTIME(f), and write L ∈ DTIME(f) if there is a TM M that decides L and its worst-case time, as a function of input size, is dominated by f:
- L ∈ DTIME(f) <==> ∃M : L(M) = L ∧ TM = O(f ).

In other words, DTIME(f) is the class of all languafes that can be decided by some TM in time eventually bounded by function c\*f, where c is constant.

Saying L ∈ DTIME(f) means that is a machine M, a constant c ∈ N and an input size n0 ∈ N such that, for every input x with size larger than n0, M decides x ∈ L at most c \* f(|x|) steps.

---
38. NTIME
39. EXP
40. NEXP
---
### 41. L
- **L = DSPACE(log n)** 
- *is the class of languages that are decidable by a deterministic TM using logarithmic read-write space;*

---
### 42. NL
- NL = NSPACE(log n)
- is the class of languages that are decidable by a TM (deterministic or not) using logarithmic read-write space;

---
43. CONNECTIVITY (or ST-CONNECTIVITY, or STCON)
---
### 44. NSPACE
- Given a computable function 
	- f : N → N, L ∈ NSPACE(f (n))
- *if there is a multi-tape non-deterministic TM N , with a read-only input tape, such that N decides x ∈ L by using O(f (|x|)) cells in the read/write tape(s).*

---
### 45. DSPACE
- Given a computable function 
	- f : N → N, **DSPACE(f (n))** 
- *is the class of languages L that are decidable in space bounded by O(f (|x|)); where n is the size of the input; i.e., **L ∈ DSPACE(f (n))** if there is a multi-tape TM M, with a read-only input tape, such that M decides x ∈ L by using O(f (|x|)) cells in the read/write tape(s).*

---
### 46. PSPACE
- PSPACE = U DSPACE(n^c) --> with c from 0 to ∞

è la classe di complessità dei problemi **decidibili da una macchina di Turing deterministica usando una quantità di memoria (spazio) polinomiale rispetto alla dimensione dell’input**.

Un linguaggio L⊆{0,1}\* appartiene a PSPACE se esiste una macchina di Turing deterministica M e un polinomio p(n) tali che, per ogni input x∈{0,1}\*:
1. M accetta x se e solo se x∈L.
2. Durante qualsiasi esecuzione, M usa al massimo p(∣x∣) celle di nastro.

Simbolicamente:
PSPACE=⋃ DSPACE(n^k) --> k≥1
dove DSPACE(f(n)) indica i problemi risolvibili in **spazio deterministico** O(f(n)).

---
### 47. NPSPACE
- NPSPACE = U NSPACE(n^c) --> with c from 0 to ∞
---
### 48. SUBSET SUM
- Let w1, w2, . . . , wn ∈ N, and let s ∈ N. The problem asks if there is a subset I ⊆ {1, . . . , n} such that
	- Σ wi = s --> i ∈ I, but a partition of the graph into
- Or, equivalently, is there a subset of indices 1 ≤ i1 < i2 < · · · < ik ≤ n such that 
	-  Σ wij = s -->j=1 till k
- Or, again, is there an n-bit string (b1, b2, . . . , bn) ∈ {0, 1}^n such that 
	- Σi biwi = s?

***SUBSET SUM is NP-complete***
- 

---
49. KNAPSACK
50. Language in NP
---
### 51. naïf algorithm
With **naïf algorithm** (or “naive algorithm”) doesn’t refer to a single specific algorithm, but rather to a **simple and straightforward approach** to solving a problem, without optimizations or advanced strategies. It’s often used as a starting point to understand the problem before moving on to more efficient versions.



---
### 52. PCP Post Correspondence Problem
- Given two sets of n strings, {A1, . . . , An} ⊂ Σ∗ and {B1, . . . , Bn} ⊂ Σ∗, is it possible to find a finite sequence of k indices 1 ≤ i1, . . . , ik ≤ n (in no particular order and possibly with repetitions) such that Ai1 Ai2 · · · Aik = Bi1 Bi2 · · · Bik ?

---
### 53. MPCP
- In the same conditons of PCP, we furthermore require that the first chosen index is i1 = 1 (i.e., pair 1 is initially laid out).

---
### 54. HAMILTONIAN PATH

*Given a directed graph G = (V, E), a path in G is called **Hamiltonian** if it touches every node in V exactly once.*

HAMILTONIAN PATH problem
- *Given a directed graph G = (V, E) and two distinct nodes s, t ∈ V , is there a **Hamiltonian path** in G starting from s and ending in t?*

HAMILTONIAN PATH is NP-complete
**Proof**
- Clearly, HAMILTONIAN PATH ∈ NP: a certificate is the path itself, expressed ad a list on nodes, which can be easily checked for the desired properties:
	- s is the first node
	- t is the last node
	- every node in V appears exactly once, 
	- two consecutive nodes are connected by an edge in the correct direction.

Let us consider a reduction form **SAT**
- given a generic CNF expression, let us create a graph that has an Hamiltonian path between two specified nodes if and only if the expression is satisfiable.
- Let f be a CNF expression on n variables x1...xn, organized as the conjunction of n disjunctive clauses C1,..,Cm.

#### *Directed Hamiltonian cycles*

Given a directed graph G = (V, E) a Hamiltonian cycle in G is a closed path (i.e., the initial node is also the final one) where every node in V is visited exactly once (clearly, the first and last step, starting and ending at the same node, count as one visit).

DIRECTED HAMILTONIAN CYCLE
- Given a directed graph G = (V, E), does G have a Hamiltonian cycle?

DIRECTED HAMILTONIAN CYCLE is NP-complete.

#### *Undirected Hamiltonian cycles*

- Given an undirected graph G = (V, E), does G have a Hamiltonian cycle?
- HAMILTONIAN CYCLE is NP-complete.

---
### 55. Cook’s Theorem
- SAT is NP-hard.
- corollary
	- SAT is NP-complete
---
### 56. Savitch’s theorem
- Given a function f (n), 
	- NSPACE( f(n)) ⊆ DSPACE( f(n)^2).

Cioè: **tutto ciò che si può fare con una macchina di Turing non deterministica usando s(n) celle di memoria, si può fare con una macchina deterministica usando al massimo s(n)^2 celle**.

---
### Kolmogorov complexity
- Given a UTM U and a string x, we define its Kolmogorov complexity KU (x) to be the size of its smallest description in U:
	- KU (x) = min{|(s, t)| : U(s, t) = x}

- Given two UTMs U and V, there is a constant value cUV such that, for every x:
	- |KU (x) − KV (x)| ≤ cUV 
- Note that the constant is independent of the specific string x
**Proof**




- Given the UTM U, the function KU : Σ\* → N is uncomputable.