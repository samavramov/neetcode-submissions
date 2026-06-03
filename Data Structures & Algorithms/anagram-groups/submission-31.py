class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs: 
            bitarr = [0] * 26
            for c in s: 
                num = ord((c))-ord("a")
                bitarr[num] += 1 
            tuparr = tuple(bitarr)
            hashmap[tuparr].append(s)
        return [val for val in hashmap.values()]           


        