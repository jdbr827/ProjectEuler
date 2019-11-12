"""
Project Euler Problem 357
"""

from primes import get_primes_less_than_sieve_efficient
from primes import isPrime

#N = 100000000
# note we need to go up to N+1 since N is a divisor of N, so we may check N + N/N = N+1
#prime_list = get_primes_less_than_sieve_efficient(N + 2)

# since d = 1 is a divisor of all numbers, we need 1 + n/1 = n+1 is prime
# thus we need only consider numbers that are 1 less than a prime

# since d = n is a divisor of all numbers, we need n + n/n = n+1 is prime, 
# so nothing new added here, we can ignore that

#candidates = [p - 1 for p in prime_list]
#print len(candidates)


def factors(n):
	return [d for d in range(1, n+1) if n%d == 0]


def is_prime_generating(n):
	for d in factors(n):
		if not isPrime(d + (n/d)):
			return False			
	return True

def interest(n):
	for i in range(n):
		if is_prime_generating(i):
			print i, factors(i)
	return 

print interest(200)

# seems that we are looking for squarefree numbers!
# if n = k(p^2)
# then p + n/p = p + kp^2 / p = p + kp = p(k+1) is divisible by p so not prime


