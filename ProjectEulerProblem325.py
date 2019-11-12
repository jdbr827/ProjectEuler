import sys
import math

TEST_CASES_SG = [
	((1, 5), True),
	((2, 6), True),
	((3, 12), True),
	((2, 3), False),
	((3, 4), False)
	]

def print_help_message():
	msg = "Solver for Project Euler Problem 325 (Stone Game 2)\n"
	msg += "-h : Print's this help message!\n"
	msg += "-sg : Deals with a specific stone game game state\n"
	msg += "\t -sg -naive : Utilizes the naive recursive algorithm\n"
	msg += "\t \t -sg -naive -test : Runs test cases using the naive recursive algorithm\n"
	msg += "\t \t -sg -naive <int1> <int2> : Utilizes the naive recursive algorithm on inputs int1, int2\n"
	msg += "\t -sg -ropt : Utilizes the optimized recursive algorithm\n"
	msg += "\t \t -sg -ropt -test : Runs test cases using the optimized recursive algorithm\n"
	msg += "\t \t -sg -ropt <int1> <int2> : Utilizes the optimized algorithm on inputs int1, int2\n"

	print msg
	pass

def pe325_commandline_parse():
	if sys.argv[1] == "-h":
		print_help_message()
	elif sys.argv[1] == "-sg": # stone game
		if sys.argv[2] == "-naive": # 
			if sys.argv[3] == "-test":
				run_test_cases_sg(sg_naive_recursive)
			else:
				sg_naive_recursive((int(sys.argv[3]), int(sys.argv[4])))
		elif sys.argv[2] == "-ropt":
			if sys.argv[3] == "-test":
				run_test_cases_sg(sg_recursive_opt1)
			else:
				print sg_recursive_opt1((int(sys.argv[3]), int(sys.argv[4])))		

	pass

def run_test_cases_sg(algorithm):
	for test_case in TEST_CASES_SG:
		if not run_test_case_sg(test_case, algorithm):
			print "did not complete tests because this one failed"
			return False
	print "All " + str(len(TEST_CASES_SG)) + " tests pass!"
	return True




def run_test_case_sg(test_case, algorithm):
	inpt = test_case[0]
	print "TEST CASE: " + str(inpt)
	expected = test_case[1]
	print "EXPECTED:" + str(expected)
	actual = algorithm(inpt)
	print "ACTUAL:" + str(actual)
	if expected == actual: 
		print "PASSED"
	else:
		print "FAILED"
	print "\n"
	return expected == actual

def sg_naive_recursive(startState):
	x = min(startState)
	y = max(startState)
	if x == 0: return False
	for m in range(1, (y // x) + 1):
		if not sg_naive_recursive((x, y - (m * x))):
			return True
	return False

def sg_recursive_opt1(startState):
	x = min(startState)
	y = max(startState)
	if y >= 2 * x: return True
	return not sg_recursive_opt1((y - x, x))

### EXECUTION STARTS HERE
pe325_commandline_parse()