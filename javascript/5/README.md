# 5. 最长回文子串

## 题目

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

### 示例 1：

输入: "babad"

输出: "bab"

注意: "aba"也是一个有效答案。

### 示例 2：

输入: "cbbd"

输出: "bb"

## 解答

使用递归来解决会很简单，代码如下，但是会导致时间效率太差，会超出时间限制！

```js
const longestPalindrome = function(s) {
    if (isPalindrome(s)) {
        return s
    } else {
        const s1 = longestPalindrome(s.slice(1))
        const s2 = longestPalindrome(s.slice(0, -1))
        if (s1.length > s2.length) {
            return s1
        } else {
            return s2
        }

    }
};
```

一种正确的方法是使用循环来做，注意代码中的 **break** 很重要！

```js
const longestPalindrome = function(s) {
    const len = s.length
    if (!len) {
        return ''
    }
    let result = s[0]
    let sc = ''
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            sc = s.slice(i, len - j)
            if (isPalindrome(sc)) {
                if (sc.length > result.length) {
                    result = sc
                }
                // 第一次找到的回文串是以 s[i] 开头的最长串
                break
            }
        }
    }
    return result
};
```
