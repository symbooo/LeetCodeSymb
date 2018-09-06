#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/9/7 0:22
@Author      : 兰兴宝 echolan@126.com
@File        : 26.RemoveDuplicatesFromSortedArray.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给出一个有序数组，在原数组中移除重复值，每个元素只出席那一次，返回新的数组长度，不可以新建数组，使用常量额外空间。

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
        Given nums = [1,1,2],
        Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

        It doesn't matter what you leave beyond the returned length.
    Example 2:
        Given nums = [0,0,1,1,1,2,2,3,3,4],
        Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

        It doesn't matter what values are set beyond the returned length.

    Clarification:
        Confused why the returned value is an integer but your answer is an array?
        Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

        Internally you can think of this:
            // nums is passed in by reference. (i.e., without making a copy)
            int len = removeDuplicates(nums);

            // any modification to nums in your function would be known by the caller.
            // using the length returned by your function, it prints the first len elements.
            for (int i = 0; i < len; i++) {
                print(nums[i]);
            }
    """
    def symb(self, nums):
        """

        :type nums:  List[int]
        :rtype:  int
        """
        cur = 0
        for x in nums:
            if nums[cur] == x:
                continue
            else:
                cur += 1
                nums[cur] = x
        return cur + 1 if nums else 0

    # 高赞解答
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.symb(nums)

