#!/usr/bin/python
# -*- coding: UTF-8 -*-

def tupleTest():
    # 只有一个元素时需要添加都好来消除歧义
    t1 = (1,)
    print t1[0]
    # 截取操作 可字符串操作类似
    t2 = (1,2,3,'a')
    print t2[::-1]
    for i in t2:
        print i

def listTest():
    list = ['a','b',1,'c','d']
    print list[1:4]
    # 修改列表项
    list[1] = 'xx'
    print list
    # 列表插入元素
    list.append('qq')
    print list
    # 删除列表元素  del根据索引删除   remove根据元素删除，只删除第一次出现的
    del list[3]
    print list
    list.remove(1)
    print list
    # 统计某个元素在列表中出现的次数
    print list.count('xx')
    # 排序
    list.sort()
    print list
    # 指定索引处插入元素
    list.insert(3,'aa')
    print list
    # 在列表某位追加序列
    list.extend((1,2,3))
    print list
    # 弹出索引处元素  默认最后一个元素
    print list.pop(2)
    print list

def dicTest():
    dict={'a':1,'v':32,34:'xx'}
    print dict[34]
    # 增加、修改键值对
    dict['b']='c'
    dict['v']= 33
    print dict
    # 字典删除、清空
    del dict['a']
    print dict
    # dict.clear()
    print dict
    # 遍历
    for key in dict.keys():
        print key
    for value in dict.values():
        print value
    for k,v in dict.items():
        print k,v
    # 和get类似 如果key不存在则插入 value为第二个参数
    dict.setdefault('v',222)
    print dict


# 无序不重复元素集
def setTest():
    s = set('abdbb')
    print s
    # 添加元素
    s.add('acd')
    print s
    # update是把元素拆开插入
    s.update('abcde')
    print s
    #
    s1 = set('runoob')
    s2 = set('google')
    # 交集
    print s1 & s2
    # 并集
    print s1 | s2
    # 差集
    print s1 - s2



if __name__ == '__main__':
    setTest()
