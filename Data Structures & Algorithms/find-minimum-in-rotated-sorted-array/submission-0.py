class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ele = max(nums)
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end) //2
            # min_ele=min(min_ele,nums[mid])
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        return nums[start]
        