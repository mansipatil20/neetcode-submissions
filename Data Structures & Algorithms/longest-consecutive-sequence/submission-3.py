class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxLen = 1
        tempLen = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] == 1:
                tempLen += 1
                maxLen = max(tempLen, maxLen)
            else:
                tempLen = 1
        return maxLen
        