class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in reversed(nums):
                vap = len(nums)-1 - list(reversed(nums)).index(diff)
                if(i != vap):
                    return [i, vap]