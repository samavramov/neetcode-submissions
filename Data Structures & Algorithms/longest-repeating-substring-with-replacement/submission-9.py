class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        r = 0
        hashmap = defaultdict(int)
        for r in range(len(s)):
            hashmap[s[r]] +=1
            maxf = max(hashmap.values())
            while (r-l+1) - maxf > k:
                hashmap[s[l]] -= 1
                l +=1
                maxf = max(hashmap.values())
            longest = max(longest, r-l+1)
        return longest


                    
                 

                    

            
        