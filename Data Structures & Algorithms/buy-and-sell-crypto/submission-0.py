class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currSum = 0
        maxSum = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                currSum = max(currSum, prices[j] - prices[i])
                maxSum = max(currSum, maxSum)

        return maxSum


        