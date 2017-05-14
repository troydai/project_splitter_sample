"""Sample test"""

# pylint: disable=W1503
# this sample test is for purpose of testing and demostrating

import unittest


class TestClassA(unittest.TestCase):
    def test_first(self):
        self.assertTrue(True)

    def test_second(self):
        self.assertFalse(False)
