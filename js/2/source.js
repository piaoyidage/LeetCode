/*
* @Author: maoying.hu
* @Date:   2018-08-28 16:53:13
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-08-28 19:30:35
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
    let numArr1 = getNum(l1)
    let numArr2 = getNum(l2)

    const len1 = numArr1.length
    const len2 = numArr2.length

    // 将两个数组处理成一样的长度，用 0 填充
    if (len1 < len2) {
        numArr1 = numArr1.concat(Array(len2 - len1).fill(0))
    } else {
        numArr2 = numArr2.concat(Array(len1 - len2).fill(0))
    }

    const max = len1 > len2 ? len1 : len2
    const sum = []
    // 进位
    let carry = 0
    let cur = 0
    let i = 0
    while (i < max) {
        cur = parseInt(numArr1[i]) + parseInt(numArr2[i]) + carry
        if (cur >= 10) {
            carry = 1
            sum.push(cur - 10)
        } else {
            carry = 0
            sum.push(cur)
        }
        i++
    }
    if (carry === 1) {
        sum.push(1)
    }

    return sum
}

// 获取链表表示的数字
const getNum = function(l) {
    const numbers = [l.val]
    let nextNode = l.next
    while (nextNode) {
        numbers.push(nextNode.val)
        nextNode = nextNode.next
    }
    return numbers.join('')
}
