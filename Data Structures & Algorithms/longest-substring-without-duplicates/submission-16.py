class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxL = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            r+=1
            maxL = max(r-l, maxL)
        return maxL
