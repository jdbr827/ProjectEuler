"""
Project Euler Problem 56
Considering natural numbers of the form a^b, where a, b < 100, what is the maximal digit sum?
"""

def digit_sum(n):
	return sum([ord(i) - ord("0") for i in str(n)])

def solve():
	best = 0
	for a in range(1, 100):
		for b in range(1, 100):
			this = digit_sum(a**b)
			if best < this:
				best = this
	return best

print solve()