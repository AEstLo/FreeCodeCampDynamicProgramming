# Write a function "bestSum(targetSum, numbers)" that takes in a
# targetSum and an array of numers as arguments.
#
# The function should return an array containing the shortest
# combination of numbers that add up to exactly the targetSum.
#
# If there is a tie for the shortest combination, you may return any
# one of the shortest
#
# You may use an element of the array as many times as needed.
#
# You may assume that all input numbers are nonnegative.
#
# Example: bestSum(7, [5, 3, 4, 7]) -> [7]

import unittest
import timeit


def bestSum_recursive(targetSum, numbers):
    # Time: O(m * n^m)
    # Space: O(m^2)
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    result = None
    for num in numbers:
        combination = bestSum_recursive(targetSum - num, numbers)
        if combination is not None:
            combination.append(num)
            if result is None or len(result) > len(combination):
                result = combination
    return result


def bestSum_memoize(targetSum, numbers, memo=None):
    # Time: O(m^2 * n)
    # Space: O(m^2)
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    result = None
    for num in numbers:
        combination = bestSum_memoize(targetSum - num, numbers, memo)
        if combination is not None:
            combination.append(num)
            if result is None or len(result) > len(combination):
                result = combination
    memo[targetSum] = result
    return result


def bestSum_tabular(targetSum, numbers):
    # Time: O(m^2 * n)
    # Space: O(m^2)
    table = [None] * (targetSum + 1)
    table[0] = []
    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = list(table[i])
                    combination.append(num)
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination
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
            [7],
            None,
            [5, 3],
            None,
        ]
        self.extended_tuple = (300, (7, 14))
        self.expected_extended_tuple = None

    def test_bestSum_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], bestSum_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_bestSum_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], bestSum_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, bestSum_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_bestSum_tabular(self):
        new_expected_n = [  # We need this variable because the order of the elements differ
            [2, 2, 3],
            [7],
            None,
            [3, 5],
            None,
        ]
        for i in range(len(self.test_n)):
            self.assertEqual(
                new_expected_n[i], bestSum_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, bestSum_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            (7, (2, 3)),
            (7, (5, 3, 4, 7)),
            (7, (2, 4)),
            (8, (2, 3, 5)),
            (200, (14, 7)),
        ]:
            print(f'bestSum_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'bestSum_recursive({tup[0]}, {tup[1]})', setup='from __main__ import bestSum_recursive', number=1))
            print(f'bestSum_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'bestSum_memoize({tup[0]}, {tup[1]})', setup='from __main__ import bestSum_memoize', number=1))
            print(f'bestSum_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'bestSum_tabular({tup[0]}, {tup[1]})', setup='from __main__ import bestSum_tabular', number=1))
    print(' ')
    unittest.main()
