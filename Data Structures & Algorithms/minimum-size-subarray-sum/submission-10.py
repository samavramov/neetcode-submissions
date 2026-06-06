class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minwindow = 0
        count = 0
        l = 0
        r = 0
        for _ in nums:
            count += nums[r]
            while count>=target:
                distance = r-l+1
                if minwindow == 0:
                    minwindow = distance
                else: 
                    minwindow = min(minwindow, distance)
                count -= nums[l]
                l +=1
            r +=1
        return minwindow
        