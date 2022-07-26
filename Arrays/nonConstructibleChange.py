"""
Calculate the smallest number of change that you can not create
using given coin values in 'coins' array
"""

# O(nlog(n)) --Time | O(1) --Space
# Traverse the array and check sum at each index
# Minimum change = sum at an index + 1,
# where array[index+1] > running sum + 1


import unittest


def nonConstructibleChange(coins):
    coins = sorted(coins)
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)
