class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        left = 0
        result = 0

        for right in range(len(s)):
            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # If window size - max_count > k, shrink from left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update result with valid window size
            result = max(result, right - left + 1)

        return result
