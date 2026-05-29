class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()
        for i, num in enumerate(nums): 
            complement = target - num
            if complement in hashset:
                return [min(i, nums.index(complement)), max(i, nums.index(complement))]
            else: 
                hashset.add(num)
        
