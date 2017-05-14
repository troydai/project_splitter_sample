"""Sample test"""

# pylint: disable=W1503
# this sample test is for purpose of testing and demostrating

import unittest


class TestClassB(unittest.TestCase):
    def test_third(self):
        self.assertTrue(True)

    def test_fourth(self):
        self.assertFalse(True)
