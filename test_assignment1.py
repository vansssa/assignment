import unittest
from assignment1 import is_perfect

class TestAssignment1(unittest.TestCase):
	def test_isperfect_true(self) :
		self.assertEqual(is_perfect(6),True)
	def test_isperfect_false(self) :
		self.assertEqual(is_perfect(8),False)


if __name__ == '__main__':
    unittest.main()

