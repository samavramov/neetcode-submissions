class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i, number in enumerate(nums): 
            if number in hashset:
                return True
            else: 
                hashset.add(number)
                if i >= k: 
                    hashset.remove(nums[i-k])
        return False

        