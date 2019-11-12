"""
Project Euler Problem 44 (Pentagon Numbers)
"""

from collections import defaultdict

def pentagon(k):
	"""
	returns the kth pentagon number
	"""
	return k*((3*k)-1) / 2.0

def solve():
	p = [0, 1, 5]
	target = defaultdict(lambda : float("inf")) 
	best_val = float("inf")
	k = 2
	diff = 4
	while p[k] - p[k-1] < best_val:
		k += 1
		diff += 3
		nxt = p[-1] + diff
		i = 0
		j = k-2
		while i < j:
			if p[i] + p[j] < nxt: 
				i += 1
			elif p[i] + p[j] > nxt:
				j -= 1
			else:
				target[p[j] + nxt] = min(target[p[j] + nxt], i)
				i += 1
				j -= 1
		if target[nxt] != float("inf"):
			best_val = min(best_val, p[target[nxt]])
			print best_val
		p.append(nxt)
	return best_val

print solve()