class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxL = 0
        l = 0
        r = 0
        if len(s) == 1:
            return 1
        else:
            while r < len(s):
                while s[r] in window:
                    maxL = max(r-l, maxL)
                    window.remove(s[l])
                    l+=1
                window.add(s[r])
                r+=1
                print(window)
            maxL = max(r-l, maxL)
            return maxL
