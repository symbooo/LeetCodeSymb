#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/29 0:35
@Author      : 兰兴宝 echolan@126.com
@File        : 20.ValidParentheses.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    判断一串由 '(', ')', '{', '}', '[' 和 ']' 组成的字符串是否有效。

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        1、Open brackets must be closed by the same type of brackets.
        2、Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:
        Input: "()"
        Output: true
    Example 2:
        Input: "()[]{}"
        Output: true
    Example 3:
        Input: "(]"
        Output: false
    Example 4:
        Input: "([)]"
        Output: false
    Example 5:
        Input: "{[]}"
        Output: true
    """
    def symb(self, s):
        """
        :type s:  str
        :rtype: bool
        """
        right = ''
        d = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for x in s:
            if x in d:
                right = d[x] + right
            else:
                if x == right[:1]:
                    right = right[1:]
                else:
                    return False
        return False if right else True

    # 高赞实现
    def isValid(self, s):
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
