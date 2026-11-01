from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter()
        required = len(count_t)   # number of unique chars needed
        formed = 0                # how many are satisfied
        left = 0
        sub_str = ""

        for right in range(len(s)):
            count_s[s[right]] += 1

            # check if this char just satisfied requirement
            if s[right] in count_t and count_s[s[right]] == count_t[s[right]]:
                formed += 1

            while formed == required:   # O(1) check instead of all(...)
                new_str = s[left:right+1]
                if not sub_str or len(new_str) < len(sub_str):
                    sub_str = new_str

                count_s[s[left]] -= 1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    formed -= 1
                left += 1

        return sub_str
