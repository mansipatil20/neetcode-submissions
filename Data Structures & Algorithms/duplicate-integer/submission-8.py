class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cn= set()
        for i in nums:
            if i in cn:
                return True
            else:
                cn.add(i)
        return False