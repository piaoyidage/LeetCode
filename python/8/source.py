#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-12
@author: Ben
'''
import math


class Solution:
    # @return an integer
    def atoi(self, str):
        # 首先清除首尾空格
        str = str.strip()
        # 如果是空
        if str == '':
            return 0
        try:
            if str[0] == '+' or str[0] == '-':
                result = str[0]
            else:
                # 如果第一个字符不能转换成整数，则进入except 
                first = int(str[0])
            result = str[0]
            for i in range(1, len(str)):
                try:
                    # 如果不能转换成整数，则进入except
                    value = int(str[i])
                    result = result + str[i]
                except:
                    if result[0] == '-':
                        result_int = int(result[1:]) * (-1)
                    elif result[0] == '+':
                        result_int = int(result[1:])
                    else:
                        result_int = int(result)
                    if result_int >= math.pow(2, 31):
                        return int(math.pow(2, 31)-1)
                    if result_int < math.pow(2, 31) * (-1):
                        return int(math.pow(2, 31) * (-1))
                    return result_int
           
            if result[0] == '-':
                    result_int = int(result[1:]) * (-1)
            elif result[0] == '+':
                    result_int = int(result[1:])
            else:
                    result_int = int(result)
            if result_int >= math.pow(2, 31):
                return int(math.pow(2, 31)-1)
            if result_int < math.pow(2, 31) * (-1):
                return int(math.pow(2, 31) * (-1))
            return result_int   
        except:
            return 0
        
so = Solution()
# print so.atoi('str')
# print so.atoi(' 12345')
# print so.atoi('123')
# print so.atoi('123fs')
# print so.atoi(' 22 fs')
# print so.atoi(' -22 fs')
print so.atoi('2147483648')
print so.atoi('-2147483648')
print so.atoi('      -11919730356x')
