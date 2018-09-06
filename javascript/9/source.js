/*
* @Author: maoying.hu
* @Date:   2018-09-06 18:14:11
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-09-06 18:16:05
*/

const isPalindrome = function(x) {
    const s = x + ''
    const len = s.length
    for (let i = 0; i < len / 2; i++) {
        if (s[i] !== s[len - i - 1]) {
            return false
        }
    }
    return true
}
