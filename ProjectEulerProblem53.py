"""
Values of C(n, r) exceeding 1 million for 1 <= n <= 100
"""

import math

def C(n, r):
	return math.factorial(n) / ( math.factorial(r) * math.factorial(n-r))


def solve(N):
	numnums = 0
	for n in range(1, N + 1):
		for r in range(n+1):
			num = C(n, r)
			if num > 1000000:
				numnums += 1
	return numnums


	# bignums = []
	# last = [1]
	# this = [1, 1]

	# for n in range(3, N+1):
	# 	last = this
	# 	this = [1]
	# 	this.extend([last[i] + last[i+1] for i in range(len(last)-1)])
	# 	this.append(1)
	# 	for num in this:
	# 		if num > 1000000:
	# 			#if num not in bignums:
	# 			bignums.append(num)
	# return len(bignums)
print C(5, 3) == 10
print C(23, 10) == 1144066
print solve(100)


