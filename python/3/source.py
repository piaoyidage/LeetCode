#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-7
@author: Ben
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        li = []
        len_max = 0
        for i in range(len(s)):
            if not s[i:i+1] in li:
                li.append(s[i:i+1])
                # 如果到字符串结尾：
                if i == len(s)-1:
                    len_cur = len(li)
                    len_max = len_cur if len_cur > len_max else len_max 
            else:
                len_cur = len(li)
                len_max = len_cur if len_cur > len_max else len_max
                # 更新li里面的值，出现重复值之前(包含重复值)的全部去除
                # 得到出现重复值的索引
                index = li.index(s[i:i+1])
                # 注意，每次去除li里面第一个元素，因为去除第一个元素后，更新后的li的一个元素是之前li的第二个元素
                for j in range(index+1):
                    li.remove(li[0])
                li.append(s[i:i+1])
        return len_max
    
so = Solution()
print(so.lengthOfLongestSubstring('abcabc'))
# print(so.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'))
