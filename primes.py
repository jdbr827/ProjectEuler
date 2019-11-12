"""
Helpful Prime functions
"""
import math


## Utilizes O(n) memory


# def get_primes_segmented_sieve(n):
# 	delta = int(math.sqrt(n))
# 	primes = get_primes_less_than_sieve_efficient(delta)
# 	m = delta
# 	while m < n:
# 		m += delta
# 		if m > n:
# 			arr = [True for i in range(m-n)]
#  		else: 
#  		arr = [True for i in range(delta)] #arr[i] = isPrime[m-delta + i] 
# 		for p in primes:
# 			if p > math.sqrt(m):
# 				break
# 			#lowest_multiple_in_this_segment = (m-delta) + (p - ((m-delta) % p))
# 			remainder = ((m-delta) % p)
# 			if remainder == 0: 
# 				runner = 0
# 			else:
# 				runner = (p - ((m-delta) % p))
# 			while runner < len(arr):
# 				arr[runner] = False 
# 				runner += p
# 		for i in range(len(arr)):
# 			if arr[i]:
# 				primes.append(m-delta+i)
# 	return primes


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



def is_prime_precompute_sieve(n):
	"""
	Returns an array where A[i] is a boolean stating whether or not i is prime.
	"""
	isPrimeArray = [True for i in range(n)]
	isPrimeArray[0] = False
	isPrimeArray[1] = False
	for i in range(2, n):
		if isPrimeArray[i]:
			j = i
			while i * j < n:
				isPrimeArray[i*j] = False
				j += 1
	return isPrimeArray


def get_primes_less_than_sieve(n):
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



def get_primes_less_than_sieve_efficient(limit):
	### Possibly broken? 
	# Idea: sieve[i] := is 2i + 3 (1?) composite?

	sievebound = (limit - 1) // 2
	sieve = [False for i in range(sievebound)]
	sieve.insert(0, True) # because 1 = 2*0 + 1 is composite
	crosslimit = int(math.sqrt(limit) - 1) // 2
	for i in range(1, crosslimit + 1):
		if not sieve[i]: #2*i+1 is prime, mark multiples
			for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
				sieve[j] = True


	primes = [2]
	for i in range(len(sieve)):
		if not sieve[i]:
			primes.append(2*i + 1)
	return primes


### O(sqrt(n)) time; O(1) memory
def isPrime(n):
	"""
	Returns whether or not n is prime
	"""
	if n < 2: return False
	for div in range(2, int(math.sqrt(n)+1)):
		if n % div == 0:
			return False
	return True


def is_relatively_prime_to_all_of(n, others):
	if others == []:
		return True
	for other in others:
		if n % other == 0:
			return False
		return True


# def get_primes_between_builder_given_smaller_primes(low_inclusive, high_exclusive, primes_less_than_low):
# 	"""
# 	Mutates primes_less_than_low
# 	Assues primes_less_than_low are sorted in increasing order
# 	"""
# 	if high_exclusive < 2: return []

# 	if low_inclusive % 2:
# 		low_inclusive = low_inclusive + 1
	
# 	primes = primes_less_than_low
# 	i = low_inclusive
# 	while i < high_exclusive:
# 		if is_relatively_prime_to_all_of(primes):
# 			for 


def get_primes_less_than_builder_efficient(n):
	if n < 2:
		return []
	primes = [2]
	if n == 2: 
		return primes
	primes.append(3)
	if n == 3 or n == 4: 
		return primes
	primes.append(5)

	pm = 1
	i = 7
	while i < n:
		isCompositeFlag = False
		thisPrime_idx = 2 # since primes[0] = 2, primes[1] = 3 and we are already filtering those out
		thisPrime = primes[thisPrime_idx]
		while thisPrime <= math.sqrt(i):
			if i % thisPrime == 0:
				isCompositeFlag = True
				break
			thisPrime_idx += 1
			thisPrime = primes[thisPrime_idx]
		if not isCompositeFlag:
			primes.append(i)

		if pm == -1:
			i += 2
		else: # pm == 1
			i += 4
		
		pm *= -1
	
	return primes

def get_primes_less_than_builder(n):
	if n < 2: return []
	primes = [2]
	if n == 2: return primes
	primes.append(3)
	if n == 3: return primes

	i = 5
	while i < n:
		isCompositeFlag = False
		thisPrime_idx = 0
		thisPrime = primes[thisPrime_idx]
		while thisPrime <= math.sqrt(i):
			if i % thisPrime == 0:
				isCompositeFlag = True
				break
			thisPrime_idx += 1
			thisPrime = primes[thisPrime_idx]

		if not isCompositeFlag:
			primes.append(i)

		i+=2
	return primes

