

def is_increasing(n):
	string = str(n)
	for i in range(len(string)):
		if string[i] != min(string[i:]):
			return False
	return True

def is_decreasing(n):
	string = str(n)
	for i in range(len(string)):
		if string[i] != max(string[i:]):
			return False
	return True

def is_bouncy(n):
	return (not is_increasing(n) and not is_decreasing(n))

def solve_112():
	num_bouncy = 0.0
	n = 99
	while num_bouncy / n != 0.99:
		n += 1
		if is_bouncy(n):
			num_bouncy += 1
	return n



	# number of non-bouncy numbers below 10^100 that start with a 9:
	# 9, 99, 999, ..., 99 9s. (99)

	# number of non-bouncy numbers below 10^100 that start with an 8:
	# number of non-bouncy numbers with k digits (1 <= k <= 99) that start with an 8:
	# k = 1 (just "8", so 1)
	# any other k, you can have the first 9 any of the k-1 other slots or none 

	# number of non-bouncy numbers below 10^100 that start with 7:
	# number of non-bouncy numbers with k digits (1 <= k <= 99) that start with a 7:
	# you have the first 8 at any of the slots 

# def num_increasing(first_num, num_digits):
# 	if num_digits == 1: return 1
# 	if first_num == 9: return 1
# 	return sum([num_increasing(first_num + 1, i) for i in range(1, num_digits)]) + 1


def num_increasing(first_num, num_digits):
	if num_digits == 1: return 1
	if first_num == 9: return 1

	# 7
	tot = 0
	for second_num in range(first_num, 10):
		tot += num_increasing(second_num, num_digits - 1)
	return tot


print num_increasing(9, 10)
print num_increasing(8, 7)	
print num_increasing(7, 4)
	# 7777
	# 7778
	# 7779



# S[i][j] := the number of increasing numbers whose first digit is i and has exactly j digits (including possibly leading 0s)

# thus, here, we can swap out each digit d for 9-d to get a 1-1 correspondence between increasing and decreasing nums
# (EXCEPT for single-digit nums and all 9s / all 0s)

# recurrence:
	#S[i][1] := 1 for all i (single-digit numbers)
	#S[9][j] := 1 for all j (all 9s)

	#S[i][j] := sum from k = i to 9 of S[k][j-1]


# for each increasing number inc with k < N digits (not counting leading 0s)
# you have, (inc.reverse())*(10**p) for 0 <= p <= N-k decreasing numbers
# for a total of N-k+1 non-bouncy numbers



def num_increasing_DP(max_ndigits):
	S = {first_digit : {n_digits : 0 for n_digits in range(1, max_ndigits + 1)} for first_digit in range(1, 10)}

	for first_digit in range(1, 10):
		S[first_digit][1] = 1 # single-digit nums
	for n_digits in range(1, max_ndigits + 1):
		S[9][n_digits] = 1 # all 9s

	for n_digits in range(2, max_ndigits + 1):
		for first_digit in range(8, 0, -1):
			S[first_digit][n_digits] = sum([S[second_digit][n_digits-1] for second_digit in range(first_digit, 10)])

	return S

#S[i][j] is the number of increasing numbers of exactly j digits (not counting leading 0s)



def solve_113(max_num_digits):
	S = num_increasing_DP(max_num_digits)
	#print S

	tot = 0
	for n_digits in range(2, max_num_digits + 1):
		for first_digit in range(1, 10):
			tot += S[first_digit][n_digits] * (2 + max_num_digits - n_digits)

	tot += 9 # single-digit numbers (which we don't want to count twice)
	
	return tot

print solve_113(6) 
print solve_113(10) 
print solve_113(100)








# tot = 0
# for i in range(1, 10):
# 	for num_digits in range(2, 101):
# 		tot += 2*num_increasing(i, num_digits)
# tot += 9 # single-digit numbers
# print tot
#print 10^100 - 1 - tot

#S[i][j] := the number of increasing numbers whose first digit is i and has exactly j digits.
# M[j] := the number of increasing numbers that has exactly j digits

# D[i][j] := the number of decreasing numbers whose first digit is i and has exactly j digits.

# is increasing to decreasing one-to-one? NO because you can have trailing but not leading 0s.


# def num_increasing_DP(max_ndigits):
# 	S = {first_num : {num_digits : 0 for num_digits in range(1, max_ndigits + 1)} for first_num in range(1, 10)}

# 	for j in range(1, max_ndigits + 1):
# 		S[9][j] = 1
# 	for i in range(1, 10):
# 		S[i][1] = 1

# 	for i in range(8, 1, -1):
# 		for j in range(2, max_ndigits + 1):
# 			S[i][j] = sum([S[i+1][k] for k in range(2, j+1)]) + 1

# 	return S

# S = num_increasing_DP(8)
# #print S


# # print S[8][7]
# # print S[7][4]



# print 2*sum([sum(S[i][j] for i in range(1, 10)) for j in range(2, 6+1)]) + 9




	# 8888888
	# 8888889
	# 8888899
	# 8888999
	# 8889999
	# 8899999
	# 8999999




#print solve_112()


