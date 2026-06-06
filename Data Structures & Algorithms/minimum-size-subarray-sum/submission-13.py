class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minwindow = 0
        count = 0
        l = 0
        r = 0
        for r, _ in enumerate(nums):
            count += nums[r]
            while count>=target:
                distance = r-l+1
                minwindow = distance if minwindow == 0 else min(minwindow, distance)
                count -= nums[l]
                l +=1
        return minwindow
        