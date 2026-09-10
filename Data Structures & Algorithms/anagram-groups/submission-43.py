from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            charcount = [0]*26
            for c in word: 
                charcount[ord(c) - ord("a")] += 1
            hashmap[tuple(charcount)].append(word)
        return list(hashmap.values())


        