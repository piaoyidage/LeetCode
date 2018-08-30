/*
* @Author: maoying.hu
* @Date:   2018-08-30 10:59:37
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-08-30 11:48:37
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // 如果 nums1 为空
    if (!nums1 || !nums1.length) {
        return getMedian(nums2)
    }
    // 如果 nums2 为空
    if (!nums2 || !nums2.length) {
        return getMedian(nums1)
    }
    // nums1 和 nums2 都不为空
    const merge = []
    const len1 = nums1.length
    const len2 = nums2.length
    let i = 0
    let j = 0
    while (i <= len1 && j <= len2) {
        // 当其中一个遍历结束
        if (i === len1) {
            merge.push(...nums2.slice(j))
            break
        }
        if (j === len2) {
            merge.push(...nums1.slice(i))
            break
        }
        if (nums1[i] < nums2[j]) {
            merge.push(nums1[i])
            i++
        } else {
            merge.push(nums2[j])
            j++
        }
    }
    return getMedian(merge)
};

const getMedian = function(num) {
    const len = num.length
    return len % 2 === 0 ? (num[len / 2 - 1] + num[len / 2]) / 2 : num[(len - 1) / 2]
}
