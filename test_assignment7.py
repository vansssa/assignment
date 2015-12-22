import unittest
from assignmnet7 import sum_func

class TestAssignment7(unittest.TestCase):
	def test_sum_func(self) :
		self.assertEqual(sum_func() , -55)


if __name__ == '__main__':
    unittest.main()

