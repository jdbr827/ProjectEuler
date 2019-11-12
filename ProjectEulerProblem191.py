"""
Project Euler Problem 191 (Prize Strings)
"""
import unittest

def T(n_days):
	"""
	Assumes n_days >= 3
	"""
	B = [1, 2, 4]
	for i in range(3, n_days+1):
		B.append(B[-1] + B[-2] + B[-3])
	return B[n_days] + sum(B[i] * B[n_days-i-1] for i in range(n_days))



class PE191Test(unittest.TestCase):

	def test_4(self):
		self.assertEqual(T(4), 43)


suite = unittest.TestLoader().loadTestsFromTestCase(PE191Test)
unittest.TextTestRunner(verbosity=2).run(suite)

print(T(30))