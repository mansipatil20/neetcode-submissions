class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_ele = {}
        for i in nums:
            if i in unique_ele:
                unique_ele[i] = unique_ele[i]+1
            else:
                unique_ele[i] = 1
        sorted_desc = sorted(unique_ele.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_desc[:k]]
        