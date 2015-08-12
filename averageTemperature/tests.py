import unittest
from average import *


class AverageTests(unittest.TestCase):
    def test_get_sum_of_array(self):
        array = [1]
        self.assertEquals(total_for_array(array), 1)
        array = [1, 2, 3]
        self.assertEquals(total_for_array(array), 6)
        array = []
        self.assertEquals(total_for_array(array), 0)

    def test_get_average_of_array(self):
        array = [1, 2, 3]
        self.assertEquals(average_for_array(array), 2)


class DataStructureParsingTests(unittest.TestCase):
    def setUp(self):
        super(unittest.TestCase, self)
        self.data = [
          {
            "name": "Jamestown",
            "population": 2047,
            "temperatures": [-34, 67, 101, 87]
          },
          {
            "name": "Awesome Town",
            "population": 3568,
            "temperatures": [-3, 4, 9, 12]
          }
        ]

    def test_get_temperatures(self):
        expected = [[-34, 67, 101, 87], [-3, 4, 9, 12]]
        self.assertListEqual(all_temperatures(self.data), expected)

    def test_get_population(self):
        expected = [2047, 3568]
        self.assertListEqual(all_population(self.data), expected)


class CombineArraysTests(unittest.TestCase):
    def test_combine_two_arrays(self):
        array1 = [2047, 3568]
        array2 = [55, 5]
        expected = [[2047, 55], [3568, 5]]
        self.assertListEqual(combine_arrays(array1, array2), expected)


class TestEverythingTogheter(unittest.TestCase):
    def setUp(self):
        super(unittest.TestCase, self)
        self.data = [
          {
            "name": "Jamestown",
            "population": 2047,
            "temperatures": [-34, 67, 101, 87]
          },
          {
            "name": "Awesome Town",
            "population": 3568,
            "temperatures": [-3, 4, 9, 12]
          }
        ]

    def test_do_it(self):
        expected = [[55, 2047], [5, 3568]]
        processed = combine_arrays(map(average_for_array, all_temperatures(self.data)), all_population(self.data))
        self.assertListEqual(processed, expected)


if __name__ == "__main__":
    unittest.main()
