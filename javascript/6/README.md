# 6. Z字形变换

## 题目

将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

```
P   A   H   N
A P L S I I G
Y   I   R
```

之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

```
string convert(string s, int numRows);
```

### 示例 1:

输入: s = "PAYPALISHIRING", numRows = 3

输出: "PAHNAPLSIIGYIR"

### 示例 2:

输入: s = "PAYPALISHIRING", numRows = 4

输出: "PINALSIGYAHRPI"

解释:

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

## 解答

思路比较清晰，row, col 表示当前前进的二维坐标，direction 来表示当前 z 走向，其中需要注意什么时候改变 direction!

```js
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
```
