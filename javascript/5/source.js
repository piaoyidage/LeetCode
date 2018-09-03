/*
* @Author: maoying.hu
* @Date:   2018-09-03 10:50:15
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-09-03 13:24:40
*/

/**
 * @param {string} s
 * @return {string}
 */
// const longestPalindrome = function(s) {
//     if (isPalindrome(s)) {
//         return s
//     } else {
//         const s1 = longestPalindrome(s.slice(1))
//         const s2 = longestPalindrome(s.slice(0, -1))
//         if (s1.length > s2.length) {
//             return s1
//         } else {
//             return s2
//         }

//     }
// };

/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function(s) {
    const len = s.length
    if (!len) {
        return ''
    }
    let result = s[0]
    let sc = ''
    for (let i = 0; i < len; i++) {
        if (result.length > len - i) {
            break
        }
        for (let j = 0; j < len; j++) {
            sc = s.slice(i, len - j)
            if (isPalindrome(sc)) {
                if (sc.length > result.length) {
                    result = sc
                }
                break
            }
        }
    }
    return result
};

// 判断一个字符串是不是回文串
const isPalindrome = function(s) {
    const len = s.length
    for (let i = 0; i < len / 2; i++) {
        if (s[i] !== s[len - i - 1]) {
            return false
        }
    }
    return true
}