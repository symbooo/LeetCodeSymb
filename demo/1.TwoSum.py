#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/19 15:39
@Author      : 兰兴宝 echolan@126.com
@File        : 1.TwoSum.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : 两数之和
"""
# Enjoy Your Code


class TwoSum:
    """
    给定一个整数列表，找出两个数的和为目标值，返回两个数的索引，每个数最多用一次
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """
    def symb(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        return False

    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
