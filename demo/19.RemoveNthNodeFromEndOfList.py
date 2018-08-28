#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/28 17:23
@Author      : 兰兴宝 echolan@126.com
@File        : 19.RemoveNthNodeFromEndOfList.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """

    """
    def symb(self, head, n):
        """
        :type head:  ListNode
        :type n:  int
        :rtype:  ListNode
        """
        node = head
        length = 0
        next_node = head.next
        while next_node is not None:
            length += 1
            next_node = next_node.next
        length = length - n
        next_node = node
        while length > 0:
            length -= 1
            next_node = next_node.next
        next_node.next = next_node.next.next
        return node

    # 膜拜大神
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions/169622
    # 解体思路：
    #   两个指针fast 和slow， fast先前进n步，slow和fast永远差n，当fast是最后一个的时候，slow就是倒数第n个

    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
