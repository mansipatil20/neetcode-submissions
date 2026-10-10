class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if( target - nums[i] == nums[j]):
                    if(i!=j):
                        result.extend([i, j])
                        return result