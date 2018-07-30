#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/26 21:35
@Author      : 兰兴宝 echolan@126.com
@File        : ZigZagConversion.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class ZigZagConversion:
    """
    将字符串"PAYPALISHIRING"按Z字形排列成指定行数，
    P   A   H   N
    A P L S I I G
    Y   I   R
    然后按行读出： PAHNAPLSIIGYIR
    实现一个将字符串进行指定行数变换的函数：
    string convert(string s, int numRows);

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);
    Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
    Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:

        P     I    N
        A   L S  I G
        Y A   H R
        P     I
    """
    # 初次实现
    def symb(self, s, numRows):
        """
        :type s:  str
        :type numRows:  int
        :rtype:  str
        """
        group_num, length = numRows * 2 - 2, len(s)
        if length <= numRows or numRows == 1:
            return s
        result = []
        step = (length // group_num) + 1 if length % group_num else (length // group_num)
        for i in range(numRows):
            nums = [i,]
            if i not in (0, numRows - 1):
                nums.append(group_num - i)
            result += [s[x * group_num + y] for x in range(step) for y in nums if (x * group_num + y) < length]
        return ''.join(result)

    # 高赞实现
    def convert(self, s, numRows):
        """
        :type s:  str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)


if __name__ == '__main__':
    zzc = ZigZagConversion()
    a = zzc.symb('PAYPALISHIRING', 3)
    print(a)
