import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    returnlist = []
    for n in nums: 
        heapq.heappush(heap, -n)
    while heap:
        returnlist.append(-heapq.heappop(heap))
    return returnlist





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
