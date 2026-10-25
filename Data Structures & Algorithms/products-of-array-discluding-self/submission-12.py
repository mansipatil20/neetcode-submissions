class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prod_arr = [1]* n
        temp_prod = 1
        for i in range(n):
            
            prod_arr[i] *= temp_prod
            temp_prod *= nums[i]
        back_prod = 1
        for j in range(n-1,-1,-1):
            
            prod_arr[j] *= back_prod
            back_prod *= nums[j]

        return prod_arr