#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/25 14:58
@Author      : 兰兴宝 echolan@126.com
@File        : 4.MedianOfSortedArrays.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class MedianOfSortedArrays:
    """
    给定两个长度分别未m，n的有序数组nums1，nums2， 查找他们的中位数，要求时间复杂度为 O(log(m + n).
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    Example 1:
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0
    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5
    """

    def symb(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 待完善
        # m, n = len(nums1), len(nums2)
        # median_nums1 = nums1[m // 2]
        # median_nums2 = nums2[n // 2]
        # if min(nums1[m // 2 - 1], nums2[n // 2 - 1], median_nums1, median_nums2) in (nums1[m // 2 -1], nums2[n // 2 - 1]) \
        #     and max(nums1[m // 2 + 1], nums2[n // 2 + 1], median_nums1, median_nums2) in ():
        #     pass
        #
        # if median_nums1 <= median_nums2:
        #     return self.symb(nums1[m // 2:], nums2[: n // 2])
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        l = (m + n) // 2 + 1
        index_a, index_b = m // 2, n // 2
        a_start, b_start = 0, 0
        while True:
            if nums1[index_a - 1] < nums2[index_b] and nums2[index_b - 1] < nums1[index_a]:
                break
            if nums1[index_a] < nums2[index_b]:
                l -= index_a - a_start
                a_start = index_a
                plus = (m - index_a) // 2
                index_a += plus if plus else 1
                index_b -= plus if plus else 1
            else:
                l -= index_b - b_start
                b_start = index_b
                sub = (index_a - a_start) // 2
                index_a -= sub if sub else 1
                index_b += sub if sub else 1
        result = min(nums1[index_a], nums2[index_b])
        if (m + n) % 2 == 0:
            result = (result + max(nums1[index_a - 1], nums2[index_b - 1])) / 2
        return result


    # # 高赞实现
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     pass

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)


if __name__ == '__main__':
    mofa = MedianOfSortedArrays()
    median = mofa.symb([1,4,], [3,5,6,8,9,11,])
    print(median)
