/**
 * @author piaoyidage
 * @version 创建时间：2015-06-09
 *
 */	

class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) 
	{
		vector<vector<int>> vvi;
		if (nums.size() < 3)
            return vvi;
		// 先排序
		sort(nums.begin(), nums.end());
		int first, second, third;
		vector<int> previous, cur;
		for(vector<int>::iterator i = nums.begin(); i != nums.end(); i++)
		{
			if ((*i) == *(i+1))
			{
				first = *i;
				second = *(i+1);
				third = 0 - first - second;
				// 如果第三个数小于第二个数，跳出循环
				if (third < second)
				{
					break;
				}
				if (find(i+2, nums.end(), third) != nums.end())
				{
					// 比较当前和最后添加到vvi中vector中的值是否一样
					if(vvi.empty())
					{
						cur.push_back(first);
						cur.push_back(second);
						cur.push_back(third);
						previous = cur;
						vvi.push_back(cur);
						vector <int>().swap(cur); 
					}
					else
					{
						if((previous[0] == first) && (previous[1] == second))
						{
							continue;
						}
						else
						{
							cur.push_back(first);
							cur.push_back(second);
							cur.push_back(third);
							previous = cur;
							vvi.push_back(cur);
							vector <int>().swap(cur); 
						}
					}
				}
				continue;
			}
			first = *i;
			// 当第一个数大于0，返回
			if (first > 0)
			{
				return vvi;
			}
			for(vector<int>::iterator j = i+1; j != nums.end(); j++)
			{
				second = *j;
				third = 0 - first - second;
				// 如果第三个数小于第二个数，跳出循环
				if (third < second)
				{
					break;
				}
				if (find(j+1, nums.end(), third) != nums.end())
				{
					// 比较当前和最后添加到vvi中vector中的值是否一样
					if(vvi.empty())
					{
						cur.push_back(first);
						cur.push_back(second);
						cur.push_back(third);
						previous = cur;
						vvi.push_back(cur);
						vector <int>().swap(cur); 
					}
					else
					{
						if((previous[0] == first) && (previous[1] == second))
						{
							continue;
						}
						else
						{
							cur.push_back(first);
							cur.push_back(second);
							cur.push_back(third);
							previous = cur;
							vvi.push_back(cur);
							vector <int>().swap(cur); 
						}
					}
				}
			}
		}
		return vvi;
	}
};
