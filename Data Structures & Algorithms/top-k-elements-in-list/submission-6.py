class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # unique_ele = {}
        # for i in nums:
        #     unique_ele[i] = unique_ele.get(i,0)+1
        # sorted_desc = sorted(unique_ele.items(), key=lambda item: item[1], reverse=True)
        
        # return [item[0] for item in sorted_desc[:k]]
        seen = Counter(nums)
        ordered = sorted(seen.items(), key= lambda pair:pair[1], reverse=True)
        result=[]

        # for i in range(k):
        #     result.append(ordered[i][0])

        return [result[0] for result in ordered[:k]]