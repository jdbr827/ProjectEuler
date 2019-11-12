"""
Project Euler Problem 95 (Amicable Chains)
"""
from ProjectEulerProblem21 import sum_of_proper_divisors
# from argbestutil import argbest_generator
# from argbestutil import ArgbestFinder
# from argbestutil import argbest
import time

NOT_YET_DISCOVERED = 0

def solve5_helper(N):
	spd = [1] * N
	for f in range(2, N): #O(N)
		for i in range(2*f, N, f): #O(N/f) ~ O(N)
			spd[i] += f

	smallest_parent = [NOT_YET_DISCOVERED for i in range(N+1)]
	for a in range(1, N+1):
		b = a
		this_path = []
		while b < N and smallest_parent[b] == NOT_YET_DISCOVERED:
			smallest_parent[b] = a
			this_path.append(b)
			b = spd[b]
		if b < N and smallest_parent[b] == a: # we have a chain!
			yield this_path[this_path.index(b):]

def solve5(N):
	return min(max(solve5_helper(N), key=len))



def solve4_helper(N):
	smallest_parent = [NOT_YET_DISCOVERED for i in range(N+1)]
	for a in range(1, N+1):
		b = a
		this_path = []
		while b < N and smallest_parent[b] == NOT_YET_DISCOVERED:
			smallest_parent[b] = a
			this_path.append(b)
			b = sum_of_proper_divisors(b) 
		if b < N and smallest_parent[b] == a: # we have a chain!
			yield this_path[this_path.index(b):]

def solve4(N):
	return min(max(solve4_helper(N), key=len))

# def solve3(N):
	argbest_finder = ArgbestFinder(len, max)
	smallest_parent = [NOT_YET_DISCOVERED for i in range(N+1)]
	for a in range(1, N+1):
		b = a
		this_path = []
		while b < N and smallest_parent[b] == NOT_YET_DISCOVERED:
			smallest_parent[b] = a
			this_path.append(b)
			b = sum_of_proper_divisors(b)
		if b < N and smallest_parent[b] == a: # we have a chain!
			argbest_finder.add_candidate(this_path[this_path.index(b):])
	return min(argbest_finder.get_argbest())


def solve(N):
	best_len = 0
	best_val = 0
	parent = [NOT_YET_DISCOVERED for i in range(N+1)] # the smallest number from which i is reachable
	for a in range(1, N+1):
		b = a
		this_path = []
		while b < N and parent[b] == NOT_YET_DISCOVERED:
			parent[b] = a
			this_path.append(b)
			b = sum_of_proper_divisors(b)
		if b < N and parent[b] == a: # we have a chain!
			i = this_path.index(b)
			this_len = len(this_path) - i
			if this_len > best_len:
				best_len = this_len
				best_val = min(this_path[i:])
			#print a, this_len
	return best_val


start = time.clock()
ans = solve5(1000000)
end = time.clock()

print "Solution is: " + str(ans) + " (solved in " + str(end - start) + " seconds)"




#print sum_of_proper_divisors(28)