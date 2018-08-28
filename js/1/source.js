/*
* @Author: maoying.hu
* @Date:   2015-11

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // 判断是否是数组
	if (!(nums instanceof Array)) {
		return;
	}
	// 存放索引
	var indices = [];
    for (var i = 0; i < nums.length; i++) {
    	for (var j = i+1; j < nums.length; j++) {
    		var sum = nums[i] + nums[j];
    		if (sum === target) {
    			indices.push(i+1, j+1);
    		}
    	}
    }
    // 自定义升序 排序（注意：js默认转换成string，按照ascii排序）
    function ascendSort(a, b) {
        return a - b;
    }
    return indices.sort(ascendSort);
};