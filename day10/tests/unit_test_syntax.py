import unittest
from day10.syntax import *


class TestPart1(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(26397, syntax("data/test_data")[0])

    def test_real_data(self):
        self.assertEqual(411471, syntax("data/real_data")[0])


class TestPart2(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(288957, syntax("data/test_data")[1])

    def test_real_data(self):
        self.assertEqual(3122628974, syntax("data/real_data")[1])


if __name__ == '__main__':
    unittest.main()
