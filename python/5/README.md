# 5. Longest Palindromic Substring

编程思路：使用Manacher算法

参考文章1：http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

参考文章2：http://blog.csdn.net/adrastos/article/details/9093779#

参考文章1讲解很好，不过最后的总结有问题，更正一下，计算P[i]分三种情况：

1) if P[i‘]  < R - i then P[i] = P[i’]

2) else if P[i‘] > R - i  then P[i] = R - i

3) else if P[i’] = R - i then P[i] >= R-i

前两种情况可以直接根据已经得到的值，计算出当前值，第三种情况则需要进行进一步的扩展，当然扩展也是在P[i] = R-i的基础上
