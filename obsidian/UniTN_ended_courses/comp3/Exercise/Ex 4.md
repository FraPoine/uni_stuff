Let M represent a Turing Machine, let there be an encoding s --> Ms mapping string s ∈ Σ* to the TM Ms encoded by it. Finally, remember that in our notation M(x) = ∞ means “M does not halt when executed on input x”. 
Consider the following languages:
- L1 = {s ∈ Σ* | ∃xMs(x) != ∞} = {s ∈ Σ* | Ms halts on some inputs}
	- it exists x st Ms(x) does halt when x is executed
- L2 = {s ∈ Σ* | ∀xMs(x) != ∞} = {s ∈ Σ* | Ms halts on all inputs}
	- 4 every x Ms(x) does halt when x is executed
- L3 = {s ∈ Σ* | ∃xMs(x) = ∞} = {s ∈ Σ* | Ms doesn’t halt on some inputs}
	- it exists x st Ms(x) does not halt when x is executed
- L4 = {s ∈ Σ* | ∀xMs(x) = ∞} = {s ∈ Σ* | Ms doesn’t halt on any input}
	- 4 every x st Ms(x) does not halt when x is executed
##### 4.1
Provide examples of TMs M1, . . . , M4 such that M1 ∈ L1, . . . , M4 ∈ L4.
- M1, M2 --> the machine that ever halts
- M3, M4 --> the machine that never halts
- dc che forte che sono
##### 4.2
Describe the set relationships between the four languages (i.e., which languages are subsets of others, which are disjoint, which have a non-empty intersection).


