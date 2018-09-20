#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
        """
        resultList = []
        candidates.sort(reverse=True)
        self.backtrack(candidates, resultList, [], target, 0)
        return resultList

    def backtrack(self, candidates, resultList, tmpList, target, start):
        if target < 0:
            return
        elif target == 0:
            resultList.append([i for i in tmpList])
        else:
            for i in range(start, len(candidates)):
                tmpList.append(candidates[i])
                self.backtrack(candidates, resultList, tmpList, target - candidates[i], i)
                tmpList.pop()

    # dp
    def combinationSum2(self, candidates, target):
        candidates.sort()
        # 前面得[[[]]]表示target=0时有一个空解
        dp = [[[]]] + [[] for _ in xrange(target)]
        for t in xrange(1, target + 1):
            for val in candidates:
                if val > t: break
                for L in dp[t - val]:
                    # val >= 保证结果顺序防止重复
                    if not L or val >= L[-1]:
                        dp[t] += L + [val],
        return dp[target]


if __name__ == '__main__':
    self = Solution()
    print self.combinationSum2([2, 3, 6, 7], 7)
