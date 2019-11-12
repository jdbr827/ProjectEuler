"""
Project Euler Problem 37 (Truncatable Primes)
"""
import math
def solve():

	num_digits = 2
	primes = [2, 3, 5, 7] 
	past_left_truncatable = [2, 3, 5, 7] # primes with num_digits - 1 digits that are left_truncatable
	past_right_truncatable = [2, 3, 5, 7] # primes with num_digits - 1 digits that are right_truncatable
	current_left_truncatable = [] # primes with num_digits digits that are left_truncatable
	current_right_truncatable = [] # primes with num_digits digits that are right_truncatable
	fully_truncatable = [] # fully truncatable primes

	candidate = 11
	while len(fully_truncatable) < 11: # we need to find all 11
		
		### Find the next prime:
		for prime in primes:
			if prime > math.sqrt(candidate):
				# It's a prime:
				primes.append(candidate)
				lt = int(str(candidate)[1:]) in past_left_truncatable
				rt = int(str(candidate)[:-1]) in past_right_truncatable
				if lt: current_left_truncatable.append(candidate)
				if rt: current_right_truncatable.append(candidate)
				if lt and rt: fully_truncatable.append(candidate)
				break 
			elif candidate % prime == 0:
				break
		candidate += 2

		## Once we have exauhsted all primes/candidates for num_digits digits,
		# we now move to num_digits+1 digits
		if len(str(candidate)) > num_digits:
			num_digits += 1
			past_left_truncatable = current_left_truncatable
			past_right_truncatable = current_right_truncatable
			current_left_truncatable = []
			current_right_truncatable = []

	return sum(fully_truncatable)




print solve()