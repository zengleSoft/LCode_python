#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
open函数三种模式 r、w、a 分别是读、写、追加  默认是读
r必须存在文件 w和a不存在则创建
读写模式是 r+
'''

def readFileTest():
    f = open('D://input.txt','r')
    # 一次读取文件所有内容
    # print f.read()
    # 行读
    # print f.readline()
    # 读取所有行返回list
    print f.readlines()
    f.close()
    # 使用with as代替 try finally
    with open('D://input.txt','r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            print line.strip()
            f.write('xx')

def writeFileTest():
    with open('D:testWrite.txt','w') as f:
        f.write('aaaaa')
        f.write('\n')
        f.write('bbbb')
    # 一次写入多行  需要手动加入换行符
    list = ['aaaa','cccc','dddd']
    with open('D:testWrite.txt','w') as f:
        list = map(lambda x:x.strip()+'\n',list)
        f.writelines(list)

# 文件夹、文件操作  os模块和shutil模块
def dirTest():
    import os
    # 当前目录
    print os.getcwd()
    # 返回指定目录下的所有文件和目录名  list
    print os.listdir('D://')
    # 检测是文件或目录
    print os.path.isfile('D://testWrite.txt')
    print os.path.isdir('D://')
    # 返回文件大小  单位字节
    print os.path.getsize('D://testWrite.txt')
    # 自动根据操作系统设定路径连接符
    print os.path.join('D://testDir','testWrite.txt')

if __name__ == '__main__':
    dirTest()