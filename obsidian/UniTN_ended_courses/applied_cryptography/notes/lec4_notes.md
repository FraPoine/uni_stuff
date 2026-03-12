# Pseudo Random Functions and Permutations

**Definition**
ε --> deterministic cipher  ε = (Enc, Dec)
_P_ = _C_ = _X_
fixed *k ∈ K*, *Enc(k, ·) = Fk : X → X* is a permutation

A **Block cipher** is a set of permutations individuated by *k ∈ K, {Fk : k ∈ K}*
**Note** that Block ciphers are also called ***Pseudo Random Permutation*** **(PRP)**


### Pseudo Random Function
More in general, ***Pseudo Random Function* (PRF)** is a function F defined over *(K, X, Y): F : K × X --> Y* 
Note: PRPs are PRFs such that X = Y and Fk is a permutation for any k ∈ K

---
## Security for block ciphers

**A secure block cipher (or PRP) should be computationally indistinguishable from a truly random permutation.**

Let ε Perms\[X\] be the set of all permutations on X .
### Attack Game (BC)
Let  = (Enc, Dec), a block cipher, and A an adversary. We define two experiments, Experiment 0 and Experiment 1. For b = 0, 1, we define:
**Experiment** b:
- The challenger selects f ∈ Perms\[X\] as follow:
	- if b = 0, *k <--(R) K, f = Enc_k* , 
	- if b = 1, *f* <--(R) Perms\[X\]
- A submits a sequence of queries to the challenger. For i = 1, 2, .... ith query is xi ∈ X and the challenger replies with yi = f (xi ) 
- A outputs ˆb ∈ {0, 1}.
Let Wb be the event that A outputs 1 in Experiment b. We define BCadv \[A, E\] = |Pr \[W0\] − Pr \[W1\]|
### Definition of secure block cipher
A block cipher ε is secure if for all efficient adversaries A, the value BCadv \[A, E\] is negligible.

---
## Secure PRF
Analogously we can define a secure PRF as a function which is computationally indistinguishable from a truly random function.
### Attack Game (PRF)
F PRF over (K, X , Y), For b = 0, 1, we define: Experiment b:
**Experiment** b:
- The challenger selects f ∈ Funs\[X, Y\] as follow:
	- if b = 0, *k <--(R) K, f <-- F(k,.) , 
	- if b = 1, *f* <--(R) Funs\[X, Y\]
- A submits a sequence of queries to the challenger. For i = 1, 2, .... ith query is xi ∈ X and the challenger replies with yi = f (xi ) 
- A outputs ˆb ∈ {0, 1}.
Let Wb be the event that A outputs 1 in Experiment b. We define PRFadv \[A, E\] = |Pr \[W0\] − Pr \[W1\]|

#### Definition 
F is secure if for all efficient adversaries A, the value PRFadv \[A, F \] is negligible.

---
#### Is a PRP indistinguishable from a PRF?
Consider the 1-bit PRP from the previous question:
	E (k, x) = x ⊕ k
Is it a secure PRF?
	NO
Attacker A: 
1. query f (·) at x = 0 and x = 1 
2. if f (0) = f (1) output "1", else "0"
- PRFadv \[A, E\] = |0 − 1/2| = 1/2

#### Is a PRP indistinguishable from a PRF?
Consider a distinguishing experiment between functions and permutations. **Observation**: The only way to distinguish between a permutation and a non-permutation function is to find a collision, inputs so that f (x1) = f (x2).

#### Theorem
*An adversary that makes Q queries can distinguish a random permutation from a random function with probability at most Q2/(2|X |). In particular, let E be a PRP over (K, X )*
- |PRFadv \[A, E\] − PRPadv \[A, E\]| < Q^2/2|X |

#### Corollary
- If |X | super-poly.
- PRFadv \[A, E\] negl. ⇔ PRPadv \[A, E\] negl.


---
## Secure encryption from PRP and PRF

how to achieve it:
	and adversary have 2 characteristics
	- what does it have (POWER)
	- what is trying to achieve (GOAL)
## Modes of operation: one time key

Is a secure block cipher also semantically secure?
	"yes", provided the message space is equal to the data block space
	
If we want to encrypt longer messages?
	break up a long message into a sequence of data blocks and encrypt each data block separately

### electronic codebook mode (ECB)
- ECB is not semantically secure for messages that contain two or more blocks.
- E = (Enc, Dec) block cipher (or PRP) over (K, X ). Suppose to use ECB mode for encrypting plaintext composed by 2 blocks, i.e. P = X^2
	- Adv. A send (m0, m0) and (m0, m1) to the challenger
	- Ch. responses with cb = (cb \[0\], cb \[1\])
	- If cb \[0\] = cb \[1\], A outputs 0, 1 otherwise.
