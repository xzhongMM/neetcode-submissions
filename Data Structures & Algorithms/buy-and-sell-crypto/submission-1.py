class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        for p in prices:
            buy = min(buy, p)
            profit = p - buy
            result = max(result, profit)

        return result