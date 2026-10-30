class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        temp_day = [0] * n
        for i,temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_in = stack.pop()
                temp_day[prev_in] = i - prev_in
            stack.append(i)

        return temp_day
        