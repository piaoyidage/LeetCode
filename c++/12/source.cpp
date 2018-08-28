/**
 * @author piaoyidage
 * @version 创建时间：2015-06-09
 *
 */	


class Solution {
public:
	string intToRoman(int num) {
		// 初始化
		string roman = "";
		
		if (num == 1000)
		{
			roman = "M";
		}
		if (num == 100)
		{
			roman = "C";
		}
		if (num == 10)
		{
			roman = "X";
		}

		// 如果数字大于1000
		if (num > 1000)
		{
			int indexFourth = num / 1000;
			for (int i = 0; i < indexFourth; i++)
			{
				roman += "M";
			}
			roman += intToRoman(num-indexFourth*1000);
		}

	    // 大于100小于100
		if(num > 100 && num < 1000)
		{
			roman = range(num, 100, "C", "D", "M");
		}
        // 大于10小于100
		if (num > 10 && num < 100)
		{
			roman = range(num, 10, "X", "L", "C");
		}
        // 大于0小于10
		if (num > 0 && num < 10)
		{
			roman = range(num, 1, "I", "V", "X");
		}
		
		return roman;
	}
    
    // 根据num值，以及区间、当前区间的罗马标识符，表示当前数字
	string range(int num, int begin, string a, string b, string c)
	{
		string roman = "";

		int index = num / begin;
		switch (index)
		{
		case 1:
		case 2:
		case 3:
			for (int i = 0; i < index; i++)
			{
				roman += a;
			}
			break;
		case 4:
			roman += a;
			roman += b;
			break;
		case 5:
			roman += b;
			break;
		case 6:
		case 7:
		case 8:
			roman += b;
			for (int i = 0; i < index - 5; i++)
			{
				roman += a;
			}
			break;
		case 9:
			roman += a;
			roman += c;
			break;
		}
		roman += intToRoman(num-index*begin);

		return roman;
	}
};