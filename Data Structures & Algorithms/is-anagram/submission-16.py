class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for i in s: 
            hashmap[i] += 1
        for i in t: 
            if hashmap[i] == 0:
                return False
            else: 
                hashmap[i] -= 1
        for i in s: 
            if hashmap[i] != 0: 
                return False
        return True