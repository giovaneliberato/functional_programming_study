import unittest
from average import *

class AverageTests(unittest.TestCase):
    def test_get_sum_of_list(self):
        array = [1]
        self.assertEquals(total_for_array(array), 1)
        array = [1, 2, 3]
        self.assertEquals(total_for_array(array), 6)
        array = []
        self.assertEquals(total_for_array(array), 0)


if __name__ == "__main__":
    unittest.main()
