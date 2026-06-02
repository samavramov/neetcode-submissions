class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        for num in nums: 
            prev = num-1
            if prev in nums: 
                continue
            tempcount = 1
            while num+1 in nums:
                tempcount += 1
                num +=1
            maxcount = max(tempcount, maxcount)
        return maxcount


        