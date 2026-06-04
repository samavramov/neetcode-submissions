class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while l < r and r < len(prices): 
            value = prices[r] - prices[l]
            if value > 0:
                maxP = max(maxP, value)
            else: 
                l = r
            r +=1
        return maxP
                