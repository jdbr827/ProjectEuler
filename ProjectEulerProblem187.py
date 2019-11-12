from primes import get_primes_less_than_sieve_efficient


#print get_primes_less_than_sieve_efficient(10**8)


# def get_semiprimes_less_than_method2(limit):
# 	count = 0
# 	known_primes = []
# 	num_prime_divisors = [0 for candidate in range(limit)]
# 	for i in range(2, limit):
# 		if num_prime_divisors[i] == 0:
# 			## the number is prime
# 			num_prime_divisors[i] += 1
# 			num_prime_divisors[i**2] += 2 # p is used twice
# 			quotient = limit // i
# 			known_primes.append(i)
# 			for p in known_primes:
# 				if p > quotient:
# 					break
# 				count += 1
# 		elif num_prime_divisors[i] == 2:
# 			count += 1
# 		print num_prime_divisors
# 	return count



def get_semiprimes_less_than(limit):
	"""
	Returns the number of numbers between 1 and limit, exclusive
	that can be written as the product of two (not necessarily distinct) primes.
	"""
	count = 0
	primes_under_limit = get_primes_less_than_sieve_efficient(limit // 2)
	print "finished sieve"	
	print len(primes_under_limit)
	return get_semiprimes_from_primes_less_than(limit, primes_under_limit)
	

def get_semiprimes_from_primes_less_than_method2(limit, primes_under_limit):
	for i in range(len(primes_under_limit)):
		quotient = limit // primes_under_limit[i]
		for j in range(i, len(primes_under_limit)):
			if primes_under_limit[j] <= quotient:
				count += 1
			else:
				break
	return count


def get_semiprimes_from_primes_less_than(limit, primes_less_than_limit):
	i = 0
	j = len(primes_less_than_limit) - 1
	count = 0
	#print primes_less_than_limit
	while i <= j:
		#print i, j, count
		if primes_less_than_limit[i] * primes_less_than_limit[j] > limit:
			#print "over"
			j -= 1
			continue
		elif primes_less_than_limit[i] * primes_less_than_limit[j] < limit:
			#print "under"
			count += j-i + 1
			i += 1
			continue

	return count

#print get_semiprimes_less_than(30)
print get_semiprimes_less_than(10**8)
