"""
Project Euler Problem 425
"""
import math
from primes import get_primes_less_than_sieve_efficient
from unionfind import UnionFind
from primes import get_primes_and_isPrime_func_sieve
import time
import unittest

def get_connected_candidates(p):
	"""
	Returns the set of numbers 'connected' to p that are less than p 
	"""
	candidates = []
	for i in range(int(math.log(p, 10)) + 1):
		power = 10**i
		val_at_pow = (p % 10**(i+1)) // power
		
		# this block is to prevent us from going 101 <--> 1
		allow_zero = True
		if i == int(math.log(p, 10)): 
			allow_zero = ((p % 10**(i)) // 10**(i-1)) != 0

		for j in range(1, val_at_pow + 1 - (1-allow_zero)):
			cand = p - (j * power)
			candidates.append(cand)

	return candidates

# Union-Find by smallest reachable prime
def solve(N):
	"""
	Returns the sum of all primes less than N that are not reachable from 2 (reachable as defined by the problem)
	"""
	uf = UnionFind(lambda aR, bR: min(aR, bR))
	tot = 0
	(isPrime, primenums) = get_primes_and_isPrime_func_sieve(N)
	for p in primenums:
		uf.makeset(p)
		for candidate in get_connected_candidates(p): 
			if isPrime[candidate]: 
				uf.union(candidate, p)
		if uf.find(p) != 2: 
			tot += p
	return tot


def test_and_run(solving_function):
	sol3 = solving_function(10**3)
	if sol3 != 431:
		return "FAILED TEST: input 10**3 expected 431 actual " + str(sol3)

	sol4 = solving_function(10**4)
	if sol4 != 78728:
		return "FAILED TEST: input 10**4 expected 78728 actual " + str(sol4)

	start = time.time()
	ans = solve(10**7)
	end = time.time()

	print ("Solution is " + str(ans) + " (found in " + str(end - start) + " seconds)")
 
test_and_run(solve)
