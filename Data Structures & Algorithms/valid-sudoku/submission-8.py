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
            
            print(f'row {i} column {j}: {row} | {column} | {subbox}')
            print(f'{self.isValidNine(row)} | {self.isValidNine(column)} | {self.isValidNine(subbox)}')
            if not (self.isValidNine(row) and self.isValidNine(column) and self.isValidNine(subbox)):
                return False
        return True


#00,01,02   03,04,05    06,07,08
#10,11,12   13,14,15    16,17,18
#20,21,22   23,24,25    26,27,28

#30,31,32
#40,41,42
#50,51,52

#30 31 32 33 34 35 36 37 38
#30 31 32 40 41 42 50 51 52

#00 01 02 03 04 05 06 07 08         
#00 01 02 10 11 12 20 21 22

#10 11 12 13 14 15 16 17 18         [(j//3)+(3*(i//3))]   [(j%3) + (3*(i//3))]
#03 04 05 13 14 15 23 24 25

#20 21 22 23 24 25 26 27 28
#06 07 08 16 17 18 26 27 28