# Say that you are a traveler on a 2D grid. You begin in the
# to-left corner and your goal is to travel to the bottom-right
# corner. You may only move down and right.
#
# In how many ways can you travel to the goal on a grid with
# dimenstions m * n?
#
# Write a function "gridTraveler(m, n)" that calculates this.

import unittest
import timeit


def gridTraveler_recursive(m, n):
    # Time: O(2^(n+m))
    # Space: O(n+m)
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return gridTraveler_recursive(m - 1, n) + gridTraveler_recursive(m, n - 1)


def gridTraveler_memo(m, n, memo={}):
    # Time: O(n*m)
    # Space: O(n+m)
    k = f'{m}-{n}'
    if k in memo:
        return memo[k]
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[k] = gridTraveler_memo(m - 1, n, memo) + \
        gridTraveler_memo(m, n - 1, memo)
    return memo[k]


def gridTraveler_tabular(m, n):
    # Time: O(n*m)
    # Space: O(n*m)
    if m <= 0 or n <= 0:
        return 0
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    matrix[1][1] = 1
    for row in range(m + 1):
        for col in range(n + 1):
            if row + 1 <= m:
                matrix[row + 1][col] += matrix[row][col]
            if col + 1 <= n:
                matrix[row][col + 1] += matrix[row][col]

    return matrix[m][n]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [(0, 0), (1, 1), (2, 3), (3, 2), (3, 3)]
        self.expected_n = [0, 1, 3, 3, 6]
        self.extended_tuple = (18, 18)
        self.expected_extended_tuple = 2333606220

    def test_gridTraveler_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], gridTraveler_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_gridTraveler_memo(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], gridTraveler_memo(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, gridTraveler_memo(self.extended_tuple[0], self.extended_tuple[1]))

    def test_gridTraveler_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], gridTraveler_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, gridTraveler_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [(0, 0), (1, 1), (2, 3), (3, 2), (3, 3), (15, 12)]:
            print(f'gridTraveler_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'gridTraveler_recursive({tup[0]}, {tup[1]})', setup='from __main__ import gridTraveler_recursive', number=1))
            print(f'gridTraveler_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'gridTraveler_memo({tup[0]}, {tup[1]})', setup='from __main__ import gridTraveler_memo', number=1))
            print(f'gridTraveler_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'gridTraveler_tabular({tup[0]}, {tup[1]})', setup='from __main__ import gridTraveler_tabular', number=1))
    print(' ')
    unittest.main()
