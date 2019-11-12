"""
Project Euler Problem 92 
(Square Digit Chains)
"""


TEN_MILLION = 10000000

def digit_square_sum(num):
	digits = [int(d) for d in str(num)]
	return sum(d**2 for d in digits)

def square_digit_chain(n):
	"""
	Runs the square digit chain algorithm on n
	prints where it ends up (1 or 89)
	"""
	m = n
	while m != 1 and m != 89:
		m = digit_square_sum(m)
	return m

# Make a diGraph, each node has outdeg 1, (u, v) in E if square_add(v) = u
# run BFS from 89, see how many numbers are discovered



# G[i] is the set of all x s.t. digit_square_sum(x) = i




def dig_square_sum(digit_freq_table):
	return sum(SQUARES[d] * digit_freq_table[d] for d in digit_freq_table)

def num_nums_for_dft(digit_freq_table, n_digits):
	"""
	assumes sum(digit_freq_table.values()) == n_digits
	"""
	digits_used = 0
	possibilities = 1
	for dig in digit_freq_table:
		possibilities *= choose(n_digits - digits_used, digit_freq_table[dig])
		digits_used += digit_freq_table[dig]
	return possibilities

def choose(n, r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))




def bfs(G):
	visited = [False for i in range(568)]
	queue = []
	queue.append(89)
	while queue:
		this_num = queue.pop(0)
		if not visited[this_num]:
			visited[this_num] = True
			for n in G[this_num]:
				queue.append(n)
	return visited


SQUARES = [i**2 for i in range(10)]


def solve():
	G = {i: [] for i in range(567 + 1)} # 9**2 * 7, the largest first value anything will go to
	for num in range(568):
		G[digit_square_sum(num)].append(num)
	print "sup"
	visited = bfs(G)
	tot = sum(visited)
	print "hi", tot
	for num in range(568, TEN_MILLION):
		if visited[digit_square_sum(num)]:
			tot += 1
	print tot
	pass
#solve()


def solve_2():
	arr = [0 for i in range(TEN_MILLION)]
	arr[1] = 1
	arr[89] = 89
	for i in range(2, TEN_MILLION):

		chain = []
		j = i
		while not arr[j]:
			chain.append(j)
			j = digit_square_sum(j)
		for k in chain:
			arr[k] = arr[j]
		#print i, j, chain

	tot = 0
	for num in arr:
		if num == 89:
			tot += 1
	return tot

print solve_2()



