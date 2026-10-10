class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for stock_price in range(len(prices)):
            for i in range(stock_price+1, len(prices)):
                profit = prices[i] - prices[stock_price]
                if max_profit < profit:
                    max_profit = prices[i]-prices[stock_price]
        return max_profit
        