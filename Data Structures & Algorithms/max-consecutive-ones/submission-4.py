class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        tempcount = 0
        for n in nums: 
            if n == 1: 
                tempcount+=1
                if tempcount > maxcount: 
                    maxcount = tempcount
            elif n == 0:
                tempcount = 0
        return maxcount
        