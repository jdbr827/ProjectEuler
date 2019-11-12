"""
Project Euler Problem 34 (Digit Factorials)
"""
import math

FACTORIAL = [math.factorial(i) for i in range(10)]

# UPPER BOUND: 10^7; 9! * 7 < 10^8

def get_digit_list(n):
	return [ord(i) - ord('0') for i in str(n)]

def brute_force(upper_bound):
	fact_sum_sum = 0
	for num in range(10, upper_bound):
		if sum(FACTORIAL[dig] for dig in get_digit_list(num)) == num:
			fact_sum_sum += num
	return fact_sum_sum


print brute_force(10**7)


