# Computability
## Recursive and recursively enumerable sets

***Why is every finite set recursive?***
- Recursive (or computable, or decidable) 
	- *given function, or a set, we say that is **recursive** if and only if a procedure can be described to compute the function's outcome in a finite number of steps.* 
	- some example 
		- the set of even numbers
		- a function that decides whether a number is prime or not
		- any function studied in a basic Algorithms course 
		- any finite or co-finite set, and any function that decides on them;
		- The number of computer algorithms is countable.
- Uncomputable functions
	- Example
		- *The set of decision functions f : N → {0, 1} (or, equivalently, f : Σ∗ → {0, 1}), is uncountable*
		- *there are uncomputable decision functions.*
		- collatz sequence 
- **Answer**
	- from the definition of **recursive** we say that a set is recursive only if a procedure can be described to compute the set's outcome in a finite number of steps. A finite set has a finite number of elements by definition, and a rule that confront every elements in the set with a given one can describe the set in a finite number of steps. So every finite set is recursive
- Recursively enumerable (RE)
	- *A set S of natural numbers is called **computably enumerable** if there is a [partial computable function](https://en.wikipedia.org/wiki/Computable_function "Computable function") whose [domain](https://en.wikipedia.org/wiki/Domain_of_a_function "Domain of a function") is exactly S, meaning that the function is defined if and only if its input is a member of S.*

***Try to prove that if a set is recursive, then its complement is recursive too.***
- Complement of a set
	- the set of all elements within a defined universal set (U) that are not in the original set (A)
- How does it work?
	- Definition of recursive set by notebook
		- a set (or a decision function) is recursive (or decidible) If and only if exists a procedure, or an algorithm, for any possible input, that can describe an outcome in a finite number of steps. A set is uncomputable (or undecidable) if it is not computable.
- **Proof**
	- let us assume that A ⊆ N is a recursive set, 
		- that mean that exists a function that f : N --> {0,1}
			- 1 if n ∈ A
			- 0 if n !∈ A
	- we want to construct a computable function g : N --> {0,1} that decides member in !A
		- and that need to be such that
			- 1 if n ∈ !A
			- 0 if n !∈ !A
		- and its equal to say
			- 1 if n !∈ A
			- 0 if n ∈ A
	- its also easy define:
		- g(n) = 1 - f(n)
	- because f(n) its total and computable, and subtraction from 1 is a simple and total operation, g(n) is also total and computable.
	- !A is recursive.

***Let S be a recursively enumerable set, and let algorithm A enumerate all elements in S. Prove that, if A lists the elements of S in increasing order, then S is recursive.***
- S set
	- recursively enumerable (**RE**)
		- A function or a set is recursively enumerable (**RE**) if we are not able to prove that is *decidible* but we can provide a procedure that terminates with the correct answer when the answer is yes.
- A algorithm
	- enumerate all elements in S
	- in increasing order 
- **Proof**
	- the set S is recursive if exits a function f : N --> {0,1} such that
		- f(n) = 1 if n ∈ S
		- f(n) = 0 if n !∈ S
	- we have the algorithm A that list all number of S in increasing order,we can use this property to decide whether a given number n is in SSS or not
		- If A outputs n, then clearly n ∈ S.
		- If A outputs some number greater than n before outputting n, n !∈ S.
	- So we can **decide** membership in S by running A step-by-step and comparing its output to n.
	- Since such a decision function exists, we conclude that **S is recursive**

---

## Turing machines
***Why do we require a TM’s alphabet Σ and state set Q to be finite, while we accept the tape to be infinite?***
- A TM is an abstract model of a real world machine
- to mirror a real world machine we need
	- Σ, an alphabet, a finite number of symbols 
	- Q, a finite number of states
- This allows us to reason about **decidability**, **recognizability**, and **complexity** in a rigorous way.
- The *infinite* tape is required by the idea that computation can use as much memory as needed, as long as is't finite at any point in time
	- that allows TM to simulate any machine and any computation as long as it halts eventually
- the tape being infinite isn't meant to suggest real machines have infinite memory. It's a theoretical convenience that helps determine what's computable, not what's convenient.

***What is the minimum size of the alphabet to have a useful TM? What about the state set?***
- There is only needed 2 symbols to create an UTM that is the **Universal Turing Machine** that can simulate every other TM. That's because every finite alphabet can be simulated with a binary codification.
- the smallest know UTM uses only 2 symbols and 3 states and may be Turing-complete
	- **Turing-complete** --> UTM
- Are only needed three states because, using an infinite amount of memory, infinite tape, based on the symbol read, the 3 states permit to:
	- decide what to write
	- decide where to move
	- move to the next state
- and this whit enough time and memory can simulate every TM making it Turing-complete.

***Try writing machines that perform simple computations or accept simply defined strings.***
- on the book

---
# Computational complexity
## Definitions
***Why introduce non-deterministic Turing machines, if they are not practical computational models***
- NTMs are not practical machines — they are powerful _theoretical tools_ for reasoning about computational complexity and problem classes.
- They help us define and understand concepts like:
	- **NP (nondeterministic polynomial time)**
	- The famous **P vs NP problem**
	- **Reductions** between problems
	- **Limits of efficient computation**
- An NTM is like a regular Turing Machine, **except**:
	- At each step, it can choose from **multiple possible transitions** (instead of just one).
	- It can "magically" guess the right path — or more formally, it explores **all possible computation paths in parallel**.

***Why do we require reductions to carry out in polynomial time?***
- Reduction in theoretical computer science
	- If I can solve problem **B**, then I can also solve problem **A**, by transforming **A into B**.
- Polinomial time
	- Input Size
	- Execution Time
	- In theoretical computer science, problems solvable in **polynomial time** are considered **"efficiently solvable"**.
- So
	- The reduction must be **at least as efficient** as the problem we’re trying to solve.
- Answer
	- We require reductions to be carried out in **polynomial time** in order to maintain the concept of **efficient computability** within complexity theory. A reduction transforms instances of one problem **A** into instances of another problem **B**, such that solving **B** allows us to solve **A**. However, for this transformation to be meaningful in complexity analysis, it must not introduce an unreasonable amount of computational overhead.
	- If a reduction took exponential time, then even if BBB could be solved efficiently (e.g., in polynomial time), the overall process of solving **A** would still be inefficient. Therefore, to ensure that the difficulty of **A** is truly "no harder" than **B**, the reduction itself must be efficient — specifically, **polynomial in the size of the input**.
	- This is particularly important in the context of **NP-completeness**. To prove that a problem **P** is NP-complete, we must show that every problem in NP can be reduced to **P** in **polynomial time**. This ensures that if **P** could be solved in polynomial time, then **all** problems in NP could also be solved efficiently.
	- In summary, polynomial-time reductions are essential to preserve the integrity of complexity class comparisons, to avoid trivial or misleading relationships between problems, and to accurately capture the notion of **efficient solvability** in theoretical computer science.
	- 
***Am I familiar with Boolean logic and combinational Boolean circuits?***
- yes i am :)

