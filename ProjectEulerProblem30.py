
FIFTHS = [i ** 5 for i in range(10)]
print FIFTHS



# at the value of i found here, we can cap the growth
def find_cap():
	n_digits = 1
	i = 9
	sf = FIFTHS[9]
	while i < sf:
		#print n_digits, i, sf
		n_digits += 1
		i *= 10
		i += 9
		sf += FIFTHS[9]
	return n_digits

### We find that it find_cap() == 6

def is_fifth_sum(num):
	digits = [int(d) for d in str(num)]
	return sum(FIFTHS[d] for d in digits) == num

sum_fifth_nums = []
for d1 in range(10):
	for d2 in range(10):
		for d3 in range(10):
			for d4 in range(10):
				for d5 in range(10):
					for d6 in range(10):
						digits = [d1, d2, d3, d4, d5, d6]
						num = sum(digits[i] * (10**(5-i)) for i in range(6))
						if num == sum(FIFTHS[d] for d in digits):
							sum_fifth_nums.append(num)

print sum_fifth_nums
print sum(sum_fifth_nums) - 1

	

