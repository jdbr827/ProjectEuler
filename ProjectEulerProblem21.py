"""
Project Euler Problem 21 (Amicable Pairs)
"""

def sum_of_divisors(n):
	tot = 1
	p = 2
	while p**2 <= n and n > 1:
		if n % p == 0:
			j = p**2
			n /= p
			while n % p == 0:
				j *= p
				n /= p
			tot *= j-1
			tot /= p-1
		if p == 2: 
			p = 3
		else: 
			p += 2
	if n > 1: 
		tot *= (n+1)
	return tot

def sum_of_proper_divisors(n):
	return sum_of_divisors(n) - n

def solve(N):
	tot = 0
	for a in range(2, N):
		b = sum_of_proper_divisors(a)
		if b > a and sum_of_proper_divisors(b) == a:
			tot += a + b
	return tot

#print solve(10000)

