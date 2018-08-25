#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/23 22:16
@Author      : 兰兴宝 echolan@126.com
@File        : 8.StringToInteger.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code
import re


class StringToInteger:
    """
    将给定一个字符串，以+或者-号开始的尽可能多的连续的数字，转换成32比特的有符号数值类型，如果超过取值范围，则返回（2*32 - 1）或者 -2*32
    如果找不到这个数字，则返回0

    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
    Example 1:
        Input: "42"
        Output: 42

    Example 2:
        Input: "   -42"
        Output: -42
        Explanation: The first non-whitespace character is '-', which is the minus sign.
                     Then take as many numerical digits as possible, which gets 42.

    Example 3:
        Input: "4193 with words"
        Output: 4193
        Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

    Example 4:
        Input: "words and 987"
        Output: 0
        Explanation: The first non-whitespace character is 'w', which is not a numerical
                     digit or a +/- sign. Therefore no valid conversion could be performed.

    Example 5:
        Input: "-91283472332"
        Output: -2147483648
        Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                     Thefore INT_MIN (−231) is returned.
    """

    def symb(self, s):
        """
        :param s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        first = s[0] if s[0] in '+-' else ''
        if first:
            s = s[1:]
        for c in s:
            if c in '1234567890':
                first += c
            else:
                break
        if first in ('-', '+', ''):
            return 0
        first = int(first)
        return min(first, 2**31 - 1) if first > 0 else max(first, -2**31)

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ret = re.match(' *([-+]?\d+)', str)
        if ret:
            ret = int(ret.group(1))
            if ret > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if ret < -2 ** 31:
                return -2 ** 31
            return ret
        else:
            return 0

    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0
