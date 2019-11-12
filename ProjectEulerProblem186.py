"""
Project Euler Problem 186 (Connectedness of a Network)
"""
import unionfind

class UnionBySize(UnionFind):

	def __init__(self, union_func = lambda a, b: a):
		"""
		union_func is the function that determines which element gets picked in a union.
		"""
		self.size = {} # size only valid while parent is valid
		super().__init__(union_func)
		pass

	def union(self, a, b):
		"""
		Returns True if root(a) already equaled root(b),
		False otherwise
		"""
		ans = super().union(a, b)
		self.size[self.parent[a]]= self.size[a] + self.size[b]
		return ans


def LaggedFibonacciGenerator:

	def __init__(self):
		self.k = 1
		self.starters = [0].extend((100003 - 200003*k + 300007*(k**3)) % 1000000)

	def nxt(self):
		if self.k <= 55:
			return 
		else:
			return 

