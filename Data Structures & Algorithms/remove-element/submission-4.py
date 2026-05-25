class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        length = len(nums)
        while pos < length:
            if nums[pos] == val:
                nums[pos] = nums[length-1]
                length -= 1
            else: 
                pos+=1
        return pos