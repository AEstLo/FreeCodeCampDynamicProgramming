# Write a function "allConstruct(target, wordBank)" that accepts a
# target string and an array of strings
#
# The function should return a 2D array containing all of the ways
# that the "target" can be constructed by contatenating elements of
# the "wordBank" array. Each element of the 2D array should represent
# one combination that constructs the "target".
#
# You may reuse elements of "wordBank" as many times as needed.
#
# Example: allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) -> [ ["abc", "def"] ]
#          allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]) -> [ ["purp", "le"], ["p", "ur", "p", "le"] ]

import unittest
import timeit


def allConstruct_recursive(target, wordBank):
    # Time: O(n^m)
    # Space: O(m)
    if target == '':
        return [[]]
    all_construct = []
    for word in wordBank:
        if target.startswith(word):
            partial_sol = allConstruct_recursive(target[len(word):], wordBank)
            for sol in partial_sol:
                all_construct.append([word] + sol)
    return all_construct


def allConstruct_memoize(target, wordBank, memo=None):
    # Time: O(n^m)
    # Space: O(m)
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    all_construct = []
    for word in wordBank:
        if target.startswith(word):
            partial_sol = allConstruct_memoize(
                target[len(word):], wordBank, memo)
            for sol in partial_sol:
                all_construct.append([word] + sol)
    memo[target] = all_construct
    return all_construct


def allConstruct_tabular(target, wordBank):
    # Time: O(n^m)
    # Space: O(n^m)
    table = [[] for __ in range(len(target) + 1)]
    table[0].append([])
    for i in range(len(target) + 1):
        for word in wordBank:
            if target[i:].startswith(word):
                for combination in table[i]:
                    table[i + len(word)].append(combination + [word])
    return table[len(target)]


class Testing(unittest.TestCase):
    def setUp(self):
        self.test_n = [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef", "c")),
            ("purple", ("purp", "p", "ur", "le", "purpl")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]
        self.expected_n = [
            [["ab", "cd", "ef"], ["ab", "c", "def"],
                ["abc", "def"], ["abcd", "ef"]],
            [["purp", "le"], ["p", "ur", "p", "le"]],
            [],
            [],
        ]
        self.extended_tuple = ("eeeeeeeeeeeeeeeeeeef",
                               ("e", "ee", "eee", "eeee", "eeeee", "eeeeee"))
        self.expected_extended_tuple = []

    def test_allConstruct_recursive(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], allConstruct_recursive(self.test_n[i][0], self.test_n[i][1]))

    def test_allConstruct_memoize(self):
        for i in range(len(self.test_n)):
            self.assertEqual(
                self.expected_n[i], allConstruct_memoize(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, allConstruct_memoize(self.extended_tuple[0], self.extended_tuple[1]))

    def test_allConstruct_tabular(self):
        new_expected_n = [
            [['abc', 'def'], ['ab', 'c', 'def'], [
                'abcd', 'ef'], ['ab', 'cd', 'ef']],
            [["purp", "le"], ["p", "ur", "p", "le"]],
            [],
            [],
        ]
        for i in range(len(self.test_n)):
            self.assertEqual(
                new_expected_n[i], allConstruct_tabular(self.test_n[i][0], self.test_n[i][1]))
        self.assertEqual(
            self.expected_extended_tuple, allConstruct_tabular(self.extended_tuple[0], self.extended_tuple[1]))


if __name__ == '__main__':
    if True:
        for tup in [
            ("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef", "c")),
            ("purple", ("purp", "p", "ur", "le", "purpl")),
            ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
            ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee")),
        ]:
            print(f'allConstruct_recu({tup[0]}, {tup[1]})', timeit.timeit(
                f'allConstruct_recursive("{tup[0]}", {tup[1]})', setup='from __main__ import allConstruct_recursive', number=1))
            print(f'allConstruct_memo({tup[0]}, {tup[1]})', timeit.timeit(
                f'allConstruct_memoize("{tup[0]}", {tup[1]})', setup='from __main__ import allConstruct_memoize', number=1))
            print(f'allConstruct_tabu({tup[0]}, {tup[1]})', timeit.timeit(
                f'allConstruct_tabular("{tup[0]}", {tup[1]})', setup='from __main__ import allConstruct_tabular', number=1))
    print(' ')
    unittest.main()
