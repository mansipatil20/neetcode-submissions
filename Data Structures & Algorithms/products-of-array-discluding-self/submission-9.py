class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = math.prod(nums)
        product_list = [1] * len(nums)
        pre_fix=1
        for i in range(len(nums)):
            product_list[i] =  pre_fix
            pre_fix *= nums[i] 
        post_fix=1
        for i in range(len(nums)-1,-1,-1):
            product_list[i] *= post_fix
            post_fix *= nums[i]
        return product_list
        