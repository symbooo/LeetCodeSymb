#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/9/16 0:31
@Author      : 兰兴宝 echolan@126.com
@File        : 28.Implement_strStr().py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    从字符串中找出目标子串，并返回其第一次出现的位置，如果找不到，则返回-1，如果目标子串是空，则返回0

    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
        Input: haystack = "hello", needle = "ll"
        Output: 2

    Example 2:
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1

    Clarification:
        What should we return when needle is an empty string? This is a great question to ask during an interview.
        For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
    """
    def symb(self, haystack, needle):
        """

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle:
            for index, value in enumerate(haystack):
                if value == needle[0]:
                    if haystack[index: index + len(needle)] == needle:
                        return index
        return -1 if needle else 0

    # 高赞回答
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    hay = 'hello'
    target = 'll'
    solution = Solution()
    print(solution.symb(hay, target))