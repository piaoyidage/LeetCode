#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-3-25
@author: Ben
'''

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        # 负数不会是回文数
        if x < 0:
            return False
        result = ''
        # 整型转字符串，方便处理
        s = str(x)
        for i in range(len(s)):
            result = result + s[len(s)-i-1]
        result_int = int(result)
        # 处理Overflow
        if result_int > math.pow(2, 31):
            return False
        return result_int == x