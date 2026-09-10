from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcount = defaultdict(int)
        numslen = set(nums)
        heap = []
        for num in nums:
            freqcount[num] += 1
        for i, num in enumerate(numslen):
            heapq.heappush(heap, (- freqcount[num], num))
        retlist = []
        for i in range(k):
            val = heapq.heappop(heap)
            retlist.append(val[1])
        return retlist

        
        