class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s, char_t=[char for char in s], [char for char in t]
        char_s.sort()
        char_t.sort()
        return True if(char_s == char_t) else False     