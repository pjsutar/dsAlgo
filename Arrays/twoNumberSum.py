"""
Return two numbers in input array that sum uo to targetSum
"""

# O(nlog(n)) --Time | O(1) --Space

"""
Increase left pointer or decrease right pointer
based on the running sum and target sum
"""


def twoNumberSum(array, targetSum):
    array.sort()
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        runningSum = array[leftIdx] + array[rightIdx]
        if runningSum == targetSum:
            return [array[leftIdx], array[rightIdx]]
            break
        elif runningSum > targetSum:
            rightIdx -= 1
        else:
            leftIdx += 1
    return []
