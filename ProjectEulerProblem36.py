"""
Project Euler Problem 34 (Double-base palindromes)

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base2
"""
MAX = 1000000

# since we are not counting leading 0s, all such numbers must be odd




def solve():
	tot = 0
	for i in range(MAX):
		if str(i)[::-1] == str(i) and str(bin(i))[2:][::-1] == str(bin(i))[2:]:
			tot += i
	print tot

def solve_2():
	print sum([i for i in range(MAX) if (str(i)[::-1] == str(i) and str(bin(i))[2:][::-1] == str(bin(i))[2:])])



solve_2()

