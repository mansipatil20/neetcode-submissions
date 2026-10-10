class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            expected_num = target - num
            if expected_num in seen:
                return [seen[expected_num], i]
            seen[num] = i
        