class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        base = len(heights)-1
        maxA = 0
        while l < r:
            currA = (min(heights[r], heights[l])) * base
            if currA >= maxA:
                maxA = currA
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            base -= 1
        return maxA 

        