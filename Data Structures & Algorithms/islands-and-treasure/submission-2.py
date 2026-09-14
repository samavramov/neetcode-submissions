from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i-1 >= 0 and i-1 < len(grid):
                    if grid [i-1][j] == 2147483647:
                        grid[i-1][j] = grid[i][j]+1
                        queue.append((i-1,j))
                if i+1 >= 0 and i+1 < len(grid):
                    if grid [i+1][j] == 2147483647:
                        grid[i+1][j] = grid[i][j]+1
                        queue.append((i+1,j))
                if j-1 >= 0 and j-1 < len(grid[0]):
                    if grid [i][j-1] == 2147483647:
                        grid[i][j-1] = grid[i][j]+1
                        queue.append((i,j-1))
                if j+1 >= 0 and j+1 < len(grid[0]):
                    if grid [i][j+1] == 2147483647:
                        grid[i][j+1] = grid[i][j]+1
                        queue.append((i,j+1))
        
                



            


        

            

        