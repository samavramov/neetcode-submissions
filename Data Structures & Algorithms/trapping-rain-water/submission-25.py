class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = (len(height)-1)
        lmax = height[l]
        rmax = height[r]

        area = 0
        while l<r: 
            if lmax <= rmax: 
                l += 1
                area += max(lmax-height[l], 0)
                lmax = max(lmax, height[l])
            else:
                r-=1
                area += max(rmax-height[r], 0)
                rmax = max(rmax, height[r])
        return area



        

        