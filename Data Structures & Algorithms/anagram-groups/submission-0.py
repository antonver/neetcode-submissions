class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = [[0] * 26 for i in strs]
        h_ = dict()
        for i in range(len(strs)):
            for j in strs[i]:
                l[i][ord(j)-ord("a")] += 1
            l[i] = tuple(l[i])
            if h_.get(l[i]):
                h_[l[i]] += [strs[i]]
                continue
            h_[l[i]] = [strs[i]]
        return [v for v in h_.values()]
