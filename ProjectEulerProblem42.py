"""
Project Euler Problem 42
"""
import time

def read_in():
	f = open("p042_words.txt", "r")
	raw_text = f.read()
	words = [word[1:-1] for word in raw_text.split(",")]
	return words

def is_triangle_number(i):
	if i < 1: return False
	if i == 1: return True
	runner = 1
	j = 2
	while runner < i:
		runner += j
		j += 1
	return runner == i

def is_triangle_word(word):
	"""
	Assumes word is in all caps
	"""
	num = sum(ord(ch) - ord("A") + 1 for ch in word)
	return is_triangle_number(num)


def solve():
	num_triangle_words = 0
	words = read_in()
	for word in words:
		if is_triangle_word(word):
			num_triangle_words += 1
	return num_triangle_words

start = time.clock()
ans = solve()
end = time.clock()

print("Solution: " + str(ans) + " (solved in " + str(end - start) + " seconds)")


