"""
Project Euler Problem 104
(Pandigital Fibonacci Ends)
"""

def is_pandigital(num_str):
	"""
	Assumes num_str is 10 digits
	""" 
	has_digit = [False for i in range(10)]
	for dig in str(num_str):

		if has_digit[int(dig)]:
			return False
		has_digit[int(dig)] = True
	return True

def suffix_pandigital(fib):
	if len(str(fib)) < 10: return False
	return is_pandigital(str(fib)[-10:])


def prefix_pandigital(fib):
	if len(str(fib)) < 10:
		return False
	return is_pandigital(str(fib)[:10])
	

def solve():
	k = 2
	F_k = 1
	F_km1 = 1
	while not (suffix_pandigital(F_k) and prefix_pandigital(F_k)):
		#print k, F_k
		k += 1
		t = F_k 
		F_k = F_k + F_km1
		F_km1 = t
	return k

def test():
	print prefix_pandigital(1234567890)
	print not prefix_pandigital(12344567890)
	print suffix_pandigital(1234567890)
	print not suffix_pandigital(12344567890)
	pass

print solve()


