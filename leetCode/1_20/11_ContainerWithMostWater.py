#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''



def maxArea(height):
    left,right = 0,len(height)-1
    maxArea = (right-left)*min(height[left],height[right])
    while left<right:
        # 每次移动木板短的 因为宽度减一只有让短的移动找到更高的才有可能增大容量
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
        maxArea = max(maxArea,(right-left)*min(height[left],height[right]))
    return maxArea