class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        potentialstarts = defaultdict(set)
        for num in nums: 
            pred = num-1
            if pred not in hashmap: 
                potentialstarts[num].add(num)
                nex = num+1
                while nex in hashmap:
                    potentialstarts[num].add(nex)
                    nex +=1
        maxlen = 0
        for val in potentialstarts.values():
            if len(val) > maxlen:
                maxlen = len(val)
        return maxlen



        