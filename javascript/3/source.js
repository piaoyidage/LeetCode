/*
* @Author: maoying.hu
* @Date:   2018-08-29 11:01:10
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-08-29 11:59:31
*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // 最长子串
    const strArr = []
    let findIdx = -1
    for(let i = 0; i < s.length; i++) {
        findIdx = strArr.indexOf(s[i])
        if (findIdx === -1) {
            strArr.push(s[i])
        } else {
            // 比较
            const restLen = lengthOfLongestSubstring(s.slice(findIdx + 1))
            const len = strArr.length
            return len > restLen ? len : restLen
        }
    }
    return strArr.length
};