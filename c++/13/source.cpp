/**
 * @author piaoyidage
 * @version 创建时间：2015-06-09 21:52:54
 *
 */ 

class Solution {
public:
    int romanToInt(string s) {
        // 判断s为空时
        if (s == "")
        {
            return 0;
        }

        int num = 0;
        // 获取尾部字符
        string curS = s.substr(s.length()-1);
        // 更新s
        s = s.substr(0, s.length()-1);

        // 分为7种情况
        if (curS == "I")
        {
            num += 1;
            num += romanToInt(s);
            return num;
        }

        if (curS == "V")
        {
            num = getNum(s, "V", "I", 5);
            return num;
        }
        if (curS == "X")
        {
            num = getNum(s, "X", "I", 10);
            return num;
        }
        if (curS == "L")
        {
            num = getNum(s, "L", "X", 50);
            return num;
        }
        if (curS == "C")
        {
            num = getNum(s, "C", "X", 100);
            return num;
        }
        if (curS == "D")
        {
            num = getNum(s, "D", "C", 500);
            return num;
        }
        if (curS == "M")
        {
            num = getNum(s, "M", "C", 1000);
            return num;
        }
    }

    // 1、V 和X 左边的小数字只能用Ⅰ。
    // 2、L 和C 左边的小数字只能用X。
    // 3、D 和M 左边的小数字只能用C。
    int getNum(string s, string a, string b, int value)
    {
        int num = 0;
        if (s == "")
        {
            num = value;
            return num;
        }
        string curS = s.substr(s.length()-1);
        if (curS == b)
        {
            if (b == "I")
            {
                num += (value-1);
            }
            else if (b == "X")
            {
                num += (value-10);
            }
            else if (b == "C")
            {
                num += (value-100);
            }
            s = s.substr(0, s.length()-1);
        }
        else
        {
            num += value;
        }
        num += romanToInt(s);
        return num;
    }
};
