class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        sorted(count.items())
        output = []
        for i in range (0,k):
            most = max(count, key=count.get)
            output.append(most)
            count.pop(most)
        return output
    