class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for i in s:
            s_hash[i] = s_hash.get(i,0)+1
        for i in t:
            t_hash[i] = t_hash.get(i,0)+1
        
        return s_hash == t_hash
        