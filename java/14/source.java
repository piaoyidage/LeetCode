/**
 * @author piaoyidage
 * @version 创建时间：2015-06-09
 *
 */ 


public class Solution {
   public String longestCommonPrefix(String[] strs)
    {
        String str = "";
        if (strs == null)
        {
            return str;
        }
        int count = 0;
        String cur = null;
        // 取首个字符
        if ((strs.length > 0) && (strs[0].length() > count))
            cur = strs[0].substring(count, count+1);
        else
            return str;
        // 逐个比较
        while (true)
        {
            for (String s : strs)
            {
                if ( (s.length() <= count) || (!s.substring(count, count+1).equals(cur)) )
                {
                    return str;
                }
            }
            str += cur;
            count++;
            if ((strs[0].length() > count))
                cur = strs[0].substring(count, count+1);
            else
                return str;
        }
    }
}
