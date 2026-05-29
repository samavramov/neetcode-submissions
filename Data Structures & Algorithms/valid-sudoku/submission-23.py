class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box = (i // 3, j // 3)
                if val in cols[i] or val in rows[j] or val in boxes[box]:
                    return False         
                cols[i].add(val)
                rows[j].add(val)
                boxes[box].add(val)
        return True
                