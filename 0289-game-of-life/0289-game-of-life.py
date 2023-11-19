class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        new_board = deepcopy(board)

        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, 1], [1, 1], [1, 0],
            [1, -1], [0, -1]
        ]

        for r in range(m):
            for c in range(n):
                count = 0
                for x, y in directions:
                    new_r, new_c = r + x, c + y
                    if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == 1:
                        count += 1

                if board[r][c] == 1 and (count < 2 or count > 3):
                    new_board[r][c] = 0
                elif board[r][c] == 0 and count == 3:
                    new_board[r][c] = 1

        for r in range(m):
            for c in range(n):
                board[r][c] = new_board[r][c]