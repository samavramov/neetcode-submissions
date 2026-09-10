class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tripleset = set()
        res = []
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum == 0:
                    tripleset.add((n, nums[l], nums[r]))
                    l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        for tup in tripleset:
            templist = []
            for t in tup:
                templist.append(t)
            res.append(templist)
        return res


        