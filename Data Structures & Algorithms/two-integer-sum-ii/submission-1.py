class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ele in numbers:
            num_find=target-ele
            if num_find in numbers and ele!=num_find:
                return [numbers.index(ele)+1,numbers.index(num_find)+1]
        return -1
        