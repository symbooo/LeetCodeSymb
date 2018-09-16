#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
YES, WE CAN!
@Time        : 2018/9/10 23:54
@Author      : 兰兴宝 echolan@126.com
@File        : 30.SubstringWithConcatenationOfAllWords.py
@Site        : 
@Project     : LeetCodeSymb
@Note        : [describe how to use it]
"""
# Enjoy Your Code


class Solution:
    """
    给你一个字符串s 和一个单词列表 words, 单词长度相同， 找出所有由单词组成的子串在s中的位置，子串中单词有且出现一次

    You are given a string, s, and a list of words, words, that are all of the same length.
    Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
    and without any intervening characters.

    Example 1:
        Input:
          s = "barfoothefoobarman",
          words = ["foo","bar"]
        Output: [0,9]
        Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.
    Example 2:
        Input:
          s = "wordgoodstudentgoodword",
          words = ["word","student"]
        Output: []
    """
    def symb(self, s, words):
        """
        遍历s, 按word长度循环取值对比当前位置之后的单词查找是否是给定单词
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        words_dict = {}
        # 统计words中的每个单词出现次数，存在字典words_dict 中
        for w in words:
            words_dict[w] = (words_dict[w] + 1) if words_dict.get(w) else 1
        result = []
        i = 0
        # 逐字符遍历s
        while i <= (len(s) - total_len):
            # 复制一份样本统计数据
            copy_words = words_dict.copy()
            j, l = i, len(words)
            # 按words中单词长度遍历取值，符合条件则继续
            while (s[j: j + word_len] in copy_words) and l:
                copy_words[s[j: j + word_len]] -= 1
                # 如果某个单词出现次数超过在words中出现的次数，则不满足条件，直接退出
                if copy_words[s[j: j + word_len]] < 0:
                    break
                j += word_len
                l -= 1
            # 如果words中的个数都匹配成功，则加入结果列表总
            if l == 0:
                result.append(i)
            i += 1
        return result

    # 高赞回答
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

    # 另一高赞回答
    def findSubstring1(self, s, words):
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans

if __name__ == '__main__':
    examples = [
        ['', [], [0, ]],
        ["wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8, ]],
        ["wordgoodstudentgoodword", ["word", "student"], []],
        ["lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"], [13, ]],
        ['aaaaaaaaaa', ['aa', 'aa', 'aa', ], [0, 1, 2, 3, 4]],
    ]
    solution = Solution()
    for example in examples:
        print(solution.symb(*example[:2]), ),
        print('answer:', solution.findSubstring(*example[:2]))
        print('another ans: ', solution.findSubstring1(*example[:2]))
