class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!= len(t)):
            return False
        mapForStringS = {}
        mapForStringT = {}
        for i in range(len(s)):
            mapForStringS[s[i]] = 1 + mapForStringS.get(s[i], 0)
            mapForStringT[t[i]] = 1 + mapForStringT.get(t[i], 0)
        return mapForStringS == mapForStringT
            