#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/11/19 0:22
@Author      : 兰兴宝 echolan@126.com
@File        : 29.DivideTwoIntegers.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution(object):
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.
    Example 1:
        Input: dividend = 10, divisor = 3
        Output: 3
    Example 2:
        Input: dividend = 7, divisor = -3
        Output: -2
    Note:
        · Both dividend and divisor will be 32-bit signed integers.
        · The divisor will never be 0.
        ·  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

        给出两个整数求相除的结果，不能使用乘、除、模操作
    """
    def symb(self, dividend, divisor):
        """
        参照答题者：@tusizi 所写答案
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend > 0) is (divisor > 0)      # 高！实在是高！
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            t, tmp = 1, divisor
            while dividend >= tmp:
                dividend -= tmp
                quotient += t
                tmp <<= 1
                t <<= 1
        if not flag:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)


    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """


if __name__ == '__main__':
    examples = [
        {'input':(7, -3), 'output': -2},
        {'input': (10, 3), 'output': 3},
        {'input': (7, -1), 'output': -7},
        {'input': (0, -3), 'output': 0},
        {'input': (10, 1), 'output': 10},
    ]
    solution = Solution()
    for example in examples:
        output = solution.symb(*example['input'])
        print(f'{output == example["output"]}, output: {output}, answer: {example["output"]}')
