#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/8/29 9:44
@Author      : 兰兴宝 echolan@126.com
@File        : 22.GenerateParentheses.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给出n对括号，写一个函数，生成所有合法的括号组合。

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
    """
    def symb(self, n):
        """
        此解法没通过检验，还有问题没解决
        我称此法为 括号插入法
        思路如下：
        每次插入一对括号 '()'
        当n = 1 时， 结果为 '()'
        当n = 2时， 可加入位置为1的 1 和 2节点，即结果为 '(())', '()()'
        当n = 3时，可在 '(())' 的2，3，4位置分别插入；可在 '()()' 的 3，4插入 结果为 '((()))', '(()())', '(())()',    '()(())', '()()()'
        ...
        当n = i时， 可在A(i-1) 的 0 元素上的 i-1, i, ..., 2*(i-1)

        :type n:  int
        :rtype: List[str]
        """
        if n <= 1:
            return ['()'] if n else ['']

        answer = [
            ['(', ')'],
        ]
        nums = 1
        while nums < n:
            result = []
            for i, ans in enumerate(answer):
                in_place = i + nums
                while in_place <= 2 * nums:
                    l = ans.copy()
                    l.insert(in_place, ')')
                    l.insert(in_place, '(')
                    result.append(l)
                    in_place += 1
            answer = result
            nums += 1
        return [''.join(a) for a in answer]

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right - 1)
            if not right:    parens += p,
            return parens

        return generate('', n, n)

    def generateParenthesis2(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right): yield q
                for q in generate(p + ')', left, right - 1): yield q

        return list(generate('', n, n))

    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + \
                   [')' + p for p in self.generateParenthesis(n, open - 1)]
        return [')' * open] * (not n)


if __name__ == '__main__':
    solution = Solution()
    examples = [3, 4, ]
    for example in examples:
        print(example, solution.symb(example))
