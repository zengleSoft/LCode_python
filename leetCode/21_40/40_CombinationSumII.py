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
        pass

    def combinationSum4(self,candidates,target):
        candidates.sort()
        dp = [set() for i in xrange(target + 1)]
        dp[0].add(())
        for num in candidates:   # 以candidates为外层循环 避免
            for t in xrange(num,target+1):  # 反向循环 避免元素多次使用
                for prev in dp[t - num]:
                    dp[t].add(prev + (num,))  # set中添加元祖  去重
        return list(dp[-1])

if __name__ == '__main__':
    self = Solutions()
    print self.combinationSum4([10, 7, 6, 5, 2, 1, 1], 8)
