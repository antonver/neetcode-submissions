class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
		let pivot = 0;
		let a = 0;
		let b = nums.length - 1;
		while (a <= b){
			pivot = a + (b - a) // 2;
			if (nums[pivot] > target){
				b = pivot - 1;
			} else if (nums[pivot] < target){
				a = pivot + 1;
			} else{
				return pivot;
			}
		}
		return -1;
	}

}
