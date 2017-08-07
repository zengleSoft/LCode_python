#!/usr/bin/python
# -*- coding: UTF-8 -*-

# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5
def findMedianSortedArrays(nums1,nums2):
    len1,len2 = len(nums1),len(nums2)
    #找出第num大的数
    num = (len1+len2)/2+1
    #x，y记录nums1和nums2遍历位置  target记录当前数   before记录比target小一个的数
    x,y,target,before = 0,0,0,0
    for i in range(num):
        #记录上一个数
        before = target
        #找出当前target应该从那个数组中取
        if x<len1 and y<len2 and nums1[x]<=nums2[y]:
            target = nums1[x]
            x += 1
        elif x>=len1:       #如果x超范围 直接取y的
            target = nums2[y]
            y += 1
        elif y>=len2:
            target = nums1[x]
            x += 1
        else:
            target = nums2[y]
            y += 1
    #如果两列表元素个数和是奇数  那么直接取target就行了  before不用管
    if (num-1)*2<len1+len2:
        before = target
    return (before+target)/2.0



if __name__ == '__main__':
    findMedianSortedArrays([2],[])