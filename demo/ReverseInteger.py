#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/31 22:34
@Author      : 兰兴宝 echolan@126.com
@File        : ReverseInteger.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code

class ReverseInteger:
    """
    翻转32位整数的数字部分
    Given a 32-bit signed integer, reverse digits of an integer.
    Example 1:
        Input: 123
        Output: 321
    Example 2:
        Input: -123
        Output: -321
    Example 3:
        Input: 120
        Output: 21
    Note:
        Assume we are dealing with an environment which could only store integers within the 32-bit
      signed integer range:
            [−231,  231 − 1].
        For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    """

    def symb(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        if str_x[0] == '-':
            result = '-' + str_x[::-1][:-1]
        else:
            result = str_x[::-1]
        result = int(result)
        return result if -2147483648 <= result <= 2147483647 else 0


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # solution 1
        # # in python3.6 cmp() function is removed
        # s = cmp(x, 0)
        # r = int(`s * x`[::-1])
        # return s * r * (r < 2 ** 31)

        s = str(x)
        res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
        return res if -2147483648 <= res <= 2147483647 else 0


if __name__ == '__main__':
    test_list = [0, -283461, -190, 3400, 12345136567876]
    RI = ReverseInteger()
    for x in test_list:
        print(x, '  --  ', RI.symb(x))
