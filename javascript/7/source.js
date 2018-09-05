/*
* @Author: maoying.hu
* @Date:   2018-09-05 17:03:44
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-09-05 17:16:37
*/


/**
 * @param {number} x
 * @return {number}
 */
const reverse = function(x) {
    let result
    if (x > 0) {
        result = +getReverse(x)
    } else {
        result = -+getReverse(-x)
    }
    if (result > Math.pow(2, 31) - 1 || result < -Math.pow(2, 31)) {
        return 0
    }
    return result
};

const getReverse = function(x) {
    const s = x + ''
    let result = ''
    for (let len = s.length, i = len - 1; i >= 0; i--) {
        result += s[i]
    }
    return result
}