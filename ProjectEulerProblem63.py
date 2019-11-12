"""
Project Euler Problem 63
How many n-digit positive integers exist which are also an n^th power?
"""

# note that this will NEVER work for a base of 10 (or greater)
# 10^1 = 10 (len = 2, n = 1); and multiplying by 10 adds 1 to both n and len

# so, how many n-digit positive integers exist which can be written as b^n, where 1 <= b <= 9?

# we can also note that if b^n contains fewer than n digits, then b^{n+1} will contain fewer than n+1 digits (since b < 10)
# (specifically, if b^n < 10^n, then b^{n+1} < 10^{n+1} because b < 10). This also proves that we eventually will find such an n

# Finally, ALL b is a solution for n == 1 (since they are all 1-digit numbers)

def solve():
	tot = 0
	for b in range(1, 10):
		n = 1
		while len(str(b**n)) == n:
			n += 1
		tot += n-1
		#print n-1
	return tot

print solve()

