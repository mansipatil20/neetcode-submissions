class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            char_s=[]
            for i in s:
                char_s.append(i)
            char_t=[]
            for i in t:
                char_t.append(i)
            set_s = set(char_s)
            set_t = set(char_t)
            count_s = []
            count_t = []
            if(set_s == set_t):
                for i in set_s:
                    count_s.append(s.count(i))
                    count_t.append(t.count(i))
                    if count_s == count_t:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
        