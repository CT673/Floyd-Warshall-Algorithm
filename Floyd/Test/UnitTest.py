import unittest
from Floyd import paths
from TestCase import (T1, P1, T2, P2)


class TestFloyd(unittest.TestCase):
    def test_1(self):
        self.assertLessEqual(P1, T1)

    def test_2(self):
        self.assertLessEqual(P2, T2)


if __name__ == '__main__':
    unittest.main()


