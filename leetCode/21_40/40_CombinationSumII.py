#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/1/1

'''
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''


class Solutions(object):
    def combinationSum2(self, candidates, target):
        resultList = []
        candidates.sort(reverse=True)
        self.backTrack(candidates, resultList, [], target, 0)
        return resultList

    def backTrack(self, candidates, resultList, tmpList, target, start):
        if target < 0:
            return
        elif target == 0:
            resultList.append([i for i in tmpList])
        else:
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:continue  # 如果和前一个相等说明前一个已经试过不管成功或失败
                tmpList.append(candidates[i])
                self.backTrack(candidates, resultList, tmpList, target - candidates[i], i + 1) #i+1去掉自身，只看后面的
                tmpList.pop()

    def combinationSum3(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for _ in candidates]
        for t in range(1, target + 1):
            duplicate = False
            for val in candidates:
                if val > t:
                    break;
                elif val == t and not duplicate:
                    dp[t].append([val])
                    duplicate = True
                elif val < t:
                    for L in dp[t - val]:
                        if not L or L[-1] <= val:
                            # dp[t] = dp[t] + L + [val]
                            dp[t] += L + [val],
        return dp[target]


if __name__ == '__main__':
    self = Solutions()
    print self.combinationSum2([10, 7, 6, 5, 2, 1, 1], 8)
