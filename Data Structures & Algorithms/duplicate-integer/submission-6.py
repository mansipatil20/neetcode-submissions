class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:   # duplicate found early
                return True
            seen.add(num)
        return False
