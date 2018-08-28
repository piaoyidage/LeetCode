/**
 * @author piaoyidage
 * @version 创建时间：2014-11-07 19:58:21
 *
 */	

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
 
using namespace std;
 
class Solution 
{
public:
	int evalRPN(vector<string> &tokens) 
	{
		// 大致思路：构造一个类似stack的容器，如果是操作数直接存进去，如果是操作符则计算后存进去,最后栈中只有一个数，即是所求
		vector<string> stack;
		vector<string>::iterator iter = tokens.begin();
		vector<string>::iterator iter_s;
		//int i = 0;
		for(; iter != tokens.end(); iter++)
		{
			// 如果是操作数
			if(*iter != "+" && *iter != "-" && *iter != "*" && *iter != "/")
			{
				stack.push_back(*iter);
				iter_s = stack.end();
			}
			// 否则是操作符
			else
			{
				// 获取栈头的两个数
				string s_1 = *(iter_s-2);
				string s_2 = *(iter_s-1);
				stack.erase(iter_s-2, iter_s);
				// string转int
				int operand_1 = atoi(s_1.c_str());
				int operand_2 = atoi(s_2.c_str());
				int operand;
				if(*iter == "+")
				{
					operand = operand_1 + operand_2;
				}
				else if(*iter == "-")
				{
					operand = operand_1 - operand_2;
				}
				else if(*iter == "*")
				{
					operand = operand_1 * operand_2;
				}
				else if(*iter == "/")
				{
					operand = operand_1 / operand_2;
				}
				// int转string
				stringstream ss;
				string s_operand;
				ss << operand;
				ss >> s_operand;
				stack.push_back(s_operand);
				iter_s = stack.end();
			}
		}
		return atoi(stack.at(0).c_str());
	}
};
 
int main()
{
        // 测试
	Solution* s = new Solution();
	string array[] = {"2", "1", "+", "3", "*"};
	//string array[] = {"4", "13", "5", "/", "+"};
	vector<string> s_vec(array, array+5);
	cout << s->evalRPN(s_vec) << endl;
 
	return 0;
}
