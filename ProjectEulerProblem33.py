"""
Project Euler Problem 33
"""


def do_digit_cancelling(numer, denom):

	n1 = numer // 10
	n2 = numer % 10
	d1 = denom // 10
	d2 = denom % 10

	if n1 == d1 and n1 != 0:
		return (n2, d2)
	if n1 == d2 and n1 != 0:
		return (n2, d1)
	if n2 == d1 and n2 != 0:
		return (n1, d2)
	if n2 == d2 and n2 != 0:
		return (n1, d1)
	return (-1, -1)


def is_digit_cancelling(numer, denom):
	(n, d) = do_digit_cancelling(numer, denom)
	if (n, d) == (-1, -1) or d == 0:
		return False

	return float(n) / d == float(numer) / denom


def solve():
	digit_cancelling_pairs = []
	for numer in range(10, 99):
		for denom in range(numer + 1, 99):
			if is_digit_cancelling(numer, denom):
				digit_cancelling_pairs.append((numer, denom))
	#print digit_cancelling_pairs

	prod_numer = 1
	prod_denom = 1
	for pair in digit_cancelling_pairs:
		prod_numer *= pair[0]
		prod_denom *= pair[1]

	print prod_numer, prod_denom

	# in this case, the solution happens to be trivial to simplify

	

solve()