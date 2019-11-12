"""
Project Euler Problem 684
(Inverse Digit Sum)
"""

def s(n):
	"""
	returns the smallest number that has digit sum n
	"""
	return (((n % 9) + 1) * 10**(n//9)) - 1

def bigS(n):
	"""
	returns sum k=1 to n of s(k)
	"""
	return sum(s(k) for k in range(1, n+1))

def bigS2(n):
	if n >= 9:
		return 45 * (10**(n//9 - 1)) #+ (n%9)*(10**(n//9))

print(s(10) == 19)
print(bigS(20) == 1074)


def m_ones(m):
	return sum(10**i for i in range(m))

def one_sum(n):
	"""
	returns sum from l = 1 to n of (l 1s)
	"""
	tot = 0
	for i in range(1, n+1):
		tot += m_ones(i)
		print(i, tot)
	return tot

def one_sum_2(n):
	

print(one_sum(50))

# for i in range(1, 50):
# 	print(i, bigS(i), bigS(i) - bigS(i-1))


