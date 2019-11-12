"""
Project Euler Problem 50 (Consecutive Prime Sum)
"""
#import primes
import math

# sieved_primer = primes.is_prime_precompute_sieve(50)
# sieved_primes = primes.get_primes_less_than_sieve_efficient(50)

# for i in range(50):
# 	if i in sieved_primes and not sieved_primer[i]:
# 		print i
# 	if i not in sieved_primes and sieved_primer[i]:
# 		print i




# def isPrime_sieve(upper_bound_exclusive):
# 	"""
# 	returns an array where, for 0 <= i < upper_bound_exclusive:
# 	isPrime_sieve[i] tells you if i is prime.
# 	"""
# 	sieve = [True for i in range(upper_bound_exclusive)]
# 	sieve[0] = False
# 	sieve[1] = False
# 	i = 2:
# 	while i < math.sqrt(upper_bound_exclusive):
# 		if sieve[i] == True:
# 			j == i**2
# 			while j < upper_bound_exclusive:
# 				sieve[j] = False
# 				j += i
# 	return sieve


def get_primes_and_isPrime_func_sieve(n):

	primes = []
	isPrimeArray = [True for i in range(n)]
	isPrimeArray[0] = False
	isPrimeArray[1] = False
	for i in range(2, n):
		if isPrimeArray[i]:
			primes.append(i)
			j = i
			while i * j < n:
				isPrimeArray[i*j] = False
				j += 1
	return isPrimeArray, primes


def longest_run_of_consecutive_primes_adding_to_a_prime_below(N):
	(isPrime_precomputed, known_primes) = get_primes_and_isPrime_func_sieve(N)
	best_prime = 2
	best_len = 0
	for i in range(len(known_primes)):
		this_candidate= sum(known_primes[i:i+best_len+1]) # Note that in Python slice indeces are handled gracefully, so this won't ever IndexError
		for j in range(i+best_len+1, len(known_primes)):
			this_candidate += known_primes[j]
			if this_candidate >= N:
				break
			elif isPrime_precomputed[this_candidate]:
				best_len = j-i+1
				best_prime = this_candidate
	return best_len, best_prime

def longest_run_of_consecutive_primes_adding_to_a_prime_below_v1(N):
	(isPrime_precomputed, known_primes) = get_primes_and_isPrime_func_sieve(N)
	best_prime = 2
	best_len = 0
	for i in range(len(known_primes)):
		this_candidate = known_primes[i]
		for j in range(i+1, len(known_primes)):
			this_candidate += known_primes[j]
			if this_candidate >= N:
				break
			elif j-i <= best_len:
				continue
			elif isPrime_precomputed[this_candidate]:
				best_len = j-i+1
				best_prime = this_candidate
				print i, j, best_prime


	# 	j = i + best_len + 1 # try to beat the best length
	# 	if j >= len(known_primes): 
	# 		break
	# 	this_candidate = sum(known_primes[i:j])
	
	# 	while this_candidate < N:
	# 		if isPrime_precomputed[this_candidate]:
	# 			best_len = j-i
	# 			best_prime = this_candidate
	# 		j += 1
	# 		if j > len(known_primes):
	# 			break
	# 		this_candidate += known_primes[j]
	# print i, j


# ### O(n^3) time
# def longest_run_of_consecutive_primes_adding_to_a_prime_below(N):
# 	#p = primes.get_primes_less_than_sieve_efficient(N)
# 	p = isPrime_sieve(N)
# 	my_primes = [prim for prim in p if p[prim]]
# 	best_prime = -1 # None

# 	## M[i][j] := the sum of i+1 consecutive primes starting with the j-1th prime 
# 	M = [my_primes]
	





# 	longest_run = 0
# 	longest_run_prime = 0
# 	for target_idx in range(len(p)):
# 		prime_target = p[i]

# 		for j in range(i):
# 			prime_sum = p[j]
# 			if prime_sum > prime_target // 2: break # cause the sum is gonna go over
# 			k = j
# 			while prime_sum < prime_target:
# 				k+= 1
# 				prime_sum += p[k]
# 			if prime_sum == prime_target:
# 				this_run = k - j + 1
# 				if this_run > longest_run:
# 					longest_run = this_run
# 					longest_run_prime = prime_target
# 	return (longest_run, longest_run_prime)

def solve():
	(test_longest_run, test_longest_run_prime) = longest_run_of_consecutive_primes_adding_to_a_prime_below(1000)
	print test_longest_run == 21, test_longest_run
	print test_longest_run_prime == 953
	(longest_run, longest_run_prime) = longest_run_of_consecutive_primes_adding_to_a_prime_below(10**6)
	print longest_run_prime
	pass


solve()
