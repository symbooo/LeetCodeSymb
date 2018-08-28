#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/28 14:58
@Author      : 兰兴宝 echolan@126.com
@File        : 16.3SumClosest.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给定一个n个元素的数组 nums 和 一个目标值， 从数组中找出3个数，使得他们之和最接近目标值，并返回三数之和。

    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Example:
        Given array nums = [-1, 2, 1, -4], and target = 1.
        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    """
    def symb(self, nums, target):
        """

        :type nums:  List[int]
        :type target: int
        :rtype:  int
        """
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return target
        return result



    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

