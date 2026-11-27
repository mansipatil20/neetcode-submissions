class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrcking(index,curr_comb,current_total):
            if current_total == target:
                result.append(curr_comb[:])
                return
            if current_total > target or index == len(nums):
                return

            curr_comb.append(nums[index])
            backtrcking(index, curr_comb, current_total + nums[index])
            curr_comb.pop()
            backtrcking(index + 1, curr_comb, current_total)
            # add
            # action
            # remove
        backtrcking(0,[],0)
        return result
        