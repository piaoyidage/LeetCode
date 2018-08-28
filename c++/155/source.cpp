/**
 * @author piaoyidage
 * @version 创建时间：2014-11-07 19:58:21
 *
 */	


#include <iostream>
#include <stack>
 
using namespace std;
 
 
class MinStack
{
public:
	void push(int x) 
	{
		// 当x小于等于当前最小值时，x压入min栈
		if(min.empty() || min.top() >= x)
		{
			min.push(x);
		}
		my_stack.push(x);
	}
 
	void pop()
	{
		if(!my_stack.empty())
		{
			// 两个栈顶值相同时，min退栈
			if(my_stack.top() == min.top())
			{
				min.pop();
			}
			my_stack.pop();
		}
	}
 
	int top() 
	{
		if(!my_stack.empty())
		{
			return my_stack.top();
		}
	}
 
	int getMin() 
	{
		if(!min.empty())
		{
			return min.top();
		}
	}
private:
	// 存储栈中的元素
	stack<int> my_stack;
	// 栈顶是最小元素
	stack<int> min;
};
 
 
int main()
{
	// 测试
	MinStack *ms = new MinStack;
	ms->push(512);
	ms->push(1024);
	ms->push(1024);
	ms->push(512);
	ms->pop();
	cout << ms->getMin() << endl;
	ms->pop();
	cout << ms->getMin() << endl;
	ms->pop();
	cout << ms->getMin() << endl;
 
	return 0;
}
