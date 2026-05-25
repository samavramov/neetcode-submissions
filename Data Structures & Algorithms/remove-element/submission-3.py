class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, n in enumerate(nums): 
            if n != val:
                count += 1
        for i in range(len(nums)-count):
            nums.remove(val)
        return count
