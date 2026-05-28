
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for l in s: 
                letterpos = ord(l) - ord("a")
                arr[letterpos] +=1
            st = tuple(arr)
            output[st].append(s)
        return list(output.values())

            