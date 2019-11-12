"""
Project Euler Problem 29
"""

def brute_force(A, B): #O((AB)^2)
	nums = []
	for a in range(2, A+1): #O(A)
		for b in range(2, B+1): #O(B)
			thisnum = a ** b 
			if thisnum not in nums: #O(AB)
				nums.append(thisnum)
	return len(nums)

def solve(func):
	if func(5, 5) == 15:
		return func(100, 100)
	return "ERROR: func(5, 5) = ", func(5, 5), "!= 15"

print solve(brute_force)


# Basically Exactly like the sieve

# because 2^2 = 4, any values of b for a=4 will be a duplicate of a value of 2


# Insight here: for no value of a is a^MAX < MAX
#MAX = 5
MAX = 500


# def binary_insert(lst, k):
# 	"""
# 	binary insert k into a sorted list 
# 	(or do nothing if it is a duplicate)
# 	"""
# 	if lst == []: return [k]
# 	if k > lst[-1]: 
# 		lst.append(k)
# 		return lst

# 	n = len(lst)
# 	i = 0
# 	j = n-1
# 	mid = (i+j) // 2


# 	while i <= j:
# 		print i, j, mid
# 		if lst[mid] == k:
# 			return lst # already exists
# 		if lst[mid] < k:
# 			i = mid + 1
# 		elif lst[mid] > k:
# 			j = mid - 1

# 		mid = (i+j) // 2

# 	lst.insert(mid, k)
# 	return lst


# up to 2 ** 1000, then 4**[500, 1000], then 8**[, 1000], then 16**[500, 1000]...

# so if i == a ^b for some a, b both between 2 and 1000, 


# def solve():
# 	distinct_nums = []
# 	for a in range(2, MAX):
# 		for b in range(2, MAX):
# 			num = a ** b
# 			if num not in distinct_nums:
# 				distinct_nums.append(num)
# 	print len(distinct_nums)


# solve()


# is_viable_a = [True for a in range(MAX + 1)]

# total_nums = 0
# for a in range(2, MAX+1):
# 	if not is_viable_a: continue
# 	apowb = a
# 	for b in range(2, MAX+1):
# 		apowb *= a
# 		print apowb
# 		total_nums += 1
# 		if apowb <= MAX:
# 			is_viable_a[apowb] = False
# 		else:
# 			total_nums += MAX - b + 1
# 			break
# print total_nums

