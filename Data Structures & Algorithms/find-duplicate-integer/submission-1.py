class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup_list = set()
        for i in nums:
            if i in dup_list:
               return i
            else:
                dup_list.add(i)