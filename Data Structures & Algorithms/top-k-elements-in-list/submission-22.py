class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcount = defaultdict(int)
 
        for num in nums:
            freqcount[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in freqcount.items():
            buckets[freq].append(val)
        print(buckets)
        kcount = 0
        result = []


        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
