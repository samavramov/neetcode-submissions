import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        heap = [[0,k]]
        visited = set()
        t = 0
        while heap:
            w1, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = w1
            for v2, w2 in edges[node]:
                if v2 in visited:
                    continue
                distance = w1 + w2
                heapq.heappush(heap, (distance, v2))
        return t if len(visited)==n else -1



        
        