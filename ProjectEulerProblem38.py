"""
Project Euler Problem 38
(Pandigital Multiples)
"""
def solve():
	for b in range(9876, 9183, -1):
		myStr = str(b) + str(2*b)
		if isPandigital(myStr): return myStr
	return "918273645"

def isPandigital(myStr):
	for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		if i not in myStr:
			return False
	return len(myStr) == 9

print isPandigital("918273645")
print solve()