import unittest
from day10.syntax import *


class TestPart1(unittest.TestCase):
    def test_test_data(self):
        self.assertEqual(syntax("data/test_data"), 26397)

    def test_real_data(self):
        self.assertEqual(syntax("data/real_data"), 411471)

if __name__ == '__main__':
    unittest.main()
