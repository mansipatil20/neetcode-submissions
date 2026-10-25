from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                pair_sum = nums[left] + nums[right]
                if pair_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif pair_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