---
## P Vs NP

***Why is it widely believed that P != NP?***
- It is widely believed that **P ≠ NP** because, despite decades of research, no polynomial-time algorithm has been found for any **NP-complete problem**, despite extensive effort by thousands of researchers. NP-complete problems are believed to be inherently hard, because they involve exploring an exponential number of possibilities (e.g., all possible truth assignments in SAT or all possible routes in the traveling salesman problem), and no known shortcuts allow solving them efficiently in all cases. Moreover, many computational tasks in cryptography, optimization, and scheduling are built on the assumption that certain problems cannot be solved efficiently — assumptions that would collapse if P = NP. While P = NP remains a logical possibility, the overwhelming lack of progress in finding efficient algorithms for NP-complete problems supports the belief that **P is not equal to NP**.

***Why is it widely hoped that P != NP?***
- It is widely **hoped** that P≠NP because if P=NP, then every problem whose solution can be efficiently _verified_ could also be efficiently _solved_. This would undermine the security of modern cryptographic systems, which rely on certain problems being computationally hard. It would also mean that many problems long thought to be intractable — like those in scheduling, optimization, and AI — would become efficiently solvable, which sounds exciting but would also eliminate many natural boundaries that guide our expectations about what is computationally feasible. In contrast, if P≠NP, it preserves the intuitive idea that **some problems are inherently hard**, and that **efficient verification does not imply efficient solution** — a foundational assumption in both theory and practice.

---

## Other complexity classes

***Why are classes EXP and NEXP relatively less studied than their polynomial counterparts?***
- **EXP and NEXP describe _very_ hard problems**
	- EXP = deterministic exponential time = problems solvable in time like 2^{n^k}
	- NEXP = non-deterministic exponential time = exponential-size certificates verifiable quickly
- Answer
	- The classes **EXP** and **NEXP** are less studied than their polynomial-time counterparts (like **P** and **NP**) primarily because they deal with problems that are **far beyond practical computation**, even for moderately sized inputs. While P and NP capture the boundary between what is feasibly computable and what is only verifiable efficiently, EXP and NEXP describe problems that require exponential time and are thus considered **intractable in practice**. Moreover, many natural problems from computer science, optimization, and cryptography fall within P and NP, making those classes more relevant for both theoretical and applied research. Finally, the structural theory of complexity classes — including notions like reductions, completeness, and relativization — has been more deeply developed in the polynomial realm, further motivating focused study on P vs NP rather than EXP vs NEXP.

---
## General discussion
- 