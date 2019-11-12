"""
Project Euler Problem 27 (Quadratic Primes)
"""
def get_primes_under(n):
	"""
	Returns a list of all the prime numbers less than n
	"""
	if n < 2: return []
	primes = [2]
	if n == 2: return primes
	candidates = range(3, n, 2)

	while candidates:
		thisPrime = candidates.pop(0)
		primes.append(thisPrime)
		runner = thisPrime ** 2
		while runner < n:
			if runner in candidates:
				candidates.remove(runner)
			runner += thisPrime
	return primes

import math

### evaluating at n = 0, we see that b must be a prime number.
b_candidates = get_primes_under(1000)
#print b_candidates

SQUARES = [i**2 for i in range(1000)]

def isPrime(k):
	if k < 2: return False
	sqrt = math.sqrt(k)
	for div in range(2, int(sqrt)+1):
		if k % div == 0:
			return False
	return True


def solve(max_abs):
	most_consecutive_primes = 0
	best_a = None
	best_b = None

	for b in get_primes_under(max_abs+1): # Since n=0 must be a prime
		for a in range(-1 * max_abs, max_abs + 1):
			n = 1
			while isPrime(n**2 + a*n + b):
				n+=1
			if n > most_consecutive_primes:
				most_consecutive_primes = n
				best_a = a
				best_b = b

	print best_a, best_b, best_a * best_b
	
	### Testing that they are indeed all primes
	for n in range(most_consecutive_primes):
		prime = n**2 + best_a*n + best_b
		print prime
		if not isPrime(prime):
			print "ERROR"


solve(1000)