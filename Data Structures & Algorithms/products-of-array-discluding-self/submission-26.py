class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        oldn = 0
        for i, n in enumerate(nums): 
            if i == 0:
                oldn = n
                continue
            prefix *= oldn
            res[i] = prefix
            oldn = n
        suffix = 1
        oldn = 0
        for i, n in enumerate(reversed(nums)):
            if i == 0:
                oldn = n
                continue
            suffix *= oldn
            res[len(nums)-1-i] *= suffix
            oldn = n
        return res




        