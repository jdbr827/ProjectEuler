"""
Project Euler Problem 55
"""


def isLychrel(num):
	num = num + int(str(num)[::-1])
	for i in range(49):
		reverse = int(str(num)[::-1])
		if reverse == num:
			return False
		else:
			num += reverse
	return True

tot = 0
for i in range(0, 10000):
	if isLychrel(i):
		tot += 1
print tot



