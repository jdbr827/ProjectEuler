"""
Project Euler Problem 669
"""
BIG_KNIGHTS_NUM = 99194853094755497 # <-- THIS IS A FIB NUM
K = 82
SEAT = 10,000,000,000,000,000
FIBS = []

def get_nth_fib():
	if n == 0: return 1
	last = 1
	this = 1
	i = 1
	while i < n:
		nxt = this + last
		last = this
		this = nxt
	return this


# F_K_MINUS_2 = get_nth_fib(K-2)
# F_K_MINUS_3 = get_nth_fib(K-3)
# F_K_MINUS_4 = get_nth_fib(K-4)
# F_K_PLUS_1 = get_nth_fib(K+1)


def get_fibs_up_to(n):
	if n == 0: return [1]
	fibs = [1, 1]
	if n == 1: return fibs
	for i in range(2, n+1):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs


# F[i-2] + a - F[i-3] = F[i-4] + a ?> F[i-2] <==>  a > F[i-2] - F[i-4] = F[i-3] + F[i-4] - F[i-4] = F[i-3] 
# a < F[i-1]


def solve(seat):
	"""
	Solves problem 82
	"""
	fibs = get_fibs_up_to(85)
	i = 1
	k = fibs[(K+1)] // 2

	k2 = fibs[K] - k
	print k2 > fibs[K-3]

	i += 1
	while True:
		print k, k > fibs[K-1]
		print fibs[K] - k
		if k > fibs[K-3]:
			if i < seat - 3:
				k -= fibs[K-3]
				i += 4
			elif i == seat-3:
				return 2*fibs[K-1] - k
			elif i == seat-2:
				return fibs[K-2] + k
			elif i == seat-1:
				return fibs[K-1] - k
			else:
				return k
		else:
			if i < seat - 5:
				k += fibs[K-4]
				i += 6
			else:
				print "YEER"
				return	



def fibonnacci_nums_leq(n):
	"""
	Prints all fibonnaci numbers <= n
	"""
	print 1
	num = 1
	if n == 1: return num
	a = 1
	b = 1
	c = a+b
	while c <= n:
		print c
		num += 1
		a = b
		b = c
		c = a + b
	return num



# LEM: for all i > 1; F_i+1 < 2*F_i



# LEM: if f1 is a fibonnacci number greater than 1, then there exists exactly one fibonnaci number f2, specifically the next fibonnacci number after f1, such that f1 < f2 < 2*f1

# Pf: Induction:
# Base Case: f1 = 2, 2*f1 = 4; f2 = 3
# Inductive Step:
# 

print solve(100)



