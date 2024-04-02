# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count_neighbors(i, j, m, n):
            neighbors_n = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            count = 0
            for ni, nj in neighbors_n:
                neighbor_i = i + ni
                neighbor_j = j + nj
                if neighbor_i < 0 or neighbor_j < 0:
                    continue
                if neighbor_i >= m or neighbor_j >= n:
                    continue
                if board[neighbor_i][neighbor_j] == 1:
                    count += 1
            return count

        m = len(board)
        n = len(board[0])

        neighbors = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                neighbors[i][j] = count_neighbors(i, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if neighbors[i][j] < 2:
                        board[i][j] = 0
                    if neighbors[i][j] > 3:
                        board[i][j] = 0
                else:
                    if neighbors[i][j] == 3:
                        board[i][j] = 1
