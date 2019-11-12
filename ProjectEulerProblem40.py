"""
Project Euler Problem 40 (Champernowe's Constant)
"""

# first 9 nums .. 1 digit
# next 90... 2 digits
# next 900 ... 3 digits

# 9 + (90*2) +

# 

import math

# def d(n):
# 	"""
# 	Returns the nth digit of the fractional part of Champernowne's constant
# 	ASSUMES n a positive integer
# 	"""
# 	num = 1
# 	counter = 1
# 	pow_of_10 = 0
# 	digit_idx = 0
# 	while True:
# 		this_digit = int(str(num)[digit_idx])
# 		#print num, counter, pow_of_10, digit_idx, this_digit
# 		if counter == n:
# 			return this_digit
# 		else:
# 			counter += 1
# 			if digit_idx < pow_of_10:
# 				digit_idx += 1
# 			else:
# 				num += 1
# 				digit_idx = 0
# 				pow_of_10 = int(math.log(num, 10))
# 	pass

def d3(n):
	"""
	Returns the nth digit of the fractional part of Champernowne's constant
	ASSUMES n a positive integer
	"""
	champernowe_string_fractional = ""
	for i in range(1,n+1):
		champernowe_string_fractional += str(i)
	#print champernowe_string
	return int(champernowe_string_fractional[n-1]) # since string is 0-indexed

print d3(1000000) * d3(100000) * d3(10000) * d3(1000) * d3(100) * d3(10) * d3(1)


def d2(n):
	"""
	Returns the nth digit of the fractional part of Champernowne's constant
	ASSUMES n a positive integer
	"""
	num = 1
	counter = 1
	pow_of_10 = 0
	digit_idx = 0
	for _ in range(1, n):
		if digit_idx < pow_of_10:
			digit_idx += 1
		else:
			num += 1
			digit_idx = 0
			pow_of_10 = int(math.log(num, 10))
	return int(str(num)[digit_idx])


# print d(1000)#, d(10000), d(100000), d(1000000)
# print d(1) * d(10) * d(100) * d(1000) * d(10000) *  d(100000) * d(1000000)
# # print 15 * 14 * 8

		
