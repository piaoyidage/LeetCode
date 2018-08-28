#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-6
@author: Ben
'''
import math

class Solution:
    # @return a string
    def convertToTitle(self, num):
        li = list()
        d = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',
             10:'J',11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q',18:'R',
             19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        
        # 确定一共多少个字母
        a = math.log(25*num+26) / math.log(26)
        b = math.log(25*num+26) // math.log(26)
        n = int(a - 1) if a == b else int(a)
        i = n
        while i > 0:
            value = int(num / math.pow(26, i-1))
            num = num - math.pow(26, i-1)*value
            # 如果还未确定后面的各个位置的字母，num变为0，需调整
            if num == 0 and i != 1:
                value = value - 1
                num = num + math.pow(26, i-1)
            li.append(d[value])
            i = i - 1
        return ''.join(li)
        
        
s = Solution()
print s.convertToTitle(26*26*26*26)
