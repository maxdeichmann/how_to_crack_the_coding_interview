# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

import unittest

def is_unique(strn):

    evaluation = ""
    for element in strn:
        if element in evaluation:
            return False
        else:
            evaluation = evaluation + element
    return True


class TestSum(unittest.TestCase):

    def test_is_unique_Hello(self):
        self.assertEqual(is_unique("Hello"), False, "Should be False")

    def test_sum_tuple(self):
        self.assertEqual(is_unique("warum"), True, "Should be True")

if __name__ == '__main__':
    unittest.main()