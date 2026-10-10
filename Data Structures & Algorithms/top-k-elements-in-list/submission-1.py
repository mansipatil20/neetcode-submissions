class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_num = {}
        for num in nums:
            if num in list_num.keys():
                list_num[num] += 1
            else:
                list_num[num] = 1

        sorted_dict=sorted(list_num.items(), key=lambda x : x[1], reverse = True)
        print(sorted_dict)
        list_k = []
        for i in range(k):
            list_k.append(sorted_dict[i][0])

        return list_k