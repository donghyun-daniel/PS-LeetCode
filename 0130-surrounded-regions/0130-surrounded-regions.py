class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = []
        (row_size, col_size) = (len(board), len(board[0]))
        if not (row_size or col_size):
            return

        for row in range(row_size):
            for col in range(col_size):
                if (row == 0 or col == 0 or row == row_size - 1 or col == col_size - 1) \
                    and board[row][col] == "O":
                    q.append((row, col))

        while q:
            (r, c) = q.pop()
            board[r][c] = "#"
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for (dir_r, dir_c) in dirs:
                new_r = r + dir_r
                new_c = c + dir_c
                if 0 <= new_r < row_size and 0 <= new_c < col_size and board[new_r][new_c] == "O":
                    q.append((new_r, new_c))

        convert = {"O": "X", "#": "O", "X": "X"}
        for row in range(row_size):
            for col in range(col_size):
                board[row][col] = convert[board[row][col]]