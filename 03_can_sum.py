# Write a function "canSum(targetSum, numbers)" that takes in a
# targetSum and an array of numers as arguments.
#
# The function should return a boolean indicating whether or not it
# is possible to generate the targetSum using numbers from the array.
#
# You may use an element of the array as many times as needed.
#
# You may assume that all input numbers are nonnegative.
#
# Example: canSum(7, [5, 3, 4, 7]) -> True

import unittest
import timeit


def canSum_recursive(targetSum, numbers):
    # Time: O(n^m)
    # Space: O(m)
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if canSum_recursive(targetSum - num, numbers):
            return True
    return False


def canSum_memoize(targetSum, numbers, memo=None):
    # Time: O(m*n)
    # Space: O(m)
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if canSum_memoize(targetSum - num, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


def canSum_tabular(targetSum, numbers):
    # Time: O(m * n)
    # Space: O(m)
    table = [False] * (targetSum + 1)
    table[0] = True
    for i in range(targetSum + 1):
        if table[i]:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True
    return table[targetSum]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [
            (7, (2, 3)),
            (7, (5, 3, 4, 7)),
            (7, (2, 4)),
            (8, (2, 3, 5)),
            (900, (2, 3, 5)),
        ]
        self.expected_n = [
            True, True, False, True, True,
        ]
        self.extended_tuple = (300, (7, 14))
        self.expected_extended_tuple = False

    def test_canSum_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canSum_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_canSum_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canSum_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, canSum_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_canSum_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canSum_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, canSum_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            (7, (2, 3)),
            (7, (5, 3, 4, 7)),
            (7, (2, 4)),
            (8, (2, 3, 5)),
            (900, (2, 3, 5)),
        ]:
            print(f'canSum_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'canSum_recursive({tup[0]}, {tup[1]})', setup='from __main__ import canSum_recursive', number=1))
            print(f'canSum_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'canSum_memoize({tup[0]}, {tup[1]})', setup='from __main__ import canSum_memoize', number=1))
            print(f'canSum_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'canSum_tabular({tup[0]}, {tup[1]})', setup='from __main__ import canSum_tabular', number=1))
    print(' ')
    unittest.main()
