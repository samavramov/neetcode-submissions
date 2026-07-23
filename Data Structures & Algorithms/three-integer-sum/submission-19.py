class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        hashset = set()
        i = 0
        for num in nums:
            j = i + 1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    temp = (nums[i], nums[j], nums[k])
                    if temp not in hashset:
                        output.append(temp)
                    hashset.add(temp)
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j+= 1
            i += 1
        return output



            


        