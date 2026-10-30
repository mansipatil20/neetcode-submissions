from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right  # track the best feasible speed
        
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                result = mid        # update feasible answer
                right = mid - 1     # try smaller speeds
            else:
                left = mid + 1      # need faster speed
        
        return result
