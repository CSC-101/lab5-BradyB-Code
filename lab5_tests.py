import data
import lab5
import unittest

from lab5 import time_add, is_descending, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_Time_add_1(self):
        input1 = data.Time(2, 40, 15)
        input2 = data.Time(0, 16, 50)
        result = time_add(input1, input2)
        expected = data.Time(2, 57, 5)
        self.assertEqual(expected, result)

    def test_Time_add_2(self):
        input3 = data.Time(3, 59, 20)
        input4 = data.Time(1, 33, 54)
        result = time_add(input3, input4)
        expected = data.Time(5, 33, 14)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending_1(self):
        input = [2.0 ,3.3 ,54.3 ,6.8 ,1.1]
        result = is_descending(input)
        expected = False
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        input = [1.0 ,1.3 ,4.3 ,6.8 ,86.1]
        result = is_descending(input)
        expected = True
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between_1(self):
        input = [4,76 ,71 ,3 ,5]
        result = largest_between(input, 2, 4)
        expected = 71
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        input = [4, 76,71 ,3 ,5]
        result = largest_between(input, 0, 1)
        expected = 76
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin_1(self):
        input = [data.Point(3, 6), data.Point(-7, 9)]
        result = furthest_from_origin(input)
        expected = 1
        self.assertEqual(expected, result)

    def test_furthest_from_origin_2(self):
        input = [data.Point(10, 6), data.Point(-7, 4), data.Point(-20, -8)]
        result = furthest_from_origin(input)
        expected = 2
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
