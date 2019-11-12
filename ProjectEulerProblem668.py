"""
Project Euler Problem 668
(Square Root Smooth Numbers)
"""
import math

LIMIT = 10000000000

from primes import get_primes_less_than_sieve_efficient
from primes import get_primes_less_than_sieve
from primes import get_primes_segmented_sieve
#print len(get_primes_less_than_sieve_efficient(int(math.sqrt(LIMIT))))


print len(get_primes_segmented_sieve(10000000000)) #== get_primes_less_than_sieve_efficient(1000000)



def pi_approx(n):
	"""
	returns the approximate number of primes less than n, according to PNT.
	"""
	return n / math.log1p(n - 1)

#ps = get_primes_less_than_sieve_efficient(10**10)
#print len(ps)

# ps = get_primes_less_than_sieve_efficient(int(math.sqrt(LIMIT)))
# print len(ps)
# tot = sum(ps)
# for i in range(int(math.sqrt(LIMIT) - 1), 0, -1):
# 	tot += i*(pi_approx(LIMIT//i) - pi_approx(LIMIT//(i+1)))
# print tot
# 	#print i, LIMIT//(i+1), LIMIT//i, pi_approx(LIMIT//i) - pi_approx(LIMIT//(i+1))



#print pi_approx(10**10)


# print math.sqrt(LIMIT)
# primes = get_primes_less_than_sieve_efficient(10**8)
# print len(primes)
# i = 10**8 + 1
# while i < LIMIT:
# 	isCompositeFlag = False
# 	thisPrime_idx = 1 # since primes[0] = 2 and we are already filtering those out
# 	thisPrime = primes[thisPrime_idx]
# 	while thisPrime <= math.sqrt(i):
# 		if i % thisPrime == 0:
# 			#print i, thisPrime
# 			isCompositeFlag = True
# 			break
# 		thisPrime_idx += 1
# 		thisPrime = primes[thisPrime_idx]
# 	if not isCompositeFlag:
# 		primes.append(i)
# 		print i
# 	i += 2


print "HI"

#print max(get_primes_less_than_builder_efficient(10000000 + 1))
# def get_primes_under(n):
# 	"""
# 	Returns the set of all prime numbers less than n
# 	"""
# 	if n < 2: return []
# 	primes = [2]
# 	if n == 2: return primes

# 	# candidates[i] = true iff 3 + 2i is prime
# 	candidates = [True for i in range(3, n, 2)]
# 	i = 0
# 	candidate = 3
# 	while candidate < n:

# 		if candidates[i]:
# 			primes.append(candidate)
# 			runner = candidate ** 2
# 			j = 3 + (3*i) + (2*(i**2))
# 			k = j
# 			print candidate, k, 
# 			while runner < n:
# 				#print candidate, k, 3 + 2*k
# 				candidates[k] = False
# 				runner += 2*candidate
# 				k += j
# 		candidate += 2
# 		i+= 1
# 	return primes






	



