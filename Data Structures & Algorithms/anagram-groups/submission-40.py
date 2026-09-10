from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            charcount = [0]*26
            for c in word: 
                num = ord(c) - ord("a")
                charcount[num] += 1
            chartup = tuple(charcount)
            hashmap[chartup].append(word)
        return list(hashmap.values())


        