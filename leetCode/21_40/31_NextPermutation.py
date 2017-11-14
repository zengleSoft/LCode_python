#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
http://www.cnblogs.com/grandyang/p/4428207.html
'''

class Solution(object):
    def nextPermutation(self,nums):
        if not nums or len(nums)<2:
            return
        flag=True
        # 从后向前寻找第一个减小的数
        for i in range(len(nums)-1,0,-1):
            start = i-1
            if nums[i]>nums[start]:
                break
        else:   # 如果没有找到 说明数组是降序排列  直接反转返回
            flag=False
            start=-1
        if flag:
            # 从后向前寻找第一个大于 nums[start] 的数 交换
            for i in range(len(nums)-1,start,-1):
                if nums[i]>nums[start]:
                    nums[start],nums[i] = nums[i],nums[start]
                    break
        # 将start后面的数字反转
        i,j = start+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

if __name__ == '__main__':
    self = Solution()
    print self.nextPermutation([1,2])
