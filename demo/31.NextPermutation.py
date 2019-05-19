#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/11/19 16:20
@Author      : 兰兴宝 echolan@126.com
@File        : 31.NextPermutation.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code
from typing import List


class Solution:
    """

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.
    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """
    def symb(self, nums: List[int]) -> None:
        """

        :type nums: List[int]
        :rtype: void ,原地修改，不返回
        """
        length, i = len(nums), -1
        while length + i > 0:
            if nums[i] > nums[i - 1]:
                j = -1
                while i <= j:
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                    j -= 1
                nums[i:] = sorted(nums[i:])
                break
            i -= 1
        else:
            nums[:] = sorted(nums)

    def nextPermtation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return None
        i = len(nums) - 1
        j = -1  # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i - 1] < nums[i]:  # first one violates the trend
                j = i - 1
                break
            i -= 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[j]:  #
                nums[i], nums[j] = nums[j], nums[i]  # swap position
                nums[j + 1:] = sorted(nums[j + 1:])  # sort rest
                return


if __name__ == '__main__':
    examples = [[1, 2, 3], [3, 2, 1], [1, 3, 2]]
    solution = Solution()
    for example in examples:
        print(example, end=' --> ')
        solution.symb(example)
        print(example)
