#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/9/10 23:05
@Author      : 兰兴宝 echolan@126.com
@File        : 29.DivideTwoIntegers.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    输入两个数，被除数（dividend），除数（divisor）, 不适用乘法、除法和模除， 返回商。

    Given two integers dividend and divisor, divide two integers without using multiplication,
      division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.

    Example 1:
        Input: dividend = 10, divisor = 3
        Output: 3
    Example 2:
        Input: dividend = 7, divisor = -3
        Output: -2
    Note:
        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers
         within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
         assume that your function returns 231 − 1 when the division result overflows.
    """
    def symb(self, dividend, divisor):
        """

        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pass

    # 高赞答案
    def divide(self, dividend, divisor):
        """

        :type dividend:  int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
