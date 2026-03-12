For each of the following properties of TMs, say whether it is semantic or not, and prove whether it is decidable or not. 
1. M decides words with an ‘a’ in them. 
	- semantic
	- not trivia
	- rice's theorem --> its undecidable
2. M always halts within 100 steps. 
	- not semantic
	- of course its decidible because we can simply verify if the machine halt after 100 steps
3. M either halts within 100 steps or never halts.
	- not semantic
	- obviously its undecidable because its an halting problem that is undecidable
4. M decides words from the 2018 edition of the Webster’s English Dictionary. 
	- semantic
	- not trivial
	- rice's theorem so undecidable
5. M never halts in less than 100 steps. 
	- not semantic
	- as point 2 is decidable 
6. M is a Turing machine. 
	- not semantic
	- trivial
	- is decidable by the TM that always say yes with no regard for the input
7. M decides strings that encode a Turing machine (according to some predefined encoding scheme). 
	- semantic
	- not trivial
	- sooooooo rice's undecidable
8. M is a TM with at most 100 states.
	- not semantic
	- decidable, because it only need to count the states from the machine definition

- ***Semantic***
	- Una proprietà è semantica se dipende dal comportamento computazionale della TM (cioè cosa fa la macchina), non solo dalla sua struttura o descrizione formale.
	- A property is semantic if its value is shared by all TMs recognizing the same language:
		- if L(M) = L(M′ ), then P (M) = P (M′ ).
- ***Decidable***

- ***Rice's Theorem***
	- All non-trivial semantic properties of TMs are undecidable.