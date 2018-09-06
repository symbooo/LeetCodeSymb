#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/31 17:40
@Author      : 兰兴宝 echolan@126.com
@File        : comment.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class ListNode:
    def __init__(self, x):
        self.__values = x
        self.val = x
        self.next = None
        self.set(x)

    def set(self, values):
        if values:
            self.val = values[0]
            self.next = ListNode(values[1:]) if values[1:] else None
