from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = (9, 9)
        board_T = board.copy()
        board_T = list(map(list, zip(*board_T)))

        board_square = []
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                board_square.append(board[row][col:col + 3] + board[row + 1][col:col + 3] + board[row + 2][col:col + 3])

        for line in range(rows):
            for digit in range(1, 10):
                if board[line].count(str(digit)) > 1 or board_T[line].count(str(digit)) > 1 or board_square[line].count(str(digit)) > 1:
                    return False
        return True

# Better solution
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != '.':
                    res += [(col,j),(i,col),(i//3,j//3,col)]
        
        return len(res) == len(set(res))
"""
