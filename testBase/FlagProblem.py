#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
荷兰国旗问题
'''

def flagSort(list):
    i,j,k=0,0,len(list)-1
    while k>=j:
        if list[k]<1:
            list[j],list[k]=list[k],list[j]
            if list[j]<0:
                list[i],list[j]=list[j],list[i]
                i+=1
            j+=1
        else:
            k-=1


if __name__ == '__main__':
    list=[123,43,0,-2,0,1,-6,-234,66,0,0,2,-5]
    flagSort(list)
    print list