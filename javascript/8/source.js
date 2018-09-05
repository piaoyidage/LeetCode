/*
* @Author: maoying.hu
* @Date:   2018-09-05 17:56:58
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-09-05 20:29:12
*/

/**
 * @param {string} str
 * @return {number}
 */
const myAtoi = function(str) {
    const result = +str
    const MAX = Math.pow(2, 31) - 1
    const MIN = -Math.pow(2, 31)
    let c = str[0]
    if (isNaN(result) || str.indexOf('e') !== -1) {
        if (isNaN(+c) && !(c === '-' || c === '+')) {
            return 0
        } else {
            let newS = ''
            let s = ''
            let i = 0
            // 找到第一个不是空格的字符
            for (let j = 0, len = str.length; j < len; j++) {
                if (str[j] !== ' ') {
                    newS = str.slice(j)
                    break
                }
            }
            c = newS[0]
            if (isNaN(+c) && !(c === '-' || c === '+')) {
                return 0
            }
            while(1) {
                s += c
                c = newS[++i]
                if (isNaN(+c) || c === ' ' || c === 'e') {
                    break
                }
            }
            let r = +s
            if (isNaN(s)) {
                return 0
            } else if (r > MAX) {
                return MAX
            } else if (r < MIN) {
                return MIN
            }
            return r
        }
    } else if (result > MAX) {
        return MAX
    } else if (result < MIN) {
        return MIN
    }
    return result
};