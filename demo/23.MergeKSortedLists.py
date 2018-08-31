#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/31 0:34
@Author      : 兰兴宝 echolan@126.com
@File        : 23.MergeKSortedLists.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    合并k个有序链表并返回，分析和描述他的复杂性。

    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:
        Input:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        Output: 1->1->2->3->4->4->5->6
    """
    def symb(self, lists):
        """
        思路：
        取出每个链表中的第一个值和指针，放入临时列表first_values中，对first_values排序，
        循环每次从first_values中取出第一位，将目标链表的下一位指向该值，再从该值所在的链表中取下一位加入first_values中，直至取完

        :type lists:  List[ListNode]
        :rtype:  ListNode
        """
        if len(lists) < 2:
            return None if not lists else lists[0]
        first_values = [(ln.val, ln) for ln in lists if ln]
        first_values.sort(key=lambda x: x[0])
        ans = step = ListNode(0)
        while first_values:
            min_index, pick_node = first_values.pop(0)
            step.next = pick_node
            pick_node = pick_node.next
            if pick_node:
                i = -1
                length = len(first_values)
                while i + length >= 0 and pick_node.val < first_values[i][0]:
                    i -= 1
                first_values.insert(length + i + 1, (pick_node.val, pick_node))
            step = step.next
        return ans.next

    # 高赞   使用了python内置队列PriorityQueue（优先级队列）
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next


    # @author: yyangbian
    #
    def mergeKLists1(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next


if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None