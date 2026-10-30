class Solution:
    def trap(self, height: List[int]) -> int:
        trap_water = 0
        n= len(height) -1
        start, end = 0, n
        max_start = 0
        max_end = 0
        while start < end:
            if height[start] < height[end]:
                max_start= max(max_start,height[start])
                trap_water += max_start - height[start]
                start +=1
            else:
                max_end = max(max_end, height[end])
                trap_water += max_end - height[end]
                end -=1
        return trap_water
        