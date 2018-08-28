#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-6
@author: Ben
'''
import math

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
             'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
             'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        n = len(s)
        num = 0
        i = 0
        while i < n:
            # 使用切片获取每个字母
            num = num + d[s[i:i+1]] * math.pow(26, n-1-i)
            i = i + 1
        return int(num) 
    
so = Solution()
print so.titleToNumber('AAA')
