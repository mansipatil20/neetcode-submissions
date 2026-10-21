class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_ele = {}
        for i in nums:
            unique_ele[i] = unique_ele.get(i,0)+1
        sorted_desc = sorted(unique_ele.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_desc[:k]]
        