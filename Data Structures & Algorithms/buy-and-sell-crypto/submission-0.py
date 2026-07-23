class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        for p in range(1, len(prices)):
            buy = min(buy, prices[p])
            result = max(result, prices[p]-buy)

        return result