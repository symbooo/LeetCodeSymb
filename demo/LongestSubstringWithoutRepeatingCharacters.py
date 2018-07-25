#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/25 10:44
@Author      : 兰兴宝 echolan@126.com
@File        : LongestSubstringWithoutRepeatingCharacters.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class LongestSubstringWithoutRepeatingCharacters:
    """
    给定一个字符串，找出最长的字母不重复的子串，返回子串长度
    Given a string, find the length of the longest substring without repeating characters.
    Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def symb(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_string_list = []
        length = 0
        longest_substring = ''
        for x in s:
            if x in sub_string_list:
                if len(sub_string_list) > length:
                    length = len(sub_string_list)
                    longest_substring = ''.join(sub_string_list)
                sub_string_list = sub_string_list[sub_string_list.index(x) + 1:]
            sub_string_list.append(x)
        else:
            if len(sub_string_list) > length:
                length = len(sub_string_list)
                longest_substring = ''.join(sub_string_list)
        print(longest_substring)
        return length

    # 高赞实现
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

