class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char = list(s1)
        len_s1 = len(s1)
        for s in range(len(s2)):
            s_char = s2[s:s+len_s1]
            if sorted(s1_char) == sorted(s_char):
                return True
        
        return False
        