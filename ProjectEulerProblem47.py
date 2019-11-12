"""
Project Euler Problem 47
(Distinct Prime Factors)
"""

import primes
UPPER_BOUND_GUESS = 1000000

def num_distinct_prime_factors_sieve(upper_bound):
	"""
	returns an array where, for 0 <= i <= upper_bound;
	num_distinct_prime_factors[i] is the number of distinct prime factors of i
	"""
	num_distinct_prime_factors = [0 for i in range(upper_bound+1)]
	for i in range(2, upper_bound+1):
		if num_distinct_prime_factors[i] == 0: 
			# i is prime
			j = i
			while j < upper_bound:
				num_distinct_prime_factors[j] += 1
				j += i
	return num_distinct_prime_factors

def first_k_consecutive_numbers_with_k_distinct_prime_factors(k, num_distinct_prime_factors_arr):
	"""
	Returns the first of first set of k consecutive numbers to have k distinct prime factors each
	Returns -1 if no answer exists between 1 and len(num_distinct_prime_factors_arr - k)
	num_distinct_prime_factors_arr must be an array where for 0 <= i <= len(num_distinct_prime_factors_arr), num_distinct_prime_factors_arr[i] is the number of distinct prime factors of i
	"""
	i = 0
	while i < len(num_distinct_prime_factors_arr) - k:
		is_answer_flag = True
		for j in range(k):
			if num_distinct_prime_factors_arr[i+j] != k:
				i += j + 1
				is_answer_flag = False
				break
		if is_answer_flag:
			return i
	return -1



def test():
	num_distinct_prime_factors = num_distinct_prime_factors_sieve(1000000)
	print num_distinct_prime_factors[14] == 2
	print num_distinct_prime_factors[15] == 2
	print num_distinct_prime_factors[644] == 3
	print num_distinct_prime_factors[645] == 3
	print num_distinct_prime_factors[646] == 3
	print first_k_consecutive_numbers_with_k_distinct_prime_factors(2, num_distinct_prime_factors) == 14
	print first_k_consecutive_numbers_with_k_distinct_prime_factors(3, num_distinct_prime_factors) == 644
	print first_k_consecutive_numbers_with_k_distinct_prime_factors(4, num_distinct_prime_factors)


	pass

test()
