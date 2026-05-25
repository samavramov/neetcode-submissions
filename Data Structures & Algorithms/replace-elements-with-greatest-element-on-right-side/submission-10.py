class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, n in enumerate(arr):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                j = i+1
                suffix_max = max(arr[j:])
                arr[i] = suffix_max
        return arr
            