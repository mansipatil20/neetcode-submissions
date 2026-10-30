from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space: min speed = 1, max speed = max pile
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            # Calculate total hours needed at speed mid
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                result = mid   # feasible, try smaller k
                right = mid - 1
            else:
                left = mid + 1 # too slow, need faster k
        
        return result
