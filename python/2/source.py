#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-1-7
@author: Ben
'''
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        # 传入的是两个链表的头
        # 遍历获取各个节点，计算存储的整数值
        num_1, num_2 = 0, 0
        p, q = l1, l2
        i, j = 0, 0
        while p != None:
            num_1 = num_1 + p.val*math.pow(10, i)
            p = p.next
            i = i + 1
        while q != None:
            num_2 = num_2 + q.val*math.pow(10, j)
            q = q.next
            j = j + 1
        num_3 = int(num_1 + num_2)
        # 整数转字符串，便于截取各个位上的数
        num_s = str(num_3)
        # 设置链表头，以及前一个节点
        head = None
        previous = None
        for i in range(len(num_s)):
            value = int(num_s[len(num_s)-i-1:len(num_s)-i])
            node = ListNode(value)
            if i == 0:
                head = node
            else:
                previous.next = node
            previous = node 
        return head
    
so = Solution()

node_1 = ListNode(2)
node_2 = ListNode(4)
node_1.next = node_2
node_3 = ListNode(3)
node_2.next = node_3
l1 = node_1

node_4 = ListNode(5)
node_5 = ListNode(6)
node_4.next = node_5
node_6 = ListNode(4)
node_5.next = node_6
l2 = node_4

l1 = ListNode(0)
l2 = ListNode(0)
print(so.addTwoNumbers(l1, l2).val)
