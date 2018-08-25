#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/24 10:19
@Author      : 兰兴宝 echolan@126.com
@File        : 10.RegularExpressionMatching.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code
import unittest


class RegularExpressionMatching:
    """
    输入一个字符串（s）和需要匹配的模式（p），执行支持 . 和 * 的正则匹配，其中，s只包含小写a-z，p只包含a-z以及 '.'和 '*'
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    Note:
        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
    Example 1:
        Input:
            s = "aa"
            p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
    Example 2:
        Input:
            s = "aa"
            p = "a*"
        Output: true
        Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:
        Input:
            s = "ab"
            p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
    Example 4:
        Input:
            s = "aab"
            p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
    Example 5:
        Input:
            s = "mississippi"
            p = "mis*is*p*."
        Output: false
    """
    def symb(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        elif not s or not p:
            return False
        char = ''
        start_index = 0
        p_index = 0
        for c in s:
            char = p[p_index] if p[p_index] not in '.*' else 'abcdefghijklmnopqrstuvwxyz' if p[p_index] == '.' else char
            if c in char:
                p_index += 1
                if p[p_index] == '*':
                    start_index = p_index + 1
                if p_index >= len(p):
                    pass
            elif start_index:
                p_index = start_index
            else:
                return False
        return True

    """
    高赞实现
    """
    def isMatch1(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]

    def isMatch2(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # referring to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


# ########################################################################################
class Solution(RegularExpressionMatching):
    def isMatch(self, s, p):
        return self.isMatch2(s, p)


# ########################################################################################
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()