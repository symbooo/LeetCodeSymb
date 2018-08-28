#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/28 15:56
@Author      : 兰兴宝 echolan@126.com
@File        : 17.LetterCombinationsOfAPhoneNumber.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code
from functools import reduce


class Solution:
    """
    给出一个由2-9组成的字符串，根据电话键盘返回所有可能的字母组合。

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
             1       2       3
                    abc     def
             4       5       6
            ghi     jkl     mno
             7       8       9
            pqrs    tuv     wxyz

    Example:
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    Note:
        Although the above answer is in lexicographical order, your answer could be in any order you want.
    """
    def symb(self, digits):
        """
        :type digits:  str
        :rtype:  List[str]
        """
        if not digits:
            return []
        dw_map = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz',
                  }
        result = ['', ]
        for d in digits:
            result = [r + s for s in dw_map.get(d) for r in result]
        return list(result)



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


if __name__ == '__main__':
    solution = Solution()
    examples = [
        '692346',
        '7958',
        '7',
    ]
    for example in examples:
        print(example, solution.letterCombinations(example))
