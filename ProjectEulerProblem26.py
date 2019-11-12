"""
Project Euler Problem 26
"""

from collections import defaultdict
import sys

def parse_command_line():
	if sys.argv[1] == "-ld": # Long division
		denom = int(sys.argv[2])
		(answer_str, cycle) = long_divison_1_over(denom)
		if cycle != None: 
			print answer_str[:-len(cycle)] + "(" + cycle + ")"
		else:
			print answer_str

	if sys.argv[1] == "-len_longest_cycle_under":
		max_denom = int(sys.argv[2])
		longest_len = 0
		longest_len_val = None
		for i in range(2, max_denom+1):
			(answer_str, cycle) = long_divison_1_over(i)
			if cycle != None and len(cycle) > longest_len:
				longest_len = len(cycle)
				longest_len_val = i
		print longest_len_val
			


UNKNOWN = -1

def find_next_answer_and_remainder(denom, remainder):
	"""
	Given that long division of 1/denom has led us to a remainder of remainder, 
	will tell us the next "answer" (things to be added to it) and next remainder 
	in the long division
	"""
	# Let's figure out what it is

	# "drop another 0"
	ans = ""
	blown_up_remainder = remainder * 10
	while blown_up_remainder < denom: 
		blown_up_remainder *= 10
		ans += "0"

	ans += str(blown_up_remainder // denom)
	new_rem = blown_up_remainder % denom
	return ans, new_rem

def find_cycle(next_remainder, next_ans, start_remainder):
	"""
	Returns a cycle in the long division starting from start_remainder and based on next_remainder and next_ans.
	"""

	cycle = next_ans[start_remainder]
	moving_remainder = next_remainder[start_remainder]
	while moving_remainder != start_remainder:
		#print moving_remainder
		cycle += next_ans[moving_remainder]
		moving_remainder = next_remainder[moving_remainder]
	return cycle

			



def long_divison_1_over(denom):

	answer_str = "0."
	remainder = 1

	# for each possible remainder, we can memoize how it will get processed
	# (namely, what will get added to answer, and what the next remainder will be)

	next_ans = ["" for i in range(denom)]
	next_remainder = [UNKNOWN for i in range(denom)]

	while remainder != 0:
		if next_remainder[remainder] == UNKNOWN:
			(next_ans[remainder], next_remainder[remainder]) = find_next_answer_and_remainder(denom, remainder)
			answer_str += next_ans[remainder]

			# Update multiples of 10 of this remainder that will have similar ans/remainders.
			# This allows us to cut leading 0s when denom is a multiples of 10
			rem_copy = remainder
			while next_ans[rem_copy][0] == "0":
				next_ans[rem_copy * 10] = next_ans[rem_copy][1:]
				next_remainder[rem_copy * 10] = next_remainder[remainder]
				rem_copy *= 10

			remainder = next_remainder[remainder]

		else:
			cycle = find_cycle(next_remainder, next_ans, remainder)
			return answer_str, cycle
			
		

	# If we exit here, then the decimal terminates
	return (answer_str, None)


parse_command_line()

