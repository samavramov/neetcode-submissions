class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s: 
            if c.isalnum():
                chars.append(c)
        string = ("".join(chars)).lower()
        l = 0
        r = len(string)-1
        print(string)
        while l<r:
            if string[l] == string [r]:
                l += 1
                r -= 1
            else: 
                return False
        return True
        