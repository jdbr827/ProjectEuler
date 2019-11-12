"""
Project Euler Problem 107 (minimal network)
"""
from unionfind import UnionFind
from graphviz import Digraph

NUM_VERTS = 40
NO_EDGE = -1



def read_in_edge_list_and_total_from_adjacency_matrix():
	"""
	returns a list of the edges in the graph in (v1, v2, w) form.
	"""
	f = open("p107_network.txt", "r")	
	edges = []
	total = 0
	for i in range(NUM_VERTS):
		line = f.readline()[:-1].split(",")
		for j in range(i+1, NUM_VERTS):
			if line[j] != "-":
				edges.append((i, j, int(line[j])))
				total += int(line[j])
	return (edges, total)

def mst_kruskall_uf(vertices, edge_list):
	"""
	edge_list is of the form (v1, v2, w)
	returns the mst as a set of edges of the form (v1, v2, w)
	"""
	edge_list.sort(key = lambda x: x[2])
	uf = UnionFind(lambda u, v: min(u, v))	
	mst_edges = set([])

	for v in vertices: uf.makeset(v)

	for edge in edge_list:
		(u, v, w) = edge
		if not uf.union(u, v):
			mst_edges.add(edge)
			if len(mst_edges) == NUM_VERTS - 1: return mst_edges
	return set([]) # error...no spanning tree exists.

def solve():
	(edges, total) = read_in_edge_list_and_total_from_adjacency_matrix()
	mst_edges = mst_kruskall_uf(range(NUM_VERTS), edges)
	plot_graphviz(mst_edges)
	return total - sum(w for (u, v, w) in mst_edges)


def plot_graphviz(edges):
	grph = Digraph()
	for (u, v, w) in edges:
		grph.edge(str(u), str(v), label=str(w))
	grph.render("PE107-graph", view=True)
	pass



import time
start = time.time()
ans = solve()
end = time.time()
print (ans, end-start)


