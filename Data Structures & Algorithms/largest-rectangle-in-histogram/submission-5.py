class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxarea = heights[0]
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                pindex = stack.pop()
                height = heights[pindex]
                if stack:
                    width = (i - stack[-1] - 1)
                else: 
                    width = i
                maxarea = max(maxarea, height*width)
            stack.append(i)
        return maxarea
