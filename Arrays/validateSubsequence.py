"""
Write a function that validates whether sequence is a subsequence of array
A subsequence is a set of numbers that are not necessarily adjucent in the 
array but they are in the same order as they appear in the array
Order matters!
"""

# O(n) --Time | O(1) --Space

# Hold sequence[seqIdx] and compare against array[arrayIdx]
# Increase arrayIdx to find sequence[seqIdx]
# Increase seqIdx if element is found in array


import unittest


def isValidSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1
    return seqIdx == len(sequence)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))
