class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = float('inf')
        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = min(prices[i], minBuy)
            else:
                res = max(res, prices[i] - minBuy)
        
        return res