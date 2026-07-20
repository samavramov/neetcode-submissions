class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nummap = defaultdict(list)
        for word in strs: 
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord("a")] += 1
            key = tuple(freq)
            nummap[key].append(word)
        return list(nummap.values())
            



        