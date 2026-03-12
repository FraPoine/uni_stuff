For each of the following classes of Turing machines, decide whether the halting problem is computable or not. If it is, outline a procedure to compute it; if not, prove it (usually with with a reduction from the general halting problem). Unless otherwise stated, always assume that the non-blank portion of the tape is bounded, so that the input can always be finitely encoded if needed.
1. TMs with 2 symbols and at most 2 states (plus the halting state), starting from an empty (all-blank) tape.
2. TMs with at most 100 symbols and 1000000 states.
3. TMs that only move right;
4. TMs with a circular, 1000-cell tape.
5. TMs whose only tape is read-only (i.e., they always overwrite a symbol with the same one);

**How to decide if an halting problem is computable or uncomputable**
- obiettivo:
	- è decidibile o non decidibile?
- quando è decidibile?
	- Lo **spazio delle configurazioni** della macchina è **finito**.
	- esempi:
		- Macchine di Turing con nastro finito e circolare
		- TM che si muove solo a destra su un nastro infinito
		- TM con stati, simboli e spazio estremamente limitati
- Quando non è computabile?
	- La macchina può generare **infiniti comportamenti diversi**
	- esempi:
		- Nastro **infinito** in entrambe le direzioni
		- Possibilità di **muoversi a destra e a sinistra**
		- **Infiniti stati** o combinazioni di dati
---
# 1 
TMs with 2 symbols and at most 2 states (plus the halting state), starting from an empty (all-blank) tape
- alphabet with two symbols
	- 0 - 1
- 2 states + halt
	- true
	- false 
	- halt
- all-blank tape

is it decidable?
- it is decidable if exists an algorithm that can solve every input in polynomial time.

**Busy Beaver game**
- Among all TMs on alphabet {0, 1} and with n = |Q| states (not counting the halting one) that halt when run on an empty (i.e., all-zero) tape:
	- let Σ(n) be the largest number of (not necesssarily consecutive) ones left by any machine upon halting; 
	- let S(n) be the largest number of steps performed by any such machine before halting.
		- The function S(n) is not computable
		- Function Σ(n) is known as the **busy beaver** function for n states, and the machine that achieves it is called the Busy Beaver for n states. Both functions grow very rapidly with n, and their values are only known for n ≤ 5.

SO...
- the TMs with 2 symbols and at most 2 states are perfectly described by the busy beaver game. since we know that up to 4 states the BB has been analyzed we know that the current TMs set are decidable.

---
# 2
TMs with at most 100 symbols and 1000000 states.

An UTM (Univarsal Turing Machine) can simulate every other TMs. So, if a set can express an universal TM, that set can express any computational problem, halting problem included, that is uncomputable.
The smallest possible UTM have 2 symbols and 3 states, much more less than the TMs with at most 100 symbols and 1000000 states, and so it is uncomputable

---
# 3
TMs that only move right

Why it is computable?
- If the machine cannot visit the same cell twice, the symbol it writes won’t have any effect on its future behavior.
- A TM that can only move right has a finite number of states so we can describe the halting problem like
	- if the machine find an already seen configuration it enter in a loop and halt, 
	- if the machine did not find an already seen config it didn't halt
- so the halting problem is decidable 

---
# 4
TMs with a circular, 1000-cell tape

this set has a finite number of cells, finite number of states, finite number of symbols. so, the number of the possible configuration is finite.
If the number of configuration is finite the machine can't go forward forever without repeating a configuration. So we can understand if it enter in a cycle of it stop. So the halting problem is decidible.

---
# 5
TMs whose only tape is read-only (i.e., they always overwrite a symbol with the same one)

**Read-only Turing Machines** have strong limitations.  
Like the ones that can only move to the right, they have a **finite number of possible configurations**.
Because the machine **cannot modify the tape**, its behavior is **fully determined** by its current state and position.
This means the computation is **finite and predictable**, and we can simulate it step by step.  
If the machine enters the **same configuration** again (same state and same tape position), we know it will **loop forever**.  
If it reaches the halting state, we know it **stops**.
So, we can **always decide** whether the machine halts or not:  
👉 **The halting problem is decidable** for read-only Turing Machines.