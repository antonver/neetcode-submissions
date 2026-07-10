class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = dict()
        t = dict()
        for i in nums:
            if h.get(i):
                h[i] += 1
                continue
            h[i] = 1
        for ke,v in h.items():
            if t.get(v):
                t[v] += [ke]
                continue
            t[v] = [ke]
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) == k:
                return res
            if t.get(i):
                res += t[i]
