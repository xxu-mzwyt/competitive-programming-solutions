# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidLine(line: List[str]) -> bool:
            line = [i for i in line if i != "."]
            return len(set(line)) == len(line)

        for row in board:
            if not isValidLine(row):
                return False

        rotated_board = list(zip(*board[::-1]))
        for col in rotated_board:
            if not isValidLine(col):
                return False

        subboxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subboxes.append(
                    board[i][j : j + 3]
                    + board[i + 1][j : j + 3]
                    + board[i + 2][j : j + 3]
                )
        for box in subboxes:
            if not isValidLine(box):
                return False

        return True
