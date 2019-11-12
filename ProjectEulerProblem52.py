"""
Project Euler Problem 52 (Permuted Multiples)
"""

def get_digit_freq_tuple(num):
	digit_lst = [0 for i in range(10)]
	for digit in str(num):
		digit_lst[ord(digit) - ord("0")] += 1
	return tuple(digit_lst)


### We obviously need x, 2x, ..., 6x to have the same NUMBER of digits, so we go by power of 10 and divide by 6 for a max

def solve():
	ten_pow = 0
	while True:
		for x in range(10**(ten_pow), (10**(ten_pow + 1) // 6) + 1):
			dig_freq_tuple = get_digit_freq_tuple(x)
			isWinner = True
			for k in range(2, 7):
				if get_digit_freq_tuple(k*x) != dig_freq_tuple:
					isWinner = False
					break
			if isWinner:
				return x
		ten_pow += 1

print solve()



