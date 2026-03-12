Tweak the proof of Exercise 7 in order to reduce VERTEX COVER (in place of INDEPENDENT SET) to ILP. 
Hint — We need to transform the condition “every edge has at most one endpoint in the set”, used in the aforementioned theorem, into the condition “every edge has at least one endpoint in the set”; the condition “there must be at least k 1’s” must become “there must be at most k 1’s”.


---
### VERTEX COVER
Given an undirected graph G = (V, E) and an integer k ∈ N, is there a vertex subset V ′ ⊆ V of size (at most) k such that every edge in E has at least one endpoint in V ′ ?

---
Just as a reminder 

INDSET to ILP

I need to start with the elements
- Graph G = (V,E)
- integer K ∈ N

I have to put some condition on the INDSET
- I need for every nodes to have a value x = {0, 1}
- x must be >= 0
- x must be <= 1
- if a node is in the indset the vertex value became 1
- 0 otherwise 
- I also need that the sum of the value of two connected nodes never exceed 1 so:
	- xi + xj <= 1 with i,j ∈ E
- In last I need to have at least k element in the indset 
	- x1 + x2 + ... + xk >= k

So my ILP became
- -xi <= 0 --> ∀i ∈ V
- xi <= 1 --> ∀i ∈ V
- xi + xj <= 1 --> ∀i,j ∈ E
- - x1 - x2 - ... - xk <= -k


---
### And now VERTEX COVER

lets star with the same method
- graph G = (V, E)
- integer k ∈ N

what did i need
- integer x ∈ N assigned to every node 
- x must be greater or equal than 0 and lower or equal than 1
- I need for every arc to be connected with at least a vertex whose x is equal to 1
	- xi + xj >= 1 with i,j ∈ E
- and I also need at most k element in my vertex cover
- x1 + x2 + ... + xk <= k

**my ILP became**
- -xi <= 0  --> ∀i ∈ V
- xi <= 1  --> ∀i ∈ V
- -xi - xj <= -1 with i,j ∈ E
- x1 + x2 + ... + xk <= k
