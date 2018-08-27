#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/27 15:15
@Author      : 兰兴宝 echolan@126.com
@File        : 15.3Sum.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给出一个元素为数值的数组， 是否存在元素 a, b, c 使得 a + b + c = 0 ？找出数组中所有唯一的三元组，他们的和为0。

    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note:
        The solution set must not contain duplicate triplets.

    Example:
        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
    """
    def symb(self, nums):
        """
        20180827
        LeetCode用户 yuzhoujr（公瑾）的解法，自己理解后写了一遍

        > 类型：固定区间斗鸡眼
        > Time Complexity O(n^2)
        > Space Complexity O(1)
        大概思路是外围写一个For循环，用于遍历数组。(这里注意，因为我们需要比较3个数，数组的长度设置为range(len(nums) - 2) ， 当i为n - 2的时候完成最后一次比较)

        每次迭代的时候，设置[l,r]的区间，区间范围为l , r = i + 1, len(nums) - 1, 这样比对的数就有3个，分别是nums[i], nums[l] 和 nums[r].
        最终要达到的效果是: nums[i] + nums[l] + nums[r] == 0
        这道题一定要记住去重，不仅仅是区间的l和r要去重，外围的i也需要去重。去重的方法如下:
        i去重： if i > 0 and nums[i-1] == nums[i]: continue
        l去重： while l < r and nums[l] == nums[l-1]: l += 1
        r去重：while l < r and nums[r] == nums[r+1] : r -= 1

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result


    # 高赞实现
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res
