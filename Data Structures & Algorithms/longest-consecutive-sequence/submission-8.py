class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        potentialstarts = defaultdict(set)
        maxlen = 0
        for num in hashmap: 
            pred = num-1
            if pred not in hashmap: 
                potentialstarts[num].add(num)
                nex = num+1
                while nex in hashmap:
                    potentialstarts[num].add(nex)
                    nex +=1
                if len(potentialstarts[num]) > maxlen:
                    maxlen = len(potentialstarts[num])
        return maxlen



        