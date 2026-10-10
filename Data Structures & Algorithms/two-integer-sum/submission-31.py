class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        new_list = list(reversed(nums))
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in new_list:
                vap = len(nums)-1 - new_list.index(diff)
                if(i != vap):
                    return [i, vap]