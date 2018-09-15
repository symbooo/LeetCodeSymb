#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/9/7 0:47
@Author      : 兰兴宝 echolan@126.com
@File        : 27.RemoveElement.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code

class Solution:
    """
    给出一个列表和一个值，从列表中删除给定的值，返回最终的数组长度

    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
    Example 1:

        Given nums = [3,2,2,3], val = 3,
        Your function should return length = 2, with the first two elements of nums being 2.
        It doesn't matter what you leave beyond the returned length.

    Example 2:

        Given nums = [0,1,2,2,3,0,4,2], val = 2,
        Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
        Note that the order of those five elements can be arbitrary.
        It doesn't matter what values are set beyond the returned length.

    Clarification:
        Confused why the returned value is an integer but your answer is an array?
        Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
        Internally you can think of this:
            // nums is passed in by reference. (i.e., without making a copy)
            int len = removeElement(nums, val);

            // any modification to nums in your function would be known by the caller.
            // using the length returned by your function, it prints the first len elements.
            for (int i = 0; i < len; i++) {
                print(nums[i]);
            }
    """
    def symb(self, nums, val):
        """

        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = 0
        for index, value in enumerate(nums):
            if value == val:
                continue
            if result != index:
                nums[result] = value
            result += 1
        return result

    # 高赞回答
    def removeElement(self, nums, val):
        """
        从左开始往右移动，每碰到一个目标值，就将其交换到列表尾部
        Starting from the left every time we find a value that is the target value we swap it out
         with an item starting from the right. We decrement end each time as we know that the final item
          is the target value and only increment start once we know the value is ok. Once start reaches end
          we know all items after that point are the target value so we can stop there.
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start
