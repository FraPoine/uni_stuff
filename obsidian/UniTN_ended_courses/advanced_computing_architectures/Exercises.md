## Vector mode
Computation in vector mode runs 20 times faster than normal
1. Draw a graph that plots the overall speedup as a function of the percentage of the computation performed in vector mode
2. What percentage is needed to achieve an overall speedup of 2?
3. What percentage is needed to achieve one-half of the maximum speedup attainable?
4. What percentage do you need in order to achieve the same speedup that you would get if vector mode run 40 times faster and the percentage were 70%?

S overall = 1/((1-F) + F/S) ---> S -> ∞ 1/1-F

2. So ((1-F) + F/S ) = 1
	- So - FSo + FSo/S = 1
	- FSo (- 1 + 1/S) = -So +1
	- F = (-So +1) / (So (1/S - 1))
	- F = S(1 - So) / (So(1 - S))
		- F = 20(-1)/2(-19)
		- = 20/38
		- = 10/19
		- = 53% :)

3. bella
4. 


