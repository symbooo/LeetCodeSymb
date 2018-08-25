#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/24 0:09
@Author      : 兰兴宝 echolan@126.com
@File        : 9.PalindromeNumber.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class PalindromeNumber:
    """
    给定一个数字，判断是否是回文数。（不能装换成字符串）
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:
        Input: 121
        Output: true

    Example 2:
        Input: -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
        Input: 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Follow up:
        Could you solve it without converting the integer to a string?
    """
    def symb(self, x):
        """
        装换成字符串方式
        :param x: int
        :rtype: bool
        """
        x = str(x)
        length = len(x) // 2
        for i in range(length):
            if x[i] != x[-(i + 1)]:
                return False
            i += 1
        return True

    def noConvertToStr(self, x):
        """
        不转换成字符串
        :param x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y, z = x, 0
        while y:
            z = z * 10 + y % 10
            y //= 10
        return y == x

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True
