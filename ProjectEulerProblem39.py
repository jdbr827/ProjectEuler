"""
Project Euler Problem 39

For what value of p <= 1000, is the number of right
triangles with integer lengths and perimeter p maximized?
"""
import math
#from argbestutil import argbest
import time


def num_integer_right_triangles_with_permiter(p):
	num = 0
	for a in range(1, int((1-(math.sqrt(2) / 2.0))*p)+1):
		b = (2*a*p - p**2) / float(2*a - 2*p)
		if b == int(b):
			num += 1
	return num 

def get_num_solutions_smarter_cleaner(n):
	return max(range(2, n+1,2), key=num_integer_right_triangles_with_permiter)

start = time.clock()
ans = get_num_solutions_smarter_cleaner(1000)
end = time.clock()
print "Solution is " + str(ans) + " (computed in " + str(end - start) + " seconds)"

# def get_num_solutions(n):
# 	(arg, best) = argbest(range(1, n+1), num_integer_right_triangles_with_permiter, max)
# 	return arg


# def get_num_solutions_smarter(n):
# 	(arg, best) = argbest(range(2, n+1, 2), num_integer_right_triangles_with_permiter, max)
# 	return arg




# def solve():
#         """
#         Solves Project Euler Problem 39
#         """
# 	best = 0
# 	argbest = 0
# 	for p in range(1, 1000+1):
# 		thisnum = 0
# 		for a in range(1, int((1-(math.sqrt(2) / 2.0))*p)+1):
# 			b = (2*a*p - p**2) / float(2*a - 2*p)
# 			if b == int(b):
# 				thisnum += 1
# 		if thisnum > best: 
# 			best = thisnum
# 			argbest = p
# 	return argbest


# def get_num_solutions_best_I_think(n):
# 	best = 0
# 	argbest = 0
# 	for p in range(1, n+1):
# 		thisnum = 0
# 		for a in range(1, int((1-(math.sqrt(2) / 2.0))*p)+1):
# 			b = (2*a*p - p**2) / float(2*a - 2*p)
# 			if b == int(b):
# 				thisnum += 1
# 		if thisnum > best: 
# 			best = thisnum
# 			argbest = p
# 	return argbest

#rint get_num_solutions_best_I_think(1000)



# def get_num_solutions(p, method):
# 	"""
# 	Returns the number of right triangles
# 	with integer lengths and perimiter p.
# 	"""
# 	if method == BRUTE_FORCE_METHOD:
# 		return get_num_solutions_brute_force(p)
# 	elif method == KEEP_INPUTS_ORDERED:
# 		return get_num_solutions_keep_inputs_ordered(p)
# 	elif method == TRIANGLE_INEQUALITY_THEOREM_METHOD:
# 		return get_num_solutions_triangle_inequality(p)
# 	else:
# 		return 0

# # def num_triplets_for_perimeter(p):
# # 	num_triplets = 0
# #     for a in range(1, p):
# #       b = float(2*a*p - p**2) / float(2*a - 2*p)  
# #       c = p - a - b 
# #       if (a <= b and b <= c  #Simplifying Assumptions
# #           and a + b > c      #Triangle Inequality 
# #           and b == int(b)):  #b must be an integer
# #         num_triplets += 1
# #     return num_triplets


# def solve2():
#   best = 0 
#   argbest = 0
#   for p in range(1, 1000 + 1):
#     this = num_triplets_for_perimeter(p)
#     if this > best:
#        best = this
#        argbest = p
#   return argbest

# def solve(p):
# 	"""
# 	Returns the number of right triangles
# 	with integer lengths and perimiter p.
# 	"""
# 	num_sols = 0
# 	for a in range(1, p):
# 		b = float(2*a*p - p**2) / float(2*a - 2*p)
# 		if b != int(b):
# 			continue
# 		c = p - a - b
# 		if (a <= b and a + 2*b <= p 
# 			and a + b > p // 2):
# 			num_sols += 1
# 	return num_sols



# def get_num_solutions_triangle_inequality(p):
# 	"""
# 	Returns the number of right triangles
# 	with integer lengths and perimiter p.
# 	"""
# 	# TRIANGLE INEQUALITY: a+b > c
# 	# keeping inputs ordered: a <= b <= c
# 	num_sols = 0
# 	for a in range(1, 1001):
# 		for b in range(1, 1001):
# 			if a <= b and a + 2*b <= p and a + b > p // 2 and a**2 + b**2 == (p-a-b)**2:
# 				num_sols += 1
# 	return num_sols






# def get_num_solutions_keep_inputs_ordered(p):
# 	"""
# 	Returns the number of right triangles
# 	with integer lengths and perimiter p.
# 	"""

# 	num_sols = 0
# 	# a <= b <= c
# 	for a in range(1, p // 3):
# 		for b in range(a, (p - a) // 2):
# 			c = p - a - b

# 			### begin error-check block
# 			if a > b or b > c or a > c:
# 				print "ERROR:", a, b, c

# 			if a**2 + b**2 == c**2:
# 				num_sols += 1
# 	return num_sols



# def get_num_solutions_brute_force(p): 
# 	"""
# 	Returns the number of right triangles
# 	with integer lengths and perimiter p.
# 	"""
# 	sols = []
# 	for a in range(1, p):
# 		for b in range(a, p): 
# 			c = p - a - b # perimiter calculation
# 			if a**2 + b**2 == c**2: 
# 				this_sol = [a, b, c]
# 				this_sol.sort()
# 				if this_sol not in sols: 
# 					sols.append(this_sol)
# 	return len(sols)

# def test():
# 	print get_num_solutions_brute_force(120) == 3
# 	print get_num_solutions_keep_inputs_ordered(120) == get_num_solutions_brute_force(120)
# 	print solve(120) == 3
# 	best_p = -1
# 	most_sols = -1
# 	for i in range(1, 1001):
# 		this_sols = solve(i)
# 		if this_sols > most_sols:
# 			most_sols = this_sols
# 			best_p = i
# 	print best_p

# #test()
# print solve2()
