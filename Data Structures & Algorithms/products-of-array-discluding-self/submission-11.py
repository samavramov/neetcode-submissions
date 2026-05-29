class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = []
        total = 1
        result = [1] * len(nums)
        for num in nums:
            total *= num
            prefix.append(total)
        total = 1
        prefix.pop()
        for num in reversed(nums):
            total *= num
            suffix.append(total)
        suffix = list(reversed(suffix))
        suffix.pop(0)
        suffix.append(1)
        for i, n in enumerate(nums):
            result[i] *= suffix[i] * prefix[i]
        return result



        
        