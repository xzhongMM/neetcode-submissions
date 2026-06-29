class Solution:
    def isValidNine(self, s: str) -> bool:
        cleaned = s.replace(".","")
        return len(cleaned) == len(set(cleaned))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = "".join(board[i])
            column = ""
            subbox = ""
            for j in range(9):
                column += board[j][i]
                subbox += board[(j//3)+(3*(i//3))][(j%3) + (3*(i%3))]
            if not (self.isValidNine(row) and self.isValidNine(column) and self.isValidNine(subbox)):
                return False
        return True

