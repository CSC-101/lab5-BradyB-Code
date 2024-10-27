from idlelib.pyshell import restart_line
from unittest import expectedFailure

import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    def test_Time_eq_1(self):
        input1 = data.Time(2, 15, 30)
        input2 = data.Time(2, 15, 30)
        result = (input1 == input2)
        expected = True
        self.assertEqual(expected, result)

    def test_Time_eq_2(self):
        input3 = data.Time(2, 25, 5)
        input4 = data.Time(1, 25, 5)
        result = (input3 == input4)
        expected = False
        self.assertEqual(expected, result)

    #### Add tests for Time.__repr__
    def test_Time_repr_1(self):
        input = data.Time(15, 10, 0)
        result = input.__repr__()
        expected = "Time(Hour: 15, Minute: 10, Second: 0)"
        self.assertEqual(expected, result)

    def test_Time_repr_2(self):
        input = data.Time(4, 23, 8)
        result = input.__repr__()
        expected = "Time(Hour: 4, Minute: 23, Second: 8)"
        self.assertEqual(expected, result)

    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
