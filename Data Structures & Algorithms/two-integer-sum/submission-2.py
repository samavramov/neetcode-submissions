class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = {}
        for a,b in enumerate(nums):
            targ = target - b
            if(targ in diffmap):
                return [diffmap[targ], a]
            else: 
                diffmap[b] = a


            
                   