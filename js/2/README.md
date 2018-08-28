# 2. 两数相加

## 题目

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

## 解答

第一时间可能会写下类似如下的代码：

```js
const addTwoNumbers = function(l1, l2) {
    const sum = getNum(l1) + getNum(l2)
    return getNumList(sum)
}

// 获取链表表示的数字
const getNum = function(l) {
    const numbers = [l.val]
    let nextNode = l.next
    while (nextNode) {
        numbers.push(nextNode.val)
        nextNode = nextNode.next
    }
    return parseInt(numbers.reverse().join('')
}

// 构造数字链表
const getNumList = function(num) {
    const numArr = (num + '').split('').reverse().map(item => parseInt(item))
    return numArr
}；
```

但是上面代码没有考虑数字相加会溢出，正确的方法是：对每一位数字相加减，然后拼接。

