"""
Project Euler Problem 23
"""

# #Use sieve to get numbers proper divisors, or just keep track of sum
# MAX_UN_SUMMABLE = 28123

# sum_of_proper_divisors = [0 for i in range(MAX_UN_SUMMABLE+1)]
# is_abundant = [False for i in range(MAX_UN_SUMMABLE) + 1]
# abundant_sum_total = 0


# ## This code returns, for all i in the range, the sum of the proper divisors of i
# # it does so in at worst O(n^2) time
# for divisor in range(1, MAX_UN_SUMMABLE+1):
# 	product = 2 * divisor #2* to ensure only PROPER divisors
# 	while product <= MAX_UN_SUMMABLE:
# 		# order here is critical to ensure only PROPER divisors
# 		sum_of_proper_divisors[product] += divisor
#		product += divisor
		

# # INVAR: once we reach "divisor" in the outer for loop
# # sum_of_proper_divisors for everything up to and including divisor is correct, so we can 
# # check if it is abundant.

# 	if sum_of_proper_divisors[divisor] > divisor:
# 		is_abundant[divisor] = True

# # Finally, since everything before that is true, we can check from 1 (NOT 0) 
# # up to half (floor) the divisor to see if both that number and the divisor - it are 
# # abundant. If so, divisor can be written as the sum of two abundant numbers and may 
# # be added to abundant_sum_total
#	can_be_written = False
# 	for smaller_addend in range(1, (divisor // 2) + 1):
# 		if is_abundant[smaller_addend] and is_abundant[divisor - smaller_addend]:
# 			can_be_written = True
# 			break
#	if not can_be_written: abundant_sum_total += divisor

# # finally, just
# return abundant_sum_total


MAX_UN_SUMMABLE = 28123
def run():
	sum_of_proper_divisors = [0 for i in range(MAX_UN_SUMMABLE+1)]
	is_abundant = [False for i in range(MAX_UN_SUMMABLE+1)]
	no_abundant_sum_total = 0

	for divisor in range(1, MAX_UN_SUMMABLE):
		product = 2 * divisor
		while product <= MAX_UN_SUMMABLE:
			sum_of_proper_divisors[product] += divisor
			product += divisor

		if sum_of_proper_divisors[divisor] > divisor:
			is_abundant[divisor] = True

		has_abundant_sum = False
		for smaller_addend in range(1, (divisor // 2) + 1):
			if is_abundant[smaller_addend] and is_abundant[divisor - smaller_addend]:
				has_abundant_sum = True
				break
		if not has_abundant_sum:
			no_abundant_sum_total += divisor
	print no_abundant_sum_total
run()


