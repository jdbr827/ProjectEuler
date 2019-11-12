"""
Project Euler Problem 87 (Prime Power Triples)
"""
from primes import get_primes_less_than_sieve_efficient
import math
import time
from collections import defaultdict





def prime_power_triples_less_than2(N):
	"""
	Returns the number of integers < N that can be expressed as the 
	sum of a prime square, a prime cube, and a prime fourth power
	"""
	start_time = time.clock()

	A = get_primes_less_than_sieve_efficient(int(math.sqrt(N)))
	
	sieve_time = time.clock() - start_time
	
	# B = []
	# C = []
	# (b, c) = (0, 0)
	# for p in A:
	# 	if p < math.pow(N, 1.0/3):
	# 		B.append(p)
	# 		if p < math.pow(N, 1.0/4):
	# 			C.append(p)
	# 		elif c = 0
	# 	else: break

	i = 0
	while A[i] < math.pow(N, 1.0/4):
		i += 1
	c_max = i
	while A[i] < math.pow(N, 1.0/3):
		i += 1
	b_max = i

	
	sieve_scan_time = time.clock() - sieve_time

	marked = defaultdict(bool)

	# remember A is sorted!
	for c_i in range(c_max):
		c = A[c_i]
		for b_i in range(0, b_max):
			b = A[b_i]
			if b**3 + c**4 >= N:
				break
			for a_i in range(len(A)):
				a = A[a_i]
				x = a**2 + b**3 + c**4
	 			if x < N:
	 				marked[x] = True
	 			else: 
	 				break

	
	# remember A, B, and C are sorted!
	# for c in C:
	# 	for b in B:
	# 		if c**4 + b**3 >= N: 
	# 			break
	# 		for a in A:
	# 			x = a**2 + b**3 + c**4
	# 			if x < N:
	# 				marked[x] = True
	# 			else:
					# break

	
	mark_time = time.clock() - sieve_scan_time

	print N, sieve_time, sieve_scan_time, mark_time
	return sum(marked.values())


def test(case, expected):
	actual = prime_power_triples_less_than(case)
	if actual != expected:
		print "Failure! f(" + str(case) + "): expected: " + str(expected) + " actual: " + str(actual)
	return actual == expected


def test_and_solve(N):
	t1 = test(28, 0) # 28 is the lowest answer
	t2 = test(29, 1) # 28 is the lowest answer
	t3 = test(50, 4) # exactly 4 numbers before 50 can be expressed in such a way
	if t1 and t2 and t3:
		start = time.clock()
		ans = prime_power_triples_less_than(N)
		end = time.clock()
		print "Solution: " + str(ans) + " (solved in " + str(end - start) + " seconds)"

PROBLEM_N = 50000000
 
test_and_solve(PROBLEM_N)