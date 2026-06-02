class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        hashset = set(nums)
        for num in hashset: 
            if num-1 in hashset: 
                continue
            tempcount = 1
            while num+1 in hashset:
                tempcount +=1
                num +=1
            maxcount = max(tempcount, maxcount)
        return maxcount


        