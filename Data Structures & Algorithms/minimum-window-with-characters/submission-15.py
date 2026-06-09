class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        window = {}
        for c in t: 
            target[c] = target.get(c,0)+1
        need = len(set(t))
        have = 0
        l = 0
        best = (0, float("inf"))
        for r, char in enumerate(s): 
            if char in target:  
                window[char] = window.get(char,0) + 1
                if window[char] == target[char]:
                    have += 1
            while have == need: 
                bestl, bestr = best
                if r-l < bestr - bestl: 
                    best = (l,r)
                left = s[l]
                if left in target: 
                    window[left] -= 1
                    if window[left] < target[left]:
                        have -= 1
                l+=1
        if best[1] == float("inf"):
            return ""           
        return s[best[0]:best[1]+1]


                

        




        