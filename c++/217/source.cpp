/**
 * @author piaoyidage
 * @version 创建时间：2015-6
 *
 */	

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) 
    {
        set<int> s;
		for (vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
		{
			s.insert(*i);
		}

		if (s.size() != nums.size())
		{
			return true;
		}

		return false;
    }
};