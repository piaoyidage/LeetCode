#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-8
@author: Ben
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        # 只有一行时
        if nRows == 1:
            return s
        # 将行号和每行的字符串建立映射
        row_str = {}
        for i in range(nRows):
            row_str.setdefault(i, '')
        i, row = 0, 0
        # 设置一个标志，当前zigzag的方向，是向下还是向上，默认向下
        flag = True
        while i < len(s):
            row_str[row] = row_str[row] + s[i]
            if flag:
                row = row + 1
                # 当达到最下面的一行，调整方向
                if row == nRows:
                    row = row - 2
                    flag = False
            else:
                row = row - 1
                # 当达到最上面一行，调整方向
                if row == -1:
                    row = row + 2
                    flag = True
            i = i + 1
        result = ''
        for i in range(nRows):
            result = result + row_str[i]
        return result
         

so = Solution()
print(so.convert('AB', 1))
print(so.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
