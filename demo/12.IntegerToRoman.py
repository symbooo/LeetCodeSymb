#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/27 9:29
@Author      : 兰兴宝 echolan@126.com
@File        : 12.IntegerToRoman.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    把数字转换成罗马数字表示法

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

    Example 1:
        Input: 3
        Output: "III"
    Example 2:
        Input: 4
        Output: "IV"
    Example 3:
        Input: 9
        Output: "IX"
    Example 4:
        Input: 58
        Output: "LVIII"
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: 1994
        Output: "MCMXCIV"
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    def symb(self, num):
        """
        20180827
        :type num: int
        :rtype: str
        """
        nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M', ]
        result = ''
        index = 0
        while num:
            n = num % 10
            num //= 10
            s = nums[index] * n if n < 4 \
                else nums[index] + nums[index + 1] if n < 5 \
                else nums[index + 1] + nums[index] * (n - 5) if n < 9 \
                else nums[index] * (10 - n) + nums[index + 2]
            result = s + result
            index += 2
        return result

    # 高赞实现
    def intToRoman(self, num):
        """
        该方法算是作弊吧？面试应该不会过吧？！ 啊哈哈哈
        :type num:  int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
