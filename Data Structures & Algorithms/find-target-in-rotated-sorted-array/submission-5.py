class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        minindex = right
        if nums[minindex] <= target <= nums[len(nums)-1]:
            left = minindex
            right = len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    return mid
            return -1
        else:
            left = 0
            right = minindex - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    return mid
            return -1



                
        