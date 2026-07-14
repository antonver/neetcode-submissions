class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs = self.calculate(nums)
        sufixs = self.calculate(nums[::-1])[::-1]
        res = []
        for i in range(len(nums)):
            res.append(prefixs[i] * sufixs[i])
        print(sufixs, prefixs)
        return res
    def calculate(self, nums: List[int]) -> List[int]:
        prefix = [1,]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        return prefix