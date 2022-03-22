var twoSum = function (nums, target) {
	const map = {};
	for (let i = 0; i < nums.length; i++) {
		map[target - nums[i]] = i;
		if (nums[i + 1] in map) return [map[nums[i + 1]], i + 1];
	}
};
