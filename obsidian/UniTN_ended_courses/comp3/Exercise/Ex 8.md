Consider the SET PACKING problem: given n sets S1, . . . , Sn and an integer k ∈ N, are there k sets Si1 , . . . , Sik that are mutually disjoint? 
1. Prove that SET PACKING ∈ NP. 
2. Prove that SET PACKING is NP-complete. 
- Hint — You can prove the completeness by reduction of INDEPENDENT SET.
---
#### SET PACKING problem
given n sets S1, . . . , Sn and an integer k ∈ N, are there k sets Si1 , . . . , Sik that are mutually disjoint?


***Mutually disjoint***
Un insieme di insiemi {S1,S2,…,Sk} è detto **mutuamente disgiunto** (_mutually disjoint_) se **nessuna coppia** di insiemi ha elementi in comune.


---
##### Prove that SET PACKING ∈ NP. 
how to prove if a problem is NP

A problem is in NP if 
- Esiste un algoritmo che può **verificare** una **soluzione candidata** (chiamata **certificato**) in **tempo polinomiale** rispetto alla dimensione dell’input.
1. PASSO 1: Descrivi l’input
2. PASSO 2: Definisci una "soluzione candidata"
3. PASSO 3: Mostra che la **verifica** può essere fatta in tempo **polinomiale**
	- Un algoritmo ha **tempo polinomiale** se il **numero di passi che esegue** è al massimo:
	- O(n^k)
	- per qualche costante k∈N, dove n è la **dimensione dell'input** (cioè, il numero di bit necessari per rappresentare l'input).

---
#### SET PACKING NP
- we have n sets S1, ..., Sn
- integer k ∈ N 
- there are k mutually disjoints sets 

##### 1 identify the input
- n sets S1, ..., Sn
- k integer ∈ N
##### 2 find a possible solution
- I need a list of k index that identify k sets mutually disjoint
	- (i1, i2, ..., ik)

##### 3 show that is computable in polynomial time
- I need to verify that every couple of sets (Si, Sj), follow this rule Si∩Sj=∅
- I have at max O(k^2) couple of sets
- to verify every element i need O(m) time, where m is the maximum number of element for every sets
- So the time to verify SET PACKING is O(mk^2) that is polynomial.

---
#### SET PACKING NP-Hardness

I need to reduce INDSET to SET PACKING

##### Goal
- show that Set Packing is NP-Hard

1. **Find an instance of SET PACKING**
	- G = (V, E) --> graph
	- we need to know if G have an indset of size k
	- I have n sets S1, ..., Sn 
	- an integer k ∈ N
2. **Transform the instance of SET PACKING in an instance of INDSET**
	- I can build a graph where the sets are the vertex
	- I can connect with arcs only the sets that are not mutually disjoint
	- now i can create an indset with the non connected vertex
	- if the indset have at least k elements the set packing is verified.
- 2.2
	- For every node i ∈ V, consider the set of its edge Si = {{i,j} ∈ E}. Given two vertices i,j ∈ V, the only element that can be shared between the corresponding sets si and sj is a common edge. Therefore, two vertex are disconnected in G if and only the corresponding sets Si and Sj are disjoint. Thus, k mutuially indipendent verices i1, i2, ..., ik, correspond to k mutually disjoint sets Si1, Si2, ..., Sik

# Kiaro