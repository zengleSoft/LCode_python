#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

def intToRoman(num):
    M = ['','M','MM','MMM']
    # 0 100 200 300...900
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]