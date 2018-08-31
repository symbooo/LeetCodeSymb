#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/31 16:08
@Author      : 兰兴宝 echolan@126.com
@File        : 25.ReverseNodesInK-Group.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code
from comment import ListNode


class Solution:
    """
    k个一组翻转链表

    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    Example:
        Given this linked list: 1->2->3->4->5
        For k = 2, you should return: 2->1->4->3->5
        For k = 3, you should return: 3->2->1->4->5
    Note:
        Only constant extra memory is allowed.
        You may not alter the values in the list's nodes, only nodes itself may be changed.
    """
    def symb(self, head, k):
        """

        :type head:  ListNode
        :type k: int
        :rtype:  ListNode
        """
        fast = slow = ListNode(0)
        i, j = 0, 0
        fast.next = head
        while i < k:
            fast = fast.next
            i += 1
            if not fast:
                return head
        pre_node = slow
        have_next_k_group = True
        while j < k:
            tmp = head.next.next
            head.next.next = head
            head = tmp
            if have_next_k_group:
                fast = fast.next
                if not fast:
                    have_next_k_group = False
            j += 1
            if j == k:
                pre_node.next = head.next
                pre_node = pre_node.next
                head = head.next
                j = 0
                if not have_next_k_group:
                    break
        return slow.next

