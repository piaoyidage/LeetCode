/**
 * @author piaoyidage
 * @version 创建时间：2015-6
 *
 */ 

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) 
    {
        map<int, int> int_count;
        int i = 0;
        for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++, i++)
        {
            // 向map中插入当前元素和其索引，当前元素作为key,索引作为value
            pair<map<int, int>::iterator, bool> ret = int_count.insert(make_pair(*it, i));
            // 当下一次遇到key，判断当前索引和map中索引的差值，如果小于k，则找到，否则更新map中索引值
            if (!ret.second)
            {
                int count = i - ret.first->second;
                if (count <= k)
                {
                    return true;
                }
                ret.first->second = i;
            }
        }
        return false;
        
    }
};
