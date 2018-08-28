#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-7
@author: Ben
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # A,B是已经排好序的数组，长度分别是m, n，找中位数，time complexity O(log(m+n))
        C = []
        m, n = len(A), len(B)
        a, b = 0, 0
        while a < m and b < n:
            if A[a] < B[b]:
                    C.append(A[a])
                    a = a + 1
            else:
                C.append(B[b])
                b = b + 1
        if a < m:
            for i in range(a, m):
                C.append(A[a])
                a = a + 1
        if b < n:
            for i in range(b, n):
                C.append(B[b])
                b = b + 1
        # 如果m+n的和是偶数，中位数是中间两个数的平均数，否则是中间数
        return (float)(C[len(C)/2] + C[len(C)/2-1])/2 if len(C) % 2 == 0 else C[len(C)/2]
    
so = Solution()
# A = [1, 3, 5]
# B = [2, 4, 6, 8, 10]
# A = [1]
# B = [1]
A = []
B = [2, 3]
print so.findMedianSortedArrays(A, B)
