before starting with other complexity classes lets define other things
### DTIME
from the polynomial languages part
- DTIME(f ) is the class of all languages that can be decided by some TM in time eventually bounded by function c · f , where c is constant.
- Saying L ∈ DTIME(f ) means that there is a machine M, a constant c ∈ N and an input size n0 ∈ N such that, for every input x with size larger than n0, M decides x ∈ L in at most c · f (|x|) steps.
### NTIME
We can define the class NTIME(f ) as the NDTM equivalent of class DTIME(f ), just by replacing the TM in with a NDTM

---
## The exponential time classes

It is possible to define classes that are analog to P and NP for exponential, rather than polynomial, time bounds:
- EXP
- NEXP
- coNEXP = {L ⊆ Σ* : ¯L ∈ NEXP}.
Lemma 9
- P ⊆ NP ⊆ EXP ⊆ NEXP.

RESTRICTED HALT is the set of all TMs that halt on a given input within a given number of steps.

theorem 28
- RESTRICTED HALT ∈ EXP.
theorem 29 
- RESTRICTED HALT is EXP-complete


### Logarithmic space classes: L and NL
- L = DSPACE(log n)
- NL = NSPACE(log n)

**STCON**
- A triplet composed of a directed graph G = (V, E) and two nodes s, t ∈ V belongs to the CONNECTIVITY (or ST-CONNECTIVITY, or STCON) language if there is a path in G from s to t.
- STCON ∈ NL.
- STCON ∈ DSPACE(log n)^2.

***NL-completeness of STCON***
- STCON is NL-complete.

**Theorem 34. NL ⊆ P**