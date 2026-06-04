class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while l < r and r < len(prices): 
            if prices[r] - prices[l] > 0:
                maxP = max(maxP, prices[r] - prices[l])
            else: 
                l = r
            r +=1
        return maxP
                