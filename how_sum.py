# Write a function "howSum(targetSum, numbers)" that takes in a
# targetSum and an array of numers as arguments.
#
# The function should return an array containing any combination of
# elemenents that add up to exactly the targetSum. If there is no
# combination that adds up to the targetSum, then return null.
#
# If there are multiple combinations possible, you may return any
# single one
#
# You may use an element of the array as many times as needed.
#
# You may assume that all input numbers are nonnegative.
#
# Example: howSum(7, [5, 3, 4, 7]) -> [7] or [3, 4] or [4, 3]

import unittest
import timeit


def howSum_recursive(targetSum, numbers):
    # Time: O(m * n^m)
    # Space: O(m)
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        combination = howSum_recursive(targetSum - num, numbers)
        if combination is not None:
            combination.append(num)
            return combination
    return None


def howSum_memoize(targetSum, numbers, memo=None):
    # Time: O(m^2*n)
    # Space: O(m^2)
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        combination = howSum_memoize(targetSum - num, numbers, memo)
        if combination is not None:
            combination.append(num)
            memo[targetSum] = list(combination)
            return combination
    memo[targetSum] = None
    return None


def howSum_tabular(targetSum, numbers):
    # Time: O(m^2 * n)
    # Space: O(m^2)
    table = [None] * (targetSum + 1)
    table[0] = []
    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = list(table[i])
                    table[i + num].append(num)
    return table[targetSum]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [
            (7, (2, 3)),
            (7, (5, 3, 4, 7)),
            (7, (2, 4)),
            (8, (2, 3, 5)),
            (200, (14, 7)),
        ]
        self.expected_n = [
            [3, 2, 2],
            [4, 3],
            None,
            [2, 2, 2, 2],
            None,
        ]
        self.extended_tuple = (300, (7, 14))
        self.expected_extended_tuple = None

    def test_howSum_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], howSum_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_howSum_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], howSum_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, howSum_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_howSum_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], howSum_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, howSum_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            (7, (2, 3)),
            (7, (5, 3, 4, 7)),
            (7, (2, 4)),
            (8, (2, 3, 5)),
            (900, (2, 3, 5)),
            (200, (14, 7)),
        ]:
            print(f'howSum_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'howSum_recursive({tup[0]}, {tup[1]})', setup='from __main__ import howSum_recursive', number=1))
            print(f'howSum_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'howSum_memoize({tup[0]}, {tup[1]})', setup='from __main__ import howSum_memoize', number=1))
            print(f'howSum_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'howSum_tabular({tup[0]}, {tup[1]})', setup='from __main__ import howSum_tabular', number=1))
    print(' ')
    unittest.main()
