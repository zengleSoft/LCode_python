#!/usr/bin/python
# -*- coding: UTF-8 -*-

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# PAYPALISHIRING
# P   A   H   N
# A P L S I I G
# Y   I   R
# 将字符串转换成z字型

def convert(s, numRows):
    listStr = []
    if numRows<2:
        return s
    for i in range(numRows):
        # 当前行索引
        current = i
        # 记录是当前行的第几个字符
        tmp = 0
        while current>=0 and current<len(s):
            tmp +=1
            listStr.append(s[current])
            if i==numRows-1:
                current += 2*(numRows-1)
            else:
                if i==0 or tmp%2<>0:
                    current += 2*(numRows-1-i)
                else:
                    current += 2*i
    return ''.join(listStr)

if __name__ == '__main__':
    print convert('PAYPALISHIRING',4)