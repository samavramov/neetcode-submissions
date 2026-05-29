from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs: 
            arr = [0] * 26
            for c in s: 
                val = ord(c) - ord("a")
                arr[val] +=1
            tup = tuple(arr)
            hashmap[tup].append(s)
        print (hashmap)
        return list(hashmap.values())