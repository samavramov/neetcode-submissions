class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        windowsum = 0
        threshold *= k
        for i,c in enumerate(arr):
            windowsum += c
            if i >= k-1:
                count += windowsum>= threshold
                windowsum -= arr[i-k+1]        
        return count


        