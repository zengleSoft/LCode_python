#!/usr/bin/python
# -*- coding: UTF-8 -*-

def readCsv():
    import  csv
    with open('D://csvTest.csv','r') as f:
        csv_reader = csv.reader(f)
        # 行读  每行返回一个列表
        for row in csv_reader:
            print row
    # 读取指定行
    with open('D://csvTest.csv','r') as f:
        csv_reader = csv.reader(f)
        for i,row in enumerate(csv_reader):
            if i==1:
                print row

def writeCsv():
    import csv
    # 以wb方式打开 避免空行
    with open('D://csvTest.csv','wb') as out:
        list = [1,2,3,4,'a']
        list2 = ['ca','sad','fdsa']
        csv_write = csv.writer(out, delimiter='|')
        # 写入一行  参数必须是list
        csv_write.writerow(list)
        csv_write.writerow(list2)


if __name__ == '__main__':
    readCsv()
