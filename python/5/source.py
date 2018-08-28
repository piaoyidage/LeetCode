#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-8
@author: Ben
'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        # 返回最长的回文子字符串
        # 使用Manacher‘s Algorithm 
        # 首先构造新的字符串，新的字符串将是奇数字符串
        # aba->#a#b#a# abccab->#a#b#c#c#b#a#
        T = '#'.join(s)
        T = '#' + T + '#'
        i, right, center = 0, 0, 0
        P = []
        while i < len(T):
            P.append(0)
            if right > i:
                # 分三种情况
                # i关于中心center对称点j
                j = center * 2 - i 
                # 1
                if P[j] < right-i:
                    P[i] = P[j]
                # 2
                elif P[j] > right-i:
                    P[i] = right - i
                # 3
                else:
                    P[i] = right-i
                    k = 1
                    while (i*2-right-k)>=0 and (k+right)<len(T) and T[i*2-right-k] == T[k+right]:
                        P[i] = P[i] + 1
                        k = k + 1
            else:
                k = 1
                while i-k>=0 and i+k<len(T) and T[i-k] == T[i+k]:
                    P[i] = P[i] + 1
                    k = k + 1
            center = i 
            right = center + P[i]
            i = i + 1
        # P中最大值
        len_max = max(P)
        # P中最大值的索引
        index_max = P.index(len_max)
        # 分两种情况
        # 1.偶数个回文串
        if T[index_max] == '#':
            index_max_s = index_max // 2
            return s[index_max_s-len_max//2:index_max_s+len_max//2]
        # 2.奇数个回文串
        else:
            index_max_s = index_max // 2
            return s[index_max_s-len_max//2:index_max_s+len_max//2+1]

so = Solution()
# print(so.longestPalindrome('ababa'))
print(so.longestPalindrome('abba'))
# print(so.longestPalindrome('ccc'))
