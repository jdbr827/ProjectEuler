

def solve(N):
	W = {n : {l : 0 for l in range(1, n+1)} for n in range(1, N+1)}
	W[1][1] = 1
	for n in range(2, N+1):
		W[n][1] = 1
		for l in range(2, n):
			W[n][l] = sum([W[n-k][k] for k in range(1, min(l, n//2) + 1)])
		W[n][n] = 1 + W[n][n-1]
		print n, W[n]
	return W
print solve(5) == 6
#print solve(100)



# # KRQ what is the largest positive integer used in the sum?
# # possible answers: 1, ..., n
# # if answer is k, then we need number of ways that n-k can be written 
# # as the sum of at least one positive integer, none greater than k.
# # f(n-k, k)
# # take the sum over all possibilities


# :
# 	"""
# 	The number of ways that n can be written as 
# 	the sum of at least ONE positive integer, none of which 
# 	are greater than cap
# 	"""
# 	if cap > n: return num_sum_cap(n, n)
# 	if n == 0: return 0
# 	if cap == 1: return 1 # all 1s

# 	# KRQ what is the largest integer used 
# 	return sum(num_sum_cap(n-k, k) for k in range(1, cap+1))

# print num_sum_cap(5, 5)