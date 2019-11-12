"""
Project Euler Problem 58
Spiral primes
"""
import math
from primes import isPrime

def solve():
	side_len = 3 
	num_on_diagonals = 5 
	num_primes_on_diagonals = 3
	while float(num_primes_on_diagonals) / num_on_diagonals >= 0.10:
		side_len += 2
		num_on_diagonals += 4
		for k in [1, 2, 3]:
			candidate = side_len**2 - k*(side_len - 1)
			if isPrime(candidate):
				num_primes_on_diagonals += 1
	return side_len

UPPER_BOUND = 27000

def solve_sieve(limit):
	### run the sieve
	sievebound = (limit - 1) // 2
	sieve = [False for i in range(sievebound)]
	sieve.insert(0, True) # because 1 = 2*0 + 1 is composite
	crosslimit = int(math.sqrt(limit) - 1) // 2
	for i in range(1, crosslimit + 1):
		if not sieve[i]: #2*i+1 is prime, mark multiples
			for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
				sieve[j] = True

	side_len = 3 
	num_on_diagonals = 5 
	num_primes_on_diagonals = 3
	while float(num_primes_on_diagonals) / num_on_diagonals >= 0.10:
		side_len += 2
		num_on_diagonals += 4
		for k in [1, 2, 3]:
			candidate = side_len**2 - k*(side_len - 1)
			print (candidate - 1) // 2
			if sieve[(candidate - 1) // 2]: # note we don't need to check for even odd^2 - num*even = odd
				num_primes_on_diagonals += 1
	return side_len


print solve()
