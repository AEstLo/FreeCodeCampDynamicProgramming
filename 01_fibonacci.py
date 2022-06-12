# Write a function "fib(n)" that takes in a number as an argument
# The function should return the n-th number of the Fibonacci sequence
#
# The 1st and 2nd number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two.
#
#      n: 1, 2, 3, 4, 5, 6,  7,  8,  9, ...
# fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
import unittest
import timeit


def fib_recursive(n):
    # Time: O(2^n)
    # Space: O(n)
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoize(n, memo={}):
    # Time: O(n)
    # Space: O(n)
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memoize(n - 1) + fib_memoize(n - 2)
    return memo[n]


def fib_tabular(n):
    # Time: O(n)
    # Space: O(n)
    if n <= 2:
        return 1
    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1
    table[2] = 1
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_tabular_given_in_youtube(n):
    # Time: O(n)
    # Space: O(n)
    table = [0] * (n + 3)
    table[1] = 1
    for i in range(n + 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    return table[n]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [6, 7, 8, 50]
        self.expected_n = [8, 13, 21, 12586269025]

    def test_fib_recursive(self):
        for i in range(len(self.test_n)):
            if self.test_n[i] < 10:
                self.assertEqual(
                    self.expected_n[i], fib_recursive(self.test_n[i]))
            else:
                print(
                    f'fib_recursive({self.test_n[i]}) omitted: too many time')

    def test_fib_memo(self):
        for i in range(len(self.test_n)):
            self.assertEqual(self.expected_n[i], fib_memoize(self.test_n[i]))

    def test_fib_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(self.expected_n[i], fib_tabular(self.test_n[i]))

    def test_fib_tabular_given_in_youtube(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], fib_tabular_given_in_youtube(self.test_n[i]))


if __name__ == '__main__':
    if True:
        for i in range(15, 36):
            print(f'fib_recursi({i})', timeit.timeit(
                f'fib_recursive({i})', setup='from __main__ import fib_recursive', number=1))
            print(f'fib_memoize({i})', timeit.timeit(
                f'fib_memoize({i})', setup='from __main__ import fib_memoize', number=1))
            print(f'fib_tabular({i})', timeit.timeit(
                f'fib_tabular({i})', setup='from __main__ import fib_tabular', number=1))
            print(f'fib_tab_ytb({i})', timeit.timeit(
                f'fib_tabular_given_in_youtube({i})', setup='from __main__ import fib_tabular_given_in_youtube', number=1))
    print(' ')
    unittest.main()
