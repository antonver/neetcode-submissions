class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        n = 0
        for i in nums:
            h[i] = n
            n += 1
        k = 0
        for i in nums:
            res = h.get(target - i)
            if res is not None and res != k:
                return [min(k, res), max(k, res)]
            k += 1