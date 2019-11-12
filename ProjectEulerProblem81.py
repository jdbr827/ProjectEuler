"""
Solution to Project Euler Problem 81
"""

LEN = 80
WIDTH = 80

def solve():
	M = read_in()
	#print M
	#print two_way_path_sum(M)
	print Dijkstra(M, neighbor_function_81, end_condition_81)
	print Dijkstra(M, neighbor_function_82, end_condition_82, start_options_82)
	print Dijkstra(M, neighbor_function_83, end_condition_83)

def read_in():
	f = open("p081_matrix.txt", "r")
	
	M = []
	for i in range(LEN):
		M.append([int(st) for st in f.readline()[:-1].split(",")]) #[:-1] gets rid of '\n' char
	return M


def end_condition_83(i, j, n):
	return i == n-1 and j == n-1

def neighbor_function_83(i, j, n):
	nbrs = []
	if i != n-1: nbrs.append((i+1, j))
	if j != n-1: nbrs.append((i, j+1))
	if i != 0: nbrs.append((i-1, j))
	if j != 0: nbrs.append((i, j-1))
	return nbrs


def end_condition_82(i, j, n):
	return j == n-1

def neighbor_function_82(i, j, n):
	nbrs = []
	if i != n-1: nbrs.append((i+1, j))
	if j != n-1: nbrs.append((i, j+1))
	if i != 0: nbrs.append((i-1, j))
	return nbrs

def start_options_82(n):
	return [(i, 0) for i in range(n)]


def end_condition_81(i, j, n):
	return i == n-1 and j == n-1

def neighbor_function_81(i, j, n):
	nbrs = []
	if i != n-1: nbrs.append((i+1, j))
	if j != n-1: nbrs.append((i, j+1))
	return nbrs 

def Dijkstra(M, neighbor_function, end_condition, start_options = lambda n: [(0, 0)]):
	n = len(M)
	D = [[float("inf") for j in range(n)] for i in range(n)]
	best_prev = [[None for j in range(n)] for i in range(n)]
	candidates = []

	for option in start_options(n):
		candidates.append(option)
		D[option[0]][option[1]] = M[option[0]][option[1]]
	while True:
		#print D
		# find the new best thing
		best_val = float("inf")
		best = (None, None)

		for candidate in candidates:
			(i, j) = candidate
			if D[i][j] < best_val:
				best_val = D[i][j]
				best = (i, j)
		(i, j) = best
		candidates.remove(best)
		#print best, best_prev[i][j]

		if end_condition(i, j, n):
			# print M
			# print D
			return D[i][j]

		for nbr in neighbor_function(i, j, n):
			nbr_i = nbr[0]
			nbr_j = nbr[1]
			if D[nbr_i][nbr_j] == float("inf"):
				candidates.append(nbr)
			if D[i][j] + M[nbr_i][nbr_j] <= D[nbr_i][nbr_j]:
				D[nbr_i][nbr_j] = D[i][j] + M[nbr_i][nbr_j]
				best_prev[nbr_i][nbr_j] = (i, j)



	# Execution should never get here
	pass






def two_way_path_sum(M):
	S = [[0 for i in range(WIDTH)] for j in range(LEN)]
	S[LEN - 1][WIDTH - 1] = M[LEN - 1][WIDTH - 1]
	for i in range(LEN - 2, -1, -1): 
		S[i][WIDTH - 1] = S[i+1][WIDTH - 1] + M[i][WIDTH - 1]

	for j in range(WIDTH - 2, -1, -1):
		S[LEN - 1][j] = M[LEN - 1][j] + S[LEN - 1][j+1]
		for i in range(LEN - 2, -1, -1):
			S[i][j] = M[i][j] + min(S[i+1][j], S[i][j+1])

	#print S
	return S[0][0]



# print Dijkstra(
# 	[[131, 673, 234, 103, 18],
# 	[201, 96, 342, 965, 150],
# 	[630, 803, 746, 422, 111],
# 	[537, 699, 497, 121, 956],
# 	[805, 732, 524, 37, 331]], neighbor_function_82, end_condition_82, start_options_82)

solve()