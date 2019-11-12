"""
Project Euler Problem 43
(Sub-String Divisibility)
"""
import itertools

def make_three_digit_num(perm, idx1, idx2, idx3):
	return 100*perm[idx1] + 10*perm[idx2] + perm[idx3]

def check_substring_divisibility_property(perm):
	return (
		make_three_digit_num(perm, 1, 2, 3) % 2 == 0 and
		make_three_digit_num(perm, 2, 3, 4) % 3 == 0 and
		make_three_digit_num(perm, 3, 4, 5) % 5 == 0 and
		make_three_digit_num(perm, 4, 5, 6) % 7 == 0 and
		make_three_digit_num(perm, 5, 6, 7) % 11 == 0 and
		make_three_digit_num(perm, 6, 7, 8) % 13 == 0 and
		make_three_digit_num(perm, 7, 8, 9) % 17 == 0
		)

def make_num(digit_tup):
	num = 0
	for i in range(1, 11):
		num += digit_tup[-1 *i] * (10**(i-1))
	return num

def solve():
	tot = 0
	for perm in itertools.permutations(range(0, 9+1)):
		if check_substring_divisibility_property(perm):
			print perm, make_num(perm)
			tot += make_num(perm)
	print tot
	pass

print check_substring_divisibility_property((1, 4, 0, 6, 3, 5, 7, 2, 8, 9))
solve()


