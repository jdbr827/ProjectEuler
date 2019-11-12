"""
Project Euler Problem 69
"""
import math
import time

def argmax(inputs, func):
	"""
	Given a finite set of possible inputs, 
	returns the input which results in the maximum output 
	for the given function, along with that output
	"""
	best_arg = None
	best_val = -1 * float("inf")
	for this_arg in inputs:
		this_val = func(this_arg)
		if this_val > best_val:
			best_arg = this_arg
			best_val = this_val
	return best_arg, best_val


def get_distinct_prime_factors(N):
	P = [set([]) for i in range(N+1)]
	for i in range(2, N+1):
		if P[i] == set([]): # i prime
			for j in range(i, N+1, i):
				P[j].add(i)

	return P

def solve(N):
	P = get_distinct_prime_factors(N)
	totient = [set([1 - (1.0/p) for p in P[n]]) for n in range(2, N)]
	for n in range(2, N):
		prod = n
		print n
		for frac in totient[n]:
			prod *= frac
		totient[n] = prod
	return argmax(range(2, N), lambda x: float(x) / totient[x])

solve(10)

def euler_gcd(a, b):
	"""
	Returns the greatest common divisor of a and b utilizing euler's gcd function
	"""
	#(a, b) = (max(a, b), min(a, b))
	#print a, b
	if a == 0: return b
	return euler_gcd(b % a, a)


def relatively_prime(a, b):
	"""
	Returns true if a and b are relatively prime
	"""
	return euler_gcd(a, b) == 1

#print solve(1000000)
def euler_totient2(n):
	"""
	Returns the number of numbers less than n which are relatively
	prime to n
	"""
	tot = 0
	for i in range(1, n):
		if relatively_prime(i, n):
				tot += 1
	return tot

def euler_totient3(n):
	"""
	"""

def solve2(N):
	best = 0
	best_val = 0
	for n in range(2, N):
		val = float(n) / euler_totient2(n)
		if val > best_val:
			best = n
			best_val = val
	return best

# start = time.clock()
# ans = solve2(10000)
# end = time.clock()
# print ans, end - start



# print euler_totient(2) == 1
# print euler_totient(3) == 2
# print euler_totient(4) == 2
# print euler_totient(5) == 4
# print euler_totient(6) == 2
# print euler_totient(7) == 6
# print euler_totient(8) == 4
# print euler_totient(9) == 6
# print euler_totient(10) == 4




# def prime_factor_list_sieve(N):
# 	"""
# 	Returns an array where arr[i] = set of prime
# 	factors of i, for any 1 <= i <= N
# 	"""
# 	p = [set([]) for n in range(N+1)]
# 	for i in range(2, n):
# 		if p[i] == set([]):
# 			for j in range(i, N+1, i):
# 				p[j].add(i)
# 	return p


# def euler_totient_max(N):
# 	"""
# 	Returns the euler totient maximum over 1,..., N
# 	"""
# 	p = prime_factor_list_sieve(N)
# 	#print p
# 	return argmax(range(2, N+1), lambda n: n / len([x for x in range(1, n) if p[x].intersection(p[n]) == set([])]))

	
# 	pass

# print euler_totient_max(10)[0] == 6
# print euler_totient_max(10**6)

# def get_primes_under(n):
# 	"""
# 	Returns a list of all the prime numbers less than n
# 	"""
# 	if n < 2: return []
# 	primes = [2]
# 	if n == 2: return primes
# 	candidates = range(3, n, 2)

# 	while candidates:
# 		thisPrime = candidates.pop(0)
# 		primes.append(thisPrime)
# 		runner = thisPrime ** 2
# 		while runner < n:
# 			if runner in candidates:
# 				candidates.remove(runner)
# 			runner += thisPrime
# 	return primes


# primes = get_primes_under(1000)


# def gcd(a, b):
# 	"""
# 	Returns the greatest common divisor (Euclid's Algorithm)
# 	a < b
# 	"""
# 	r = b % a
# 	b = b // a
# 	while r != 0:
# 		print a, b, r
# 		b = a
# 		a = r
# 		r = b % a
# 		b = b // a
# 	return b


# def get_relative_primes_to(n):
# 	"""
# 	Returns all numbers relatively prime to n
# 	"""
# 	rel_primes = [1]
# 	rel_primes.extend([i for i in range(1, n) if gcd(i, n) == 1])
# 	return rel_primes

# print get_relative_primes_to(10)
# print gcd(3, 10)

# idx = 0
# i = 1
# j = 1
# while j < 1000000:
# 	i = j
# 	j *= primes[idx]
# 	print j
# print i