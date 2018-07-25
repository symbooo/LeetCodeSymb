#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/7/19 16:59
@Author      : 兰兴宝 echolan@126.com
@File        : AddTwoNumbers.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class AddTwoNumbers:
    """
    给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头。
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
    """

    # 最开始实现的,用列表冒充了链表，惭愧惭愧
    def symb(self, l1, l2):
        """
        :type l1:  ListNode
        :type l2:  ListNode
        :rtype: ListNode
        """
        l1_length = len(l1)
        l2_length = len(l2)
        max_length = max(l1_length, l2_length)
        result = list()
        carry = 0    # 进位
        for i in range(max_length):
            s = (l1[i] if i < l1_length else 0) + (l2[i] if i < l2_length else 0) + carry
            result.append(s % 10)
            carry = s // 10
        if carry:
            result.append(carry)
        return result

    # 高赞实现
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


if __name__ == '__main__':
    l1 = [1, 6, 4, 9]
    l2 = [8, 6, 3, 7]
    atn = AddTwoNumbers()
    l = atn.symb(l1, l2)
    print(l)
