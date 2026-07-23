class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        outputlist = []
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                outputlist.append(l+1)
                outputlist.append(r+1)
                return outputlist
            elif sum < target:
                l += 1
            elif sum > target :
                r -= 1
        