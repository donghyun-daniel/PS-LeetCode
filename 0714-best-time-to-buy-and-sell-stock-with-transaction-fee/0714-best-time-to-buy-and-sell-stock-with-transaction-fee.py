class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        
        for idx in range(1, n):
            buy[idx] = max(buy[idx-1], sell[idx-1] - prices[idx])
            sell[idx] = max(sell[idx-1], buy[idx-1] + prices[idx] - fee)
        
        return sell[-1]