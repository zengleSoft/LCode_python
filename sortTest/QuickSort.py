#!/usr/bin/python
# -*- coding: UTF-8 -*-


def quick(list, left, right):
    if left >= right:
        return list
    key = list[left]
    low, high = left, right
    while left < right:
        # 从右开始向左找第一个比key小的数   把left处的值覆盖  此时key记录了left处的值 所以可以覆盖
        while left < right and key <= list[right]:
            right -= 1
        list[left] = list[right]

        while left < right and key >= list[left]:
            left += 1
        list[right] = list[left]

    list[right] = key
    quick(list, low, left - 1)
    quick(list, left + 1, high)
    return list


def quick2(list, left, right):
    if left >= right: return list
    key = list[left]
    begin, end = left, right
    while begin < end:
        # 一定先从右边开始找第一个小于key的数   因为循环外面是left和begin交换 所以必须保证左边始终满足条件
        while begin < end and key < list[end]: end -= 1
        # 判断条件带等于是因为 key是左边第一个取得 如果不带，key第一次就交换走了
        while begin < end and key >= list[begin]:begin += 1
        list[begin],list[end] = list[end],list[begin]
    list[left],list[begin] = list[begin],list[left]
    quick2(list,left,begin-1)
    quick2(list,begin+1,right)
    return list

if __name__ == '__main__':
    import random
    for i in range(10000):
        list = []
        tmp = []
        for i in range(100):
            x = random.randint(0, 99)
            list.append(x)
            tmp.append(x)
        # print list
        tmp.sort()
        list = quick(list, 0, len(list) - 1)
        print tmp == list
    # list = [6,1,5,4,8,3,9,12,51,11,15,14,13,25,69,47,56,74,26,78]
    # print quick(list,0,len(list)-1)
