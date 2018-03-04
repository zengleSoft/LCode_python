#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/1

'''
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

'''


class Solution(object):
    # 最短路径 广度优先搜索
    def jump(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if len(nums) < 2: return 0
        # max_range 记录当前step的终点   next_range始终记录能到达的最远索引
        step, max_range, next_range = 1, nums[0], nums[0]
        for i in range(1, len(nums)+1):
            # 先判断当前层数的终点能都到底
            if max_range >= len(nums) - 1:
                return step
            # 循环进入下一层
            if i > max_range:
                max_range = next_range
                step += 1
            # 更新最远点
            next_range = max(next_range, i + nums[i])

if __name__ == '__main__':
    self = Solution()
    print self.jump([1,2,3])
