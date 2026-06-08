class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        l = 1
        for r, num in enumerate(nums):
            if r == 0:
                seen[num] += 1
                continue
            if seen[num] < 2:
                seen[num] += 1
                nums[l] = nums[r]
                l +=1
        return l
        