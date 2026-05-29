class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxset = defaultdict(set)
        for row in board:
            seenrow = set()
            for value in row:
                if value == ".":
                    continue
                else:
                    if value in seenrow:
                        return False
                    
                    else:
                        seenrow.add(value)
        rows = len(board)
        cols = len(board[0])
        for column in range(cols):
            seencol = set()
            for row in range(rows):
                value = board[row][column]
                if value == ".":
                    continue
                else:
                    if value in seencol:
                        return False
                    else:
                        seencol.add(value)
        boxcount = 0
        for i, row in enumerate(board): 
            for j, value in enumerate(row):
                if value == ".":
                    continue
                else:
                    if 0 <= i <=2:
                        if 0 <= j <=2:
                            box = 0
                        elif 3 <= j <=5:
                            box = 1
                        else: 
                            box = 2
                    elif 3 <= i <=5:
                        if 0 <= j <=2:
                            box = 3
                        elif 3 <= j <=5:
                            box = 4
                        else: 
                            box = 5
                    else:
                        if 0 <= j <=2:
                            box = 6
                        elif 3 <= j <=5:
                            box = 7
                        else: 
                            box = 8
                if value in boxset[box]:
                    return False
                else:
                    boxset[box].add(value)
        return True
        