from graphviz import Digraph

def g(bool6):
	(a, b, c, d, e, f) = bool6
	return (b, c, d, e, f, a ^ (b and c))

def bool6_to_int(b6):
	(a, b, c, d, e, f) = b6
	return f + 2*e + 4*d + 8*c + 16*b + 32*a

def inverse_bool6_to_int(num):
	a = num//32
	b = (num - 32*a) // 16
	c = (num - 32*a - 16*b) // 8
	d = (num - 32*a - 16*b - 8*c) // 4
	e = (num - 32*a - 16*b - 8*c - 4*d) // 2
	f = (num - 32*a - 16*b - 8*c - 4*d - 2*e)
	return (a, b, c, d, e, f)

def num_g(num):
	return bool6_to_int(g(inverse_bool6_to_int(num)))


def check_bool6_to_int_and_inverse():
	for num in range(64):
		if bool6_to_int(inverse_bool6_to_int(num)) != num:
			print("ERROR: bool6_to_int and inverse_bool6_to_int are not inverses for " + str(num))
			return False
	return True



def get_cycle_lens():
	cycle_lens = []
	marked = [False for i in range(64)]
	for i in range(64):
		if not marked[i]:
			marked[i] = True
			this_cycle_len = 1
			j = num_g(i)
			while j != i:
				marked[j] = True
				this_cycle_len += 1
				j = num_g(j)
			cycle_lens.append(this_cycle_len)
	return cycle_lens

print(get_cycle_lens())

def fib(n):
	vals = [1, 2, 3]
	if n <= 2:
		return vals[n]
	for _ in range(n-2):
		vals.append(vals[-1] + vals[-2])
	return vals



def solve():
	cycle_lens = get_cycle_lens()
	vals = fib(max(cycle_lens))
	tot = 1
	for l in cycle_lens:
		if l == 1: 
			tot *= 1
		elif l == 2:
			tot *= 3
		else:
			tot *= vals[l-1] + vals[l-3]
			print(vals[l-1] + vals[l-3])
	return tot

print("SOLUTION:" + str(solve()))



graph = Digraph()
for num in range(64):
	graph.edge(str(num), str(bool6_to_int(g(inverse_bool6_to_int(num)))))
graph.render("PE209-graph", view=True)
