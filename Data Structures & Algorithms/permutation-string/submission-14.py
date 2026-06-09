class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = defaultdict(int)
        window = defaultdict(int)
        for c in s1: 
            target[c] +=1
        l = 0
        for r, c in enumerate(s2):
            if target[c] == 0:
                window.clear()
                l = r +1
                continue
            window[c] +=1
            while window[c] > target[c]:
                window[s2[l]] -= 1
                l+=1
            if r-l+1 == len(s1):
                return True
        return False
        

        