#!/usr/bin/python
# -*- coding: UTF-8 -*-

#选择排序
def select():
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    for i in range(len(a)-1):
        minIndex = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]
    print a