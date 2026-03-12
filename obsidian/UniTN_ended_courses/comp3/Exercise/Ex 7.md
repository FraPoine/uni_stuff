Show that INDEPENDENT SET ≤p INTEGER LINEAR PROGRAMMING by a direct reduction. 

*Hint — Given a graph G = (V, E), and an integer k ∈ N, create an ILP problem with one variable for each vertex, constrained to {0, 1}, and try to come up with constraints that require the chosen vertices to be at least k and not connected to each other*

---
### Indipendent Set

INDEPENDENT SET (or simply INDSET) — Given an encoding of graph G and a number k, does G contain k nodes that are all disconnected from each other8 ?
The problem is almost the same, but we require the vertex subset to have no edges (while CLIQUE requires the subset to have all possible edges). Clearly, INDSET instances can be transformed into equivalent INDSET instances by simply complementing the edge set, which can be attained by negating the graph’s adjacency matrix, which is clearly a polynomial time procedure in the graph’s size (indeed, linear).

---
### CLIQUE
Given an encoding of graph G and a number k, does G contain k nodes that are all
connected to each other

---
### INTEGRAL LINEAR PROGRAMMING (ILP)
Given a set of m linear inequalities with integer coefficients on n integer variables, is there at least a solution? In other terms, given n × m coefficients A_{ij} ∈ Z and m bounds b_i ∈ Z, does the following set of inequalities:
- A11X1 + A12X2 + ... + A1nXn =< b1
- A21X1 + A22X2 + ... + A2nXn =< b2
- ...
- ...
- Am1X1 + Am2X2 + ... + AmnXn =< bm


have a solution with x1 , . . . , xn ∈ Z?

---
#### How to do a reduction
1. **Prendere un’istanza di A**,
2. **Trasformarla in un’istanza di B** in **tempo polinomiale**,
3. **Usare la soluzione di B per ottenere la soluzione di A**,


##### Polynomial time 


---
#### Reduction ILP to IndSet

goal:
- find the proof that ILP is NP-hard

***1 Find an instance of ILP***
- I have a graph G = (V, E)
- an integer k ∈ N

we need to find a set of at least k vertex not connected with each-other

***2 Transform the instance of ILP to a one of IndSet***

for every vertex i ∈ V, i need to introduce a new variable Xi ∈ {0,1} where:
- xi​=1 if the vertex is in the IndSet
- xi = 0 otherwise
- I also need to set boundaries for xi, make it 0=< xi =< 1

I also need to be sure that no vertex in the IndSet can be connected to each other with an arc, so:
- xi + xj  =< 1  

In last I need to have at least k vertexes in my IndSet, so:
- x1 + x2 + ... + xn >= k

***3 my final instance became***

- - xi      <= 0                ∀i ∈ V
- xi        <= 1                 ∀i ∈ V
- xi + xj <= 1                 ∀{i,j} ∈ E
- -x1 - x2 - ... - xn <= -k         at least k vertex