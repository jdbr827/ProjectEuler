
def solve3():
	T = 1
	Tn = 1
	P = 1
	Pn = 1
	H = 1
	Hn = 1
	found = set([])
	while len(found) < 2:
		# update the sequence whose most recent element is smallest
		M == min(T, P, H):
		if M == T:
			Tn += 1
			T = Tn * (Tn+1) / 2
		elif M == P:
			Pn += 1
			P = Pn * ((3*Pn)-1) / 2
		elif H == P:
			Hn += 1
			H = Hn*((2*Hn)-1)
		# check to see if we have found a number
		if T == P and T == H:
			found.add(T)
	return found, Tn, Pn, Hn


def solve2():
	T = 1
	Tn = 1
	P = 1
	Pn = 1
	H = 1
	Hn = 1
	found = set([])
	while len(found) < 2:
		if T <= P and T <= H:
			Tn += 1
			T = Tn * (Tn+1) / 2
		elif P <= T and P <= H:
			Pn += 1
			P = Pn * ((3*Pn)-1) / 2
		elif H <= T and H <= P:
			Hn += 1
			H = Hn*((2*Hn)-1)
		if T == P and T == H:
			found.add(T)
	return found, Tn, Pn, Hn

def solve():
	T = [1]
	P = [1]
	H = [1]
	found = set([])
	while len(found) < 2:
		if T[-1] <= P[-1] and T[-1] <= H[-1]:
			n = len(T) + 1
			next_elm = n * (n+1) / 2
			T.append(next_elm)
		elif P[-1] <= T[-1] and P[-1] <= H[-1]:
			n = len(P) + 1
			next_elm = n * ((3*n)-1) / 2
			P.append(next_elm)
		elif H[-1] <= T[-1] and H[-1] <= P[-1]:
			n = len(H) + 1
			next_elm = n*((2*n)-1)
			H.append(next_elm)
		if T[-1] == P[-1] and T[-1] == H[-1]:
			found.add(next_elm)
	return found, next_elm

print solve2()
