"""
Project Euler Problem 32
"""
from itertools import permutations
import time


# times location should never be after the midpoint, make max of times_location 5 (5-1 = 4)

def digit_list_to_int(dig_list):
	num = ""
	for dig in dig_list:
		num += dig
	return int(num)

def solve():
	perm = permutations("123456789")

	nums = []
	for p in list(perm):
		for times_location in range(1, 5):
			for equals_location in range(times_location+1, 9):
				multiplier_1 = p[:times_location]
				m1 = digit_list_to_int(p[:times_location])
				m2 = digit_list_to_int(p[times_location:equals_location])
				product = digit_list_to_int(p[equals_location:])
				if m1 * m2 == product:
					if product not in nums:
						nums.append(product)
	return sum(nums)


start = time.clock()
ans = solve()
end = time.clock()
print ("Solution: " + str(ans) + " (solved in " + str(end - start) + " seconds)")

# for i in list(perm):
# 	print i
