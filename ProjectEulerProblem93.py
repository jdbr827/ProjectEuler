"""
Project Euler Problem 93 (Arithmetic Expressions)
"""
from collections import defaultdict
import itertools
import time
from argbestutil import argbest

OPMAP = {
	"+" : lambda a, b: a + b,
	"-" : lambda a, b: a - b,
	"*" : lambda a, b: a * b,
	"/" : lambda a, b: sneaky_division(a, b)}

# hmmm, what about inf - inf + d? Can that happen?
def sneaky_division(a, b):
	if b == 0 or b == float("inf") or b == -1 * float("inf"):
		return float("inf")
	return a / float(b)


def is_int(a):
	return a == int(a)


def process(m1, m2, m3, m4, op1, op2, op3):
	r1 = OPMAP[op3](OPMAP[op2](OPMAP[op1](m1, m2), m3), m4)  # ((m1 op1 m2) op2 m3) op3 m4
	r2 = OPMAP[op2](OPMAP[op1](m1, m2), OPMAP[op3](m3, m4))  # (m1 op1 m2) op2 (m3 op3 m4)
	r3 = OPMAP[op3](OPMAP[op1](m1, OPMAP[op2](m2, m3)), m4)  # (m1 op1 (m2 op2 m3)) op3 m4
	r4 = OPMAP[op1](m1, OPMAP[op3](OPMAP[op2](m2, m3), m4))  # m1 op1 ((m2 op2 m3) op3 m4)
	r5 = OPMAP[op1](m1, OPMAP[op2](m2, OPMAP[op3](m3, m4)))  # m1 op1 (m2 op2 (m3 op3 m4))
	return set([r1, r2, r3, r4, r5])

OPS = ["+", "-", "*", "/"]
DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def solve():
	(best, best_max_made) = argbest(
		list(itertools.combinations(DIGITS, 4)), # combinations given in sorted order
		lambda (a, b, c, d): smallest_unreachable_positive_integer(set([a, b, c, d])) - 1,
		max
		)
	return format_solution(best)


def format_solution(best):
	(a, b, c, d) = best
	return str(a) + str(b) + str(c) + str(d)

def smallest_unreachable_positive_integer(four_digit_set):
		made_map = reachable_positive_integers_map(four_digit_set)
		i = 1
		while made_map[i]:
			i += 1
		return i
		

def reachable_positive_integers_map(four_digit_set):
	made_map = defaultdict(bool)
	for (m1, m2, m3, m4) in list(itertools.permutations(four_digit_set)):
		for (op1, op2, op3) in list(itertools.product(OPS, repeat=3)):
			for r in process(m1, m2, m3, m4, op1, op2, op3):
				if r > 0 and r != float("inf") and is_int(r):
					made_map[int(r)] = True
	return made_map


def test_and_solve():
	made_map_1234 = reachable_positive_integers_map(set([1, 2, 3, 4]))
	t1 = made_map_1234[8]
	t2 = made_map_1234[14]
	t3 = made_map_1234[19]
	t4 = made_map_1234[36]
	t5 = max(made_map_1234) == 36
	t6 = (smallest_unreachable_positive_integer(set([1, 2, 3, 4])) == 29)
	if t1 and t2 and t3 and t4 and t5 and t6:
		start = time.clock()
		ans = solve()
		end = time.clock()
		print "Solution is: " + str(ans) + " (found in " + str(end - start) + " seconds)"
	else:
		print "TEST FAILURE:", 
		print t1, t2, t3, t4, t5, t6
	pass
test_and_solve()
#print list(itertools.product(OPS, repeat=3))