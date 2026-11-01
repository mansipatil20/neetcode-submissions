class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap= []
        result = []
        #build initial heap
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        result.append(-heap[0][0])
        
        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))

            while heap[0][1]<= i- k:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
        
        # brute force approach
        # max_list = []
        # max_ele = 0
        # start = 0
        # end = k
        # while end <= len(nums):
        #     sub_arr = nums[start:end]
        #     max_list.append(max(sub_arr))
        #     start +=1
        #     end +=1

        # return max_list