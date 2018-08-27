#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/27 12:44
@Author      : 兰兴宝 echolan@126.com
@File        : 14.LongestCommonPrefix.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给定一个元素为字符串的列表，找出列表中字符串的最长公共前缀

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
        Input: ["flower","flow","flight"]
        Output: "fl"
    Example 2:
        Input: ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
    Note:
        All given inputs are in lowercase letters a-z.
    """
    def symb(self, strs):
        """
        20180827
        :type strs:  List[str]
        :rtype: str
        """
        result = ''
        if strs:
            for x in range(len(strs[0])):
                s = strs[0][x]
                for i in strs:
                    if not i[x:] or i[x] != s:
                        return result
                result += s
        return result

    # 最高赞
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


    # 代码最少
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret


if __name__ == '__main__':
    examples = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        [''],
        ['a'],
    ]
    solution = Solution()
    for example in examples:
        print(example, solution.longestCommonPrefix(example))