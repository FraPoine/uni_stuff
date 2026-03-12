- Complete the proof of Theorem 9 by writing down, given a positive integer n, an n-state Turing machine on alphabet {0, 1} that starts on an empty (i.e., all-zero) tape, writes down n consecutive ones and halts below the rightmost one.
- Test it for n=3.

Theorem 9
- The function Σ(n) eventually outgrows any computable function.
- proof
	- Let f : N → N be computable. Let us define the following function:
		- F(n) = Σ_{i=0}^n \[f(i) + i^2 ]
	- By definition, F clearly has the following properties:
		- F (n) ≥ f (n) ∀n ∈ N,
		- F (n) ≥ n^2 ∀n ∈ N,
		- F (n + 1) > F (n) ∀n ∈ N
- the latter because F (n + 1) is equal to F (n) plus a strictly positive term. Moreover, since f is computable, F is computable too. Suppose that MF is a TM on alphabet {0, 1} that, when positioned on the rightmost symbol of an input string of x ones and executed, outputs a string of F (x) ones (i.e., computes the function x 7→ F (x) in unary representation) and halts below the rightmost one. Let C be the number of states of MF. Given an arbitrary integer x ∈ N, we can define the following machine M running on an initially empty tape (i.e., a tape filled with zeroes):
	- Write x ones on the tape and stop at the rightmost one (i.e., the unary representation of x: it can be done with x states, see Exercise 2 at page 90);

---
Lets try to understand the theorem 
- talking about the BB function
	- ***the function Σ(n) eventually outgrows any computable function.***
- what does it mean
	- the function Σ(n)
		- that is the largest number of (not necessarily consecutive) ones left by any machine upon halting;
	- because is the largest number of 1s left by a function, any other function that halts will be outgrow by Σ(n)
- Proof
	- we need a function that is computable f : N --> N
		- F(N) = f(i) + i^2
			- i from 0 to n
	- by definition F(N) clearly
		- is >= than f(n)
		- is >= than n^2
		- F(n + 1) is > than F(n) --> if this one is true is it also true that if F(n) is computable F(n + 1) is computable too
			- just remember that is true for every n in N
	- we also need a TM, we will call it Mf, that is a TM on alphabet {0,1} that:
		- when positioned on the rightmost symbol of an input string of x ones and executed, outputs a string of F(x) ones, and halts below the rightmost one
		- C is the number of states of Mf
	- given an arbitrary integer x ∈ N, we can define the following M running on an initially empty tape. 
		- It:
			- Write x ones on the tape and stop at the rightmost one
			- Execute Mf on the tape
			- Execute Mf again on the tape
		- M works on alphabet {0,1}, start with an empty tape, ends with F(F(x)) ones written on it and has x + 2C states; therefore it is a busy beaver candidate, and the (x + 2C)-state BB must perform at least as well:
			- Σ(x + 2C) >= than F(F(x))
			- F(x) >= than x^2 >_e_ x + 2C

all of that say that the function Σ(n) eventually outgrows any computable function :)


therefore

Ex 2
given a positive integer n, an n-state Turing machine on alphabet {0, 1} that starts on an empty (i.e., all-zero) tape, writes down n consecutive ones and halts below the rightmost one.
- positive integer n 
- n-state TM
- alphabet {0,1}
- start on empty tape,
- write down n consecutive ones and halts below the rightmost one

what we know
- to write a TM we need 
	- symbol 
	- direction
	- next state

|      | 0              | 1              |
| ---- | -------------- | -------------- |
| S1   | 1, right, S2   | 1, right, Halt |
| S2   | 1, right, S3   | -              |
| Si   | 1, right, Si+1 | -              |
| Sn-1 | 1, right, Sn   | -              |
| Sn   | 1, left, halt  | -              |

Its important remember that the machine must have n states
of course the machine only need 1 state but it must have n states :)

---
# 2.2
test it for n = 3
lets simulate the machine 

|     | 0            | 1              |
| --- | ------------ | -------------- |
| S1  | 1, right, S2 | 1, right, Halt |
| S2  | 1, right, S3 | -              |
| S3  | 1, left, S1  | -              |

lets simulate it :)

lets start
- \[0]0000000 --> S1
- \[1]0000000 --> S1
- 1\[0]000000 --> S2
- 1\[1]000000 --> S2
- 11\[0]000000 --> S3
- 11\[1]000000 --> S3
- 1\[1]100000 --> S1
- 11\[1]000000 --> halt


