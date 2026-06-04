class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        windowsum = 0
        threshold *= k
        for i,c in enumerate(arr):
            windowsum += c
            if i >=k:
                windowsum -= arr[i-k]
            if (windowsum)>= threshold and i >= k-1:
                count +=1        
        return count


        