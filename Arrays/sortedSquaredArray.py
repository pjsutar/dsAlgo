"""
Return array that holds squared values of all elements in a sorted list in sorted manner
Consider negative values
"""

# O(n) --Time | O(n) --Space
# Straightforward

import unittest


def sortedSquaredArray(array):
    squaredArray = [1 for _ in array]
    for i in range(len(array)):
        squaredArray[i] = array[i]**2
    return sorted(squaredArray)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)
