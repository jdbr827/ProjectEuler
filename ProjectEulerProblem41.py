"""
Project Euler Problem 41 (Pandigital Prime)
What is the largest n-digit pandigital prime that exists?
"""
import math
import itertools
from primes import isPrime

## Any 9-digit pandigital prime has digit sum 45 and is thus divisible by 3
## Any 8-digit pandigital prime has digit sum 36 and is thus divisible by 3

def make_num(digit_tup):
	num = 0
	for i in range(7):
		num += digit_tup[-1 *i] * (10**i)
	return num

def solve():
	best = 0
	for i in itertools.permutations(range(1, 7+1)):
		num = make_num(i)
		if isPrime(num):
			if num > best:
				best = num
	print best
	pass

solve()
print solve_2()

	
	
