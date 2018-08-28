#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-8
@author: Ben
'''
import math

class Solution:
    # @return an integer
    def reverse(self, x):
        result = ''
        abs_x = abs(x)
        # 整型转字符串，方便处理
        s = str(abs_x)
        for i in range(len(s)):
            result = result + s[len(s)-i-1]
        # 负数注意加上‘-’
        result_int = int(result) if x >= 0 else int(result)*(-1)
        # 处理Overflow
        if result_int > math.pow(2, 31) or result_int < math.pow(2, 31)*(-1):
            return 0
        return result_int 
    
so = Solution()
print so.reverse(1534236469)
print so.reverse(153000)
print so.reverse(-2147483648)
print so.reverse(1563847412)
