class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subbox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                box = (r//3, c//3)
                if value in rows[r] or value in columns[c] or value in subbox[box]:
                    return False
                
                rows[r].add(value)
                columns[c].add(value)
                subbox[box].add(value)

        return True
