"""
Project Euler Problem 22
(Names Scores)
"""
def solve():
	names = process_input()
	names.sort()
	return sum((i+1) * get_score(names[i]) for i in range(len(names)))

def get_score(name):
	return sum(ord(ch) - ord("A") + 1 for ch in name)

def process_input():
	f = open("p022_names.txt", "r")
	text = f.read()
	split_text = text.split(",")

	# Remove the quotation marks
	for i in range(len(split_text)):
		split_text[i] = split_text[i][1:-1]
	return split_text


print solve()
