class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            char_s=[]
            for i in s:
                char_s.append(i)
            char_t=[]
            for i in t:
                char_t.append(i)
            char_s.sort()
            char_t.sort()
            count_s = []
            count_t = []
            if(char_s == char_t):
                return True
            else:
                return False
        else:
            return False
        