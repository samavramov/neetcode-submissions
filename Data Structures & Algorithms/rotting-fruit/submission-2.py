from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0,0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                orange = grid[i][j]
                if orange == 0:
                    continue
                elif orange == 1:
                    fresh += 1
                else:
                    queue.append((i, j))
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i-1 >= 0 and i-1 < len(grid):
                    if grid[i-1][j] == 1:
                        grid[i-1][j] = 2
                        queue.append((i-1, j))
                        fresh -= 1
                if i+1 >= 0 and i+1 < len(grid):
                    if grid[i+1][j] == 1:
                        grid[i+1][j] = 2
                        queue.append((i+1, j))
                        fresh -= 1
                if j-1 >= 0 and j-1 < len(grid[0]):
                    if grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        queue.append((i, j-1))
                        fresh -= 1
                if j+1 >= 0 and j+1 < len(grid[0]):
                    if grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        queue.append((i, j+1))
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else: 
            return -1
                
                    

                    


        