"""
Project Euler Problem 673 (beds and desks)
"""
import unittest
from collections import defaultdict
import math
from graphviz import Graph


MOD = 999999937
# import them as a graph
# keep track of all CCs
# Isolated Nodes are one cat
# Paths with an odd number of nodes are one cat (for each number)
# Paths with an even number of nodes are separated by outsider (and have 2x symmetry)
# Cycles are one cat for each num and have symmetry number of nodes

def read_in():
	beds = [0 for i in range(500 + 1)]

	beds_file = open("p673_beds.txt", "r")
	for line in beds_file.readlines():
		nums = line[:-1].split(",")
		beds[int(nums[0])] = int(nums[1])
		beds[int(nums[1])] = int(nums[0])

	desks = [0 for i in range(500 + 1)]
	desks_file = open("p673_desks.txt", "r")
	for line in desks_file.readlines():
		nums = line[:-1].split(",")
		desks[int(nums[0])] = int(nums[1])
		desks[int(nums[1])] = int(nums[0])

	return beds, desks

def to_array_from_edge_list(edge_list, N):
	arr = [0 for i in range(N+1)]
	for (u, v) in edge_list:
		arr[int(u)] = int(v)
		arr[int(v)] = int(u)
	return arr

def to_graph(beds, desks, filename):
	N = len(beds)
	g = Graph()
	for i in range(1, N):
		g.node(str(i))
	for i in range(1, N):
		if beds[i] != 0 and i < beds[i]:
			g.edge(str(i), str(beds[i]), color='blue')
		if desks[i] != 0 and i < desks[i]:
			g.edge(str(i), str(desks[i]), color='green')
	g.render(filename, view=True);
	pass

def get_connected_component_types(beds, desks):
	"""
	given the type of the problem, we care about 5 types of connected components:
	- Isolated Nodes
	- paths that start with a bed connection and end with a bed connection (separated by length)
	- paths that start with a desk connection and end with a desk connection (separated by length)
	- paths that start with a bed connection and end with a desk connection (separated by length) [the reverse is symmetrically here as well]
	- cycles (spearated by length)

	We return in order, those 5 things. The isolated nodes as an integer, the others as dicitonaries
	mapping lengths to the number of CCs of that type and length
	"""
	N = len(beds)
	visited = [False for i in range(N+1)]

	num_isolated_nodes = 0
	bb= defaultdict(int) # number of blue-blue paths of length l
	gg = defaultdict(int) # number of green-green paths of length l
	odds = defaultdict(int) # number of odd-length (blue-green) paths of length l
	cycles = defaultdict(int) # number of cycles of length l

	for i in range(1, N):
		if visited[i] or (beds[i] != 0 and desks[i] != 0):
			continue

		visited[i] = True

		if beds[i] == 0 and desks[i] == 0:
			num_isolated_nodes += 1
			print(str(i))
			continue

		l = 2
		if beds[i] != 0:
			j = beds[i]
			while True:
				visited[j] = True
				if desks[j] == 0:
					bb[l] += 1
					break
				visited[desks[j]] = True
				l += 1
				if beds[desks[j]] == 0:
					odds[l] += 1
					break
				j = beds[desks[j]]
				l += 1

		else: # desks[i] != 0:
			j = desks[i]
			while True:
				visited[j] = True
				if beds[j] == 0:
					gg[l] += 1
					break
				visited[beds[j]] = True
				l += 1
				if desks[beds[j]] == 0:
					odds[l] += 1
					break
				j = desks[beds[j]]
				l += 1

	# cycles
	for i in range(1, N):
		if visited[i]:
			continue
		else:
			# print(i)
			# print ("-----")
			visited[i] = True
			l = 2
			j = i
			while beds[desks[j]] != i:
				l += 2
				visited[desks[j]] = True
				visited[beds[desks[j]]] = True
				j = beds[desks[j]]
			visited[desks[j]] = True
			cycles[l] += 1

	# print("Number of Isolated Nodes:" + str(num_isolated_nodes))
	# print("Blue/Blue Paths:" + str(dict(bb)))
	# print("Green/Green Paths:" + str(dict(gg)))
	# print("Odd Length Paths:" + str(dict(odds)))
	# print("Cycles:" + str(dict(cycles)))

	return (num_isolated_nodes, bb, gg, odds, cycles)



def solve2(beds, desks):
	(num_isolated_nodes, bb, gg, odds, cycles) = get_connected_component_types(beds, desks)

	# any isolated node can (only) be mapped to another isolated node	
	tot = math.factorial(num_isolated_nodes)

	# any blue-blue path can be mapped to another blue-blue path of the same length (factorial)
	# then, each one can be either kept in place or reversed (2**val)
	for val in bb.values(): tot *= math.factorial(val) * 2**val

	# any green-green path can be mapped to another green-green path of the same length (factorial)
	# then, each one can be either kept in place or reversed (2**val)
	for val in gg.values(): tot *= math.factorial(val) * 2**val

	# any blue-green path can be mapped to another blue-green path of the same length (factorial)
	# note tho that it CANNOT be reversed
	for val in odds.values(): tot *= math.factorial(val) 

	# any cycle can be mapped to another cycle of the same length (Factorial)
	# and can be rotated cyclically to ANY other position (l**val)
	for (l, val) in cycles.items(): tot *= math.factorial(val) * l**val


	return tot

TOGRAPH = False

class PE673Test(unittest.TestCase):


	def test_easy(self):
		beds = to_array_from_edge_list([(1,2),(3,4),(5,6)], 6)
		desks = to_array_from_edge_list([(3,6),(4,5)], 6)
		if TOGRAPH:
			to_graph(beds, desks, "PE673_easyTest")
		self.assertEqual(solve2(beds, desks), 8)

	def test_medium(self):
		beds = to_array_from_edge_list([(2,13),(4,30),(5,27),(6,16),(10,18),(12,35),(14,19),(15,20),(17,26),(21,32),(22,33),(24,34),(25,28)], 36)
		desks = to_array_from_edge_list([(1,35),(2,22),(3,36),(4,28),(5,25),(7,18),(9,23),(13,19),(14,33),(15,34),(20,24),(26,29),(27,30)], 36)
		if TOGRAPH:
			to_graph(beds, desks, "PE673_mediumTest")
		self.assertEqual(solve2(beds, desks), 663552)

	def test_answer(self):
		(beds, desks) = read_in()
		if TOGRAPH:
			to_graph(beds, desks, "PE673_answer")
		self.assertEqual(solve2(beds, desks) % MOD, 700325380)


suite = unittest.TestLoader().loadTestsFromTestCase(PE673Test)
unittest.TextTestRunner(verbosity=2).run(suite)