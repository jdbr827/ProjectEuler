
from collections import defaultdict

def solve(N):
	M = defaultdict(lambda : defaultdict(int))
	x = 0
	while 2*x <= N:
		y = 0
		while 2*x + 3*y <= N:
			z = 0
			while 2*x + 3*y + 5*z <= N:
				#print 2**x * 3**y * 5**z, x, y, z, x+y+z, 2*x +3*y + 5*z
				M[x+y+z][2*x+3*y+5*z] += 1
				z += 1
			y += 1
		x += 1
	print M
	tot = 0
	for r in M.keys():
		print r, M[r].keys()
		for s in M[r].keys():
			if s <= N // 2:
				tot += M[r][s] * M[r][N-s]
	return tot


print solve(10)
print solve(100)
#print solve(10**7)