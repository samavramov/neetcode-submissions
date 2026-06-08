class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r, num in enumerate(nums):
            if r == 0:
                continue
            if num != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l