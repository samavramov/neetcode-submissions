class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxsize = 1
        l = 0
        r = 1
        currsign = ""
        while r < len(arr):
            if arr[r-1] < arr[r] and currsign != "<":
                currsign = "<"
                r+=1
                maxsize = max(maxsize, r-l)
            elif arr[r-1] > arr[r] and currsign != ">":
                currsign = ">"
                r +=1
                maxsize = max(maxsize, r-l)
            else: 
                if arr[r] == arr[r-1]:
                    r +=1
                l = r-1
                currsign = ""
        return maxsize



        