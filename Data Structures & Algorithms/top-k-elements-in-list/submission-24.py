class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcount = defaultdict(int)
        result = []
        for num in nums: 
            freqcount[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in freqcount.items():
            buckets[freq].append(val)
        print(buckets)
        kcount = 0
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                continue





        

        