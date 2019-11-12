"""
Project Euler Problem 49
(Prime Permutations)
"""
import primes
from collections import defaultdict

def get_digit_freq_tuple(num):
	digit_lst = [0 for i in range(10)]
	for digit in str(num):
		digit_lst[ord(digit) - ord("0")] += 1
	return tuple(digit_lst)




p = primes.get_primes_less_than_builder(10000)

# slice p just to get 4-digit numbers
i = 0
while p[i] < 1000: 
	i += 1
p = p[i:]


## perm_nums[some tuple] is the se
perm_nums = defaultdict(lambda : [])
for prime in p:
	perm_nums[get_digit_freq_tuple(prime)].append(prime)

#print dict(perm_nums)

for perm_lst in perm_nums.values():
	if len(perm_lst) >= 3:
		for i in range(len(perm_lst)-2):
			for j in range(i+1, len(perm_lst)-1):
				diff = perm_lst[j] - perm_lst[i]
				if perm_lst[j] + diff in perm_lst:
					print perm_lst[i], perm_lst[j], perm_lst[j] + diff





