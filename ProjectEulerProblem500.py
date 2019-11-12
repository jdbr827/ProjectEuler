"""
Problem 500
(Problem 500!!! -- smallest number with 2^{500500} distinct divisors
(mod 500500507)
"""

# want: product of the first 500500 primes
import primes
import itertools




ps = primes.get_primes_less_than_sieve_efficient(10000000)
prod = 1
for i in range(500500):
	prod *= ps[i]
	prod %= 500500507
print prod

print (2**499499) % 500500507
