"""
Project Euler Problem 57
"""

import math 
def solve():
	(n, d) = (3, 2)
	tot = 0
	for _ in range(2, 1000 + 1):
		(n, d) = (n + 2*d, n + d)
		if int(math.log(n, 10)) > int(math.log(d, 10)):
			tot += 1
	return tot

print solve() 
