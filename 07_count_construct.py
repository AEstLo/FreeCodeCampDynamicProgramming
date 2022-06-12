# Write a function "countConstruct(target, wordBank)" that accepts a
# target string and an array of strings
#
# The function should return the number of ways that the "target" can
# be constructed by contatenating elements of the "wordBank" array.
#
# You may reuse elements of "wordBank" as many times as needed.
#
# Example: countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) -> 1
#          countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]) -> 2

import unittest
import timeit


def countConstruct_recursive(target, wordBank):
    # Time: O(m*n^m)
    # Space: O(m^2)
    if target == '':
        return 1
    count = 0
    for word in wordBank:
        if target.startswith(word):
            count += countConstruct_recursive(target[len(word):], wordBank)
    return count


def countConstruct_memoize(target, wordBank, memo=None):
    # Time: O(m^2*n)
    # Space: O(m^2)
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    count = 0
    for word in wordBank:
        if target.startswith(word):
            count += countConstruct_memoize(target[len(word):], wordBank, memo)
    memo[target] = count
    return count


def countConstruct_tabular(target, wordBank):
    # Time: O(m^2*n)
    # Space: O(m)
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target)):
        for word in wordBank:
            if target[i:].startswith(word):
                table[i + len(word)] += table[i]
    return table[len(target)]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd")),
            ("purple", ("purp", "p", "ur", "le", "purpl")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]
        self.expected_n = [
            1,
            2,
            0,
            4,
            0,
        ]
        self.extended_tuple = ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                               ("e", "ee", "eee", "eeee", "eeeee", "eeeeee"))
        self.expected_extended_tuple = False

    def test_countConstruct_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], countConstruct_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_countConstruct_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], countConstruct_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, countConstruct_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_countConstruct_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], countConstruct_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, countConstruct_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd")),
            ("purple", ("purp", "p", "ur", "le", "purpl")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]:
            print(f'countConstruct_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'countConstruct_recursive("{tup[0]}", {tup[1]})', setup='from __main__ import countConstruct_recursive', number=1))
            print(f'countConstruct_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'countConstruct_memoize("{tup[0]}", {tup[1]})', setup='from __main__ import countConstruct_memoize', number=1))
            print(f'countConstruct_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'countConstruct_tabular("{tup[0]}", {tup[1]})', setup='from __main__ import countConstruct_tabular', number=1))
    print(' ')
    unittest.main()
