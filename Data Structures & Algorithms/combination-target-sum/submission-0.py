from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, curr_comb, curr_sum):
            # Found a valid combination
            if curr_sum == target:
                result.append(curr_comb[:])
                return

            # Invalid path
            if curr_sum > target or index == len(nums):
                return

            # Include nums[index]
            curr_comb.append(nums[index])
            dfs(index, curr_comb, curr_sum + nums[index])  # reuse same number
            curr_comb.pop()

            # Skip nums[index]
            dfs(index + 1, curr_comb, curr_sum)

        dfs(0, [], 0)
        return result