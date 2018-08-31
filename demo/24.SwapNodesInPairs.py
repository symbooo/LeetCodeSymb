#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/31 1:13
@Author      : 兰兴宝 echolan@126.com
@File        : 24.SwapNodesInPairs.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    输入一个链表，每隔两个数交换一次。不允许直接交换节点的值，只可以使用常量额外空间

    Given a linked list, swap every two adjacent nodes and return its head.

    Example:
        Given 1->2->3->4, you should return the list as 2->1->4->3.
    Note:
        Your algorithm should use only constant extra space.
        You may not modify the values in the list's nodes, only nodes itself may be changed.
    """
    def symb(self, head):
        """
        :type head: ListNode
        :return:  ListNode
        """
        if not head or not head.next:     # 输入为空或者之后一个元素，直接返回
            return head
        ans = head.next
        before_last = None                 # 记录上次循环的最后一个节点
        while head and head.next:          # 当后续依然2个及以上的值时，继续下一次循环交换
            first, next = head, head.next
            if before_last:                # 上一次循环最后一个节点链接到本次循环的第二个节点
                before_last.next = next
            next_next = next.next          # 记录第二个元素的下一个节点
            first.next, next.next = next.next, first
            head = next_next
            before_last = first
        return ans

    # 高赞答案
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    # Recursively  递归法
    def swapPairs1(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head


if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    examples = [
        node,
    ]

    solution = Solution()
    for example in examples:
        print(example, solution.symb(example))
