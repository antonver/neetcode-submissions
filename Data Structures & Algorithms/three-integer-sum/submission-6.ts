class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
		let res: number[][] = [];
		nums.sort((a,b)=> a-b);
		for (let i = 0; i < nums.length - 2; ++i){
			if (i > 0 && nums[i] == nums[i-1]){
				continue
			}
			let a = i + 1;
			let b = nums.length - 1;
			while (a < b){
				if (nums[i] + nums[b] + nums[a] < 0){
					++a
				} else if (nums[i] + nums[b] + nums[a] > 0){
					--b
				}else{
					res.push([nums[i],nums[a], nums[b]])
				++a
				--b
				while (a < b && nums[a] == nums[a-1]){
					++a
				}
				while (a < b && nums[b] == nums[b + 1]){
					--b
				}}
			}
		}
		return res;
	}
}
