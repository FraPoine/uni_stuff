Write a Turing machine according to the following specifications: 
- the alphabet is Σ = {- , 0, 1}, where ‘-’ is the default symbol;
- it has a single, bidirectional and unbounded tape; 
- the input string is a finite sequence of symbols in {0, 1}, surrounded by endless ‘-’ symbols on both sides; 
- the initial position of the machine is on the leftmost symbol of the input string; 
- every ‘1’ that immediately follows ‘0’ must be replaced with ‘-’ (i.e., every sequence ‘01’ must become ’0-’). 
- the final position of the machine is at the righmost symbol of the output sequence. 
For instance, in the following input case 
- . . . - - 1 0 1 1 1 0 1 0 0 - - . . .  --> s1 
the final configuration should be
- . . . - - 1 0 - 1 1 0 - 0 0 - - . . . --> halt 
You can assume that there is at least one non-‘-’ symbol on the tape, but considering the more general case in which the input might be the empty string is a bonus

---
- every 1 that immediately follows 0 must be replaced with -
- final position rightmost symbols

|     | 0          | 1             | -             |
| --- | ---------- | ------------- | ------------- |
| s1  | 0,right,s2 | 1, righgt, s1 | -, left, halt |
| s2  | 0,right,s2 | -, righgt, s1 | -, left, halt |

---
### 3.2
- \[0]10011000111 --> s1
- 0\[1]0011000111 --> s2
- 0-\[0]011000111 --> s1
- 0-0\[0]11000111 --> s2
- 0-00\[1]1000111 --> s2
- 0-00-\[1]000111 --> s1
-  0-00-1\[0]00111 --> s1
- 0-00-10\[0]0111 --> s2
- 0-00-100\[0]111 --> s2
- 0-00-1000\[1]11 --> s2
- 0-00-1000-\[1]1 --> s1
- 0-00-1000-1\[1] --> s1
- 0-00-1000-11\[-] --> s1
- 0-00-1000-1\[1] --> halt


