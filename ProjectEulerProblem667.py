"""
Project Euler Problem 668
"""
from primes import get_primes_less_than_builder

print max(get_primes_less_than_builder(10000000))
print get_primes_less_than_builder(10000000000)