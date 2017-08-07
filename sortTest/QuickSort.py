#!/usr/bin/python
# -*- coding: UTF-8 -*-


def quick(list,left,right):
    if left >= right:
        return list
    key = list[left]
    low,high = left,right
    while left<right:
        #从右开始向左找第一个比key小的数   把left处的值覆盖  此时key记录了left处的值 所以可以覆盖
        while left < right and key <= list[right]:
            right -= 1
        list[left] = list[right]

        while left < right and key >= list[left]:
            left += 1
        list[right] = list[left]

    list[right] = key
    quick(list,low,left-1)
    quick(list,left+1,high)
    return list

if __name__ == '__main__':
    import random
    for i in range(10000):
        list = []
        tmp = []
        for i in range(10):
            x = random.randint(0,99)
            list.append(x)
            tmp.append(x)
        # print list
        tmp.sort()
        list = quick(list,0,len(list)-1)
        print tmp==list
