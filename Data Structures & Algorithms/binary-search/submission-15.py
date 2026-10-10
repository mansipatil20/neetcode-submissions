class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            number_pos=(high+low)//2
            if nums[number_pos] == target:
                return number_pos
            elif nums[number_pos] > target:
                    high=number_pos-1
            else:
                    low= number_pos+1
        return -1