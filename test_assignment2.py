import unittest
from assignment2 import get_max_of_n

class TestAssignment1(unittest.TestCase):
	def test_sort_file(self) :
		self.assertEqual(get_max_of_n('sample.txt',3) , [6421,8723,9239])



if __name__ == '__main__':
    unittest.main()

