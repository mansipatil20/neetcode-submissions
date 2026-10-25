class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        s1_count = Counter(s1)
        for s in range(len(s2)-len(s1)+1):
            s_char = s2[s:s+len_s1]
            if Counter(s_char) == s1_count:
                return True
        
        return False
        