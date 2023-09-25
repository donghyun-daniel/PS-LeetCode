class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        size = len(matrix)
        for r in range(size):
            for c in range(r+1, size):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]