#!/usr/bin/python
# -*- coding: UTF-8 -*-

#冒泡排序
def bubble(list):
    n=len(list)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if(list[j-1]>list[j]):
                list[j-1],list[j]=list[j],list[j-1]
            print list
    print list

def bubble2(list):
    n=len(list)
    for i in range(0,n):
        for j in range(i+1,n):
            if(list[j]<list[i]):
                list[j],list[i]=list[i],list[j]
            print list
    print list

if __name__ == '__main__':
    list=[5,4,3,2,1]
    bubble2(list)