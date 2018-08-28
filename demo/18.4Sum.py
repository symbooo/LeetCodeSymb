#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/28 16:54
@Author      : 兰兴宝 echolan@126.com
@File        : 18.4Sum.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给定一个数组nums和一个目标值target，找出所有满足条件（ a + b + c + d = target）的abcd值，组合不可重复。

    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

    Note:

    The solution set must not contain duplicate quadruplets.

    Example:
        Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
        A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
    """
    def symb(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for a in range(len(nums) - 3):                      # 第一层 a
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            middle_target =target - nums[a]
            # is_get_middle_result = True
            for b in range(a + 1, len(nums) - 2):           # 第二层 b
                # if not is_get_middle_result:
                #     break
                if b > a + 1 and nums[b] == nums[b - 1]:     # b 去重
                    continue

                c, d = b + 1, len(nums) - 1                 # 第三层  c, d  斗鸡眼开始
                while c < d:
                    s = nums[b] + nums[c] + nums[d]
                    if s == middle_target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        if result[-1] == [-5, -2, -2, 0]:
                            print(result)
                        c, d = c + 1, d - 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        # is_get_middle_result = True
                    elif s < middle_target:
                        c += 1
                    else:
                        d -= 1
        return result



    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


if __name__ == '__main__':
    solution = Solution()
    examples = [
        [[1, 0, -1, 0, -2, 2], 0],
        [[-1, 0, -5, -2, -2, -4, 0, 1, -2], -9],
    ]
    for example in examples:
        print(example, solution.symb(*example))
