"""
Project Euler Problem 46 
(Goldbach's other conjecture)

What is the smallest odd compostie that cannot
be written as the sum of a prime and twice a square?
"""
from primes import isPrime

candidate = 3
primes = []
squares = [1, 4]
while True:
	if isPrime(candidate):
		primes.append(candidate)
	else:
		isGoldbach = False
		for square in squares:
			if candidate - 2*square in primes:
				isGoldbach = True
				break
		if not isGoldbach:
			print candidate
			break

	candidate += 2
	if candidate > (len(squares) + 1)**2:
		squares.append((len(squares) + 1) ** 2)