- SSadv \[A, ECB\] = 1

#### Deterministic counter-mode (Det. CTR)
- Let X = {0, 1}n. Let F be a PRF over (K, X , X ), the **Deterministic counter-mode** (Det. CTR) encryption is the cipher E′ = (Enc, Dec) defined over (K, X ≤l, X ≤l)
- for which encryption and decryption work as:
	- for k ∈ K and m ∈ X ≤l, with |m| = v
		- Enc(k, m) = (F (k, 0n) ⊕ m\[0], F (k, 1n) ⊕ m\[1], ..., F (k, (v − 1)n) ⊕ m\[v − 1])
- for k ∈ K and c ∈ X ≤l , with |c| = v
	- Dec(k, c) = (F (k, 0n) ⊕ c\[0], F (k, 1n) ⊕ m\[1], ..., F (k, (v − 1)n) ⊕ c\[v − 1]) 

### CRT mode

#### Theorem 
Let x1, ..., xl be fixed, distinct elements, and F be a secure PRF. G (k) = (F (k, x1), F (k, x2), ..., F (k, xl)) is a secure PRG.

##### Corollary
Det. CTR is semantically secure. In particular, for any eff. adversary A attacking E_{DETCTR} there exists an eff. PRF adversary B s.t. 
	SSadv \[A, E_{DETCTR} ] = 2 · PRFadv \[B, F ].


---
# Modes of Operation: many-time Key

## Modes of Operation: many-time Key Semantic Security for many-time key

### Attack Game (Chosen plain-text semantic security)

**security Attack Game (Chosen plaintext semantic security)** 
- Let E = (Enc, Dec) over (K, P, C), and consider an adversary A. For b = 0,1, we define 
- **Experiment b:**
	- The challenger computes k <--(R) K, 
	- A submits a sequence of queries to the challenger. 
		For i = 1, 2, ..., the ith query is a pair of messages, mi0, mi1 ∈ P, of the same length. The challenger computes ci <--(R) Enc(ki , mib ), and sends ci to the adversary.
	- A outputs a bit ˆb ∈ {0, 1}. 
- For b = 0, 1, let Wb be the event that A outputs 1 in Experiment b. We define A’s advantage with respect to E as 
	- CPAadv \[A, E] := |Pr \[W0] − Pr \[W1]|.
- Note: if A wants Enc(k, m) it queries mi0 = mi1 = m. 

##### Definition
E is semantically secure under CPA (IND-CPA) if for any efficient adversary A we have CPAadv \[A, E] is negligible.

Note: CPA Game can be recast as a "bit guessing" game. CPAadv ∗\[A, E] = |Pr \[ˆb = b] − 1/2|, and as usual CPAadv \[A, E] = 2 · CPAadv ∗\[A, E].


---
# Randomized encryption
encrypting same msg twice gives different ciphertexts
ciphertext must be longer than plaintext: CT-size = PT-size + "# random bits"

## Cipher block chaining (CBC)
### CBC: CPA Analysis
##### Theorem
If E is a secure PRP over (K, X ) then ECBC is a sem. sec. under CPA over (K, X^≤l, X^{≤l+1}).
In particular, for a Q-query adversary A attacking E_{CBC} there exists a PRP adversary B s.t.
	CPAadv \[A, ECBC ] ≤ 2 · PRPadv \[B, E] + 2(Q^2 l^2)/|X| .
##### Remark
CBC is only secure as long as Q^2 · l^2 << |X|.

#### Attack on CBC with predictable IV
CBC where attacker can predict the IV is not CPA-secure,
Bug in SSL/TLS 1.0: IV for record \#i is last CT block of record #(i-1) Suppose that A, given c = E_{CBC} (k, m) can predict IV for next message

#### A CBC technicality: padding
How do you encrypt odd-length messages with a fixed-length block cipher?
	Pad message somehow.
padding attack :(


#### rand CTR-mode: CPA analysis

##### Theorem
*If F is a secure PRF over (K, X , Y) then E_{rndCTR} is a sem. sec. under CPA. In particular, for a Q-query adversary A attacking E_{rndCTR} there exists a PRF adversary B s.t.*
	CPAadv \[A, E_{rndCTR} ] ≤ 2 · PRFadv \[B, F ] + 2(Q^2 l)/|X|
note: rand. CTR-mode only secure as long as Q^2 l << |X| . (Better than CBC!)



End with comparison between CBC and CTR-mode 