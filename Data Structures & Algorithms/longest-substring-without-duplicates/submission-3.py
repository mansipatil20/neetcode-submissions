class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starting = 0
        max_len = 0
        seen = set()
        for ending in range(len(s)):
            while s[ending] in seen:
                seen.remove(s[starting])
                starting +=1
            seen.add(s[ending])
            max_len = max(max_len, ending - starting +1)

        return max_len
