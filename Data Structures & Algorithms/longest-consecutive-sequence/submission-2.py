class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        max_ = 1
        cur = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            if cur > max_:
                max_ = cur
        return max_