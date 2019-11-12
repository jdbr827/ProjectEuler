# num_recs(m, n) = 1 + num_recs(n-1, m) + num_recs(n, m-1)
# num_recs(0, m) = num_recs(0, n) = 0


def num_recs(n, m):
	if n == 0 or m == 0: return 0
	return 1 + 2*num_recs(n-1, m) - num_recs(n-2, m) + 2*num_recs(n, m-1) - num_recs(n, m-2) + num_recs(n-2, m-2)

print num_recs(3, 2)