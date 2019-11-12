"""
funWithYield
"""

def generator(N):
	for i in range(1, N):
		if i % 2:
			yield i

g = generator(100)
for num in g:
	print(num)