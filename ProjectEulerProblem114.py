"""
Project Euler Problem 104
(Pandigital Fibonacci Ends)
"""

def is_pandigital(num):
	has_digit = [False for i in range(10)]
	for dig in str(num[:9]):
		if has_digit[int(dig)]:
			return False
		has_digit[int(dig)]
	return True


def prefix_pandigital(fib):
	if len(fib) < 9:
		return False
	return is_pandigital(fib[:9])
	

def solve():
	k = 2
	F_k = 1
	F_km1 = 1
	pass

def test():
	print prefix_pandigital(1234567890)
	print not prefix_pandigital(12344567890)
	pass

test()


