#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/26 20:18
@Author      : 兰兴宝 echolan@126.com
@File        : 5.LongestPalindromicSubstring.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class LongestPalindromicSubstring:
    """
    给定要给字符串s，找出最长的回文子串。假定s最长为1000
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    Example 1:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
    Example 2:
        Input: "cbbd"
        Output: "bb"
    """

    def symb(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 失败案例
        # max_index = len(s) - 1
        # if max_index <= 1:
        #     return s if max_index < 1 or s[0] == s[1] else s[0]
        # start = end = 0
        #
        # for x in range(1, max_index):
        #     i = j = x
        #     # if max_index - x < (end - start) / 2:
        #     #     break
        #     if s[x - 1] == s[x + 1]:
        #         i, j = x - 1, x + 1
        #     elif s[x] == s[x + 1]:
        #         i, j = x, x + 1
        #     if i != j:
        #         while i > 0 and j < max_index:
        #             if s[i - 1] == s[j + 1]:
        #                 i += 1
        #                 j += 1
        #             else:
        #                 break
        #         if j - i > start - end:
        #             start, end = i, j
        #     if j == max_index:
        #         break
        # return s[start:end + 1]

        length = len(s)
        if length <= 2:
            return s[0] if length == 2 and s[0] != s[1] else s
        start = end = 0
        for x in range(length):
            # abba 这种格式
            i, j = x, x + 1
            while i >= 0 and j < length:
                if s[i] == s[j]:
                    i, j = i - 1, j + 1
                else: break
            if j - i - 1 > end - start:
                start, end = i + 1, j

            # aba 这种格式
            i, j = x - 1, x + 1
            while i >= 0 and j < length:
                if s[i] == s[j]:
                    i, j = i - 1, j + 1
                else: break
            if j - i - 1 > end - start:
                start, end = i + 1, j
        return s[start:end]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]

if __name__ == '__main__':
    LPS = LongestPalindromicSubstring()
    s_list = ['babad', 'cbbd']
    for s in s_list:
        print(s, ' --  ', LPS.longestPalindrome(s))
