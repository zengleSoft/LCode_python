#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
instance41
'''
def instance41_test1():
    var=0
    print 'var=%d'%var
    var+=1

'''
instance44
'''
def instance44_test1():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]
    result = [[0, 0,0 ],
         [0, 0, 0],
         [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j]=X[i][j]+Y[i][j]
    print result

'''
instance45
'''
def instance45_test1():
    tmp=0
    for i in range(1,101):
        tmp+=i
    print tmp

'''
instance46
'''
def instance46_test1():
    pass




if __name__ == '__main__':
    instance46_test1()





# class Static:
#     StaticVar=5
#     def varfunc(self):
#         self.StaticVar+=1
#         print self.StaticVar

# print Static.StaticVar
# a=Static()
# for i in range(3):
#     a.varfunc()

