class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0,len(nums)-1):
            for j in range(1, len(nums)):
                if( target - nums[i] == nums[j]):
                    if(i!=j):
                        result.extend([i, j])
                        return result
        