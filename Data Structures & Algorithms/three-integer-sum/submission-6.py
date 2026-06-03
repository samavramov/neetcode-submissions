class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, n in enumerate(nums): 
            l = i+1
            r = len(nums)-1
            while l < r: 
                sum = n+nums[l]+nums[r]
                if sum < 0: 
                    l +=1
                    continue
                elif sum > 0:
                    r -= 1
                    continue
                else:
                    lis = [n, nums[l], nums[r]]
                    if lis not in output: 
                        output.append(lis)
                    l += 1
                    r -= 1
        return output


        