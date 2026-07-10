class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        for i in s:
            if hash_s.get(i):
                hash_s[i] += 1
                continue
            hash_s[i] = 1
        for i in t:
            if hash_t.get(i):
                hash_t[i] += 1
                continue
            hash_t[i] = 1
        return hash_s == hash_t
