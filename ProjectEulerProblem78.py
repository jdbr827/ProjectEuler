"""
Project Euler Problem 78
"""

def p(n):
	if n == 1: return 1
	return 1 + sum([p(i) for i in range(1, n)])


print p(1), p(2), p(3), p(4), p(5)