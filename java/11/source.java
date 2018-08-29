/**
 * @author piaoyidage
 * @version 创建时间：2015-4
 *
 */ 

public class Solution {
 public int maxArea(int[] height)
    {
        // 初始化
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        // 循环
        while (right > left)
        {
            // 当前计算的值
            int current = (right - left) * min(height[left], height[right]);
            max = current > max ? current : max;
            
            // 当右边线段长，左边坐标点右移
            if (height[right] > height[left])
            {
                int k = left;
                while (k < right && height[k] <= height[left])
                {
                    k++;
                }
                left = k;
            }
            else
            {
                int k = right;
                while (k > left && height[k] <= height[right])
                {
                    k--;
                }
                right = k;
            }
        }

        return max;
    }

    public int min(int a, int b)
    {
        int minValue = a;
        minValue = a > b ? b : a;
        return minValue;
    }

}