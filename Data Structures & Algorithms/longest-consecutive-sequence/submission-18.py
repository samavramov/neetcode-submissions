class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxn = 0
        for num in nums: 
            pred = num-1
            if pred not in nums: 
                tempmax = 1
                while num+1 in nums:
                    tempmax += 1
                    num += 1
                maxn = max(tempmax, maxn)
        return maxn

        