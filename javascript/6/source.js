/*
* @Author: maoying.hu
* @Date:   2018-09-04 10:38:14
* @Last Modified by:   maoying.hu
* @Last Modified time: 2018-09-04 11:51:37
*/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = function(s, numRows) {
    const len = s.length
    if (numRows === 1) {
        return s
    }
    // 构造二维数组，并初始化
    const numArrs = Array(numRows)
    for (let i = 0; i < numRows; i++) {
        numArrs[i] = []
    }
    // 记录运动的走向
    // 1: 直行
    // 0: 斜行
    let direction = 1
    // 当前的二维坐标
    let row = 0
    let col = 0
    let i = 0
    while (i < len) {
        if (direction) {
            for (let j = 0; j < numRows && i < len; j++) {
                numArrs[row++][col] = s[i++]
            }
            col++
            row -= 2
            if (row !== 0) {
                direction = 0
            }
        } else {
            numArrs[row--][col++] = s[i++]
            if (row === 0) {
                direction = 1
            }
        }
    }
    let result = ''
    for (let i = 0; i < numRows; i++) {
        result += numArrs[i].join('')
    }
    return result
};
