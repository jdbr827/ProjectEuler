"""
Project Euler Problem 35
"""
from collections import defaultdict
import primes as primelib
	

def is_circular_prime(p, isPrimeFunc):
	"""
	Returns whether or not p is a circular prime (does NOT assume p is prime)
	"""
	rotating_p = p
	if not isPrimeFunc(p):
		return False

	### If p has a 0 in it, fails because it will end there
	# this needs to be here because of how cycle_left works
	if "0" in str(p): return False


	for cycle in range(len(str(p))):
		rotating_p = cycle_left(rotating_p)
		if not isPrimeFunc(rotating_p):
			return False
		
	return True


def is_new_circular_prime(p, isPrimeFunc, circular_primes):
	rotating_p = p
	if not isPrimeFunc(p):
		return False
	if binary_search(p, circular_primes):
		return False
	if "0" in str(p): return False

	for cycle in range(len(str(p))):
		rotating_p = cycle_left(rotating_p)
		if not isPrimeFunc(rotating_p) or binary_search(p, circular_primes):
			return False
	return True


def cycle_left(num):
	"""
	There should not be a 0 in the number!!
	"""
	string = str(num)
	return int(string[1:] + string[0])
#print get_primes_under(1000)

def brute_force(n):
	"""
	Returns the list of circular primes less than 10**n 
	"""
	num_circular = 0
	for i in range(1, 10**n):
		if is_circular_prime(i, primelib.isPrime):
			num_circular += 1
	return num_circular

def binary_search(x, arr):
	"""
	Conduct a binary search for x on SORTED list arr
	"""
	if arr == []: return False
	i = 0
	j = len(arr)
	if x < arr[0] or x > arr[-1]:
		return False

	while i <= j:
		mid = (i + j) // 2
		if x < arr[mid]:
			j = mid - 1
		elif x > arr[mid]:
			i = mid + 1
		elif x == arr[mid]:
			return True
	return False


def pre_compute_primes(n):
	"""
	Returns the list of circular primes less than 10**n
	"""

	primes = primelib.get_primes_less_than_builder(10**n)
	
	num_circular_primes = 0
	for i in range(1, 10**n):
		if is_circular_prime(i, lambda x: binary_search(x, primes)):

			num_circular_primes += 1
			#print i
	return num_circular_primes


def pre_compute_primes_check_new(n):
	"""
	Returns the list of circular primes less than 10**n
	"""

	primes = primelib.get_primes_less_than_builder(10**n)
	
	circular_primes = []
	for i in range(1, 10**n):
		if is_new_circular_prime(i, lambda x: binary_search(x, primes), circular_primes):
			circular_primes.append(i)
	print circular_primes
	return len(circular_primes)



def solve():
	print binary_search(2, [1, 2, 3])
	print binary_search(1, [1, 2, 3])
	print binary_search(3, [1, 2, 3])
	print binary_search(4, [1, 2, 3, 4, 5])
	print binary_search(4, [1, 2, 3, 4, 5, 6])
	print not binary_search(7, [1, 2, 3, 4, 5, 6])
	print not binary_search(0, [1, 2, 3, 4, 5, 6])
	print is_circular_prime(197, primelib.isPrime)
	print not is_circular_prime(19, primelib.isPrime)
	print brute_force(2) == 13
	print pre_compute_primes(2) == 13
	print not is_circular_prime(121, primelib.isPrime)
	print pre_compute_primes_check_new(2) == 13
	print pre_compute_primes_check_new(6)

solve()

#print primelib.get_primes_less_than_builder(10000) == primelib.get_primes_less_than_sieve(10000)

def get_circular_primes_below_10_pow(n):
	"""
	returns the list of circular primes less than 10**n
	"""
	primes = get_primes_under_v2(10**n)

	prime_digits_freq_table = defaultdict(lambda : 0)

	# num_circular_primes = 0
	# for prime in primes:
	# 	prime_sorted_digits = str(prime).split()
	# 	prime_sorted_digits.sort()
	# 	prime_sorted_digits = tuple(prime_sorted_digits)
	# 	prime_digits_freq_table[prime_sorted_digits] += 1
	# 	if prime_digits_freq_table[prime_sorted_digits] == len(prime_sorted_digits):
	# 		print prime
	# 		num_circular_primes += len(prime_sorted_digits)

	# return num_circular_primes


	# circular_primes = []

	# for prime in primes:
	# 	l = len(str(prime))
	# 	cycled_prime = cycle_left(prime)

	# 	is_circular_flag = True
	# 	for i in range(l-1):
	# 		if cycled_prime not in primes:
	# 			is_circular_flag = False
	# 			break
	# 		cycled_prime = cycle_left(cycled_prime)
	# 	if is_circular_flag:
	# 		circular_primes.append(prime)

	# return circular_primes

# print get_circular_primes_below_10_pow(2) #== 13

# print get_primes_under(10**6)
# print "OK"
#print len(get_circular_primes_below_10_pow(2))


			