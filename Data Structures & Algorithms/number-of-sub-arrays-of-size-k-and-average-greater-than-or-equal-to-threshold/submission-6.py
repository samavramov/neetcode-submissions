class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        windowsum = 0
        for i,c in enumerate(arr):
            windowsum += c
            if i >=k:
                windowsum -= arr[i-k]
            if (windowsum)/k >= threshold and i >= k-1:
                count +=1
                print(windowsum)
            
        return count


        