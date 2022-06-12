# Write a function "canConstruct(target, wordBank)" that accepts a
# target string and an array of strings
#
# The function should return a boolean indicating whether or not the
# "target" can be constructed by contatenating elements of the
# "wordBank" array.
#
# You may reuse elements of "wordBank" as many times as needed.
#
# Example: canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) -> True

import unittest
import timeit


def canConstruct_recursive(target, wordBank):
    # Time: O(m*n^m)
    # Space: O(m^2)
    if target == '':
        return True
    for word in wordBank:
        if target.startswith(word):
            if canConstruct_recursive(target[len(word):], wordBank):
                return True
    return False


def canConstruct_memoize(target, wordBank, memo=None):
    # Time: O(m^2*n)
    # Space: O(m^2)
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordBank:
        if target.startswith(word):
            if canConstruct_memoize(target[len(word):], wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


def canConstruct_tabular(target, wordBank):
    # Time: O(m^2*n)
    # Space: O(m)
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if target[i:].startswith(word):
                    table[i + len(word)] = True
    return table[len(target)]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]
        self.expected_n = [
            True,
            False,
            True,
            False,
            False,
        ]
        self.extended_tuple = ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                               ("e", "ee", "eee", "eeee", "eeeee", "eeeeee"))
        self.expected_extended_tuple = False

    def test_canConstruct_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canConstruct_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_canConstruct_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canConstruct_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, canConstruct_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_canConstruct_tabular(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], canConstruct_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, canConstruct_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]:
            print(f'canConstruct_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'canConstruct_recursive("{tup[0]}", {tup[1]})', setup='from __main__ import canConstruct_recursive', number=1))
            print(f'canConstruct_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'canConstruct_memoize("{tup[0]}", {tup[1]})', setup='from __main__ import canConstruct_memoize', number=1))
            print(f'canConstruct_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'canConstruct_tabular("{tup[0]}", {tup[1]})', setup='from __main__ import canConstruct_tabular', number=1))
    print(' ')
    unittest.main()
