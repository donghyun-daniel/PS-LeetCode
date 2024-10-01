class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[r_start, c_start]]
        total_cells = rows * cols
        
        if total_cells == 1:
            return result

        steps = 0
        d = 0

        while len(result) < total_cells:
            steps += 1
            for _ in range(2):
                for _ in range(steps):
                    r_start += directions[d][0]
                    c_start += directions[d][1]
                    if 0 <= r_start < rows and 0 <= c_start < cols:
                        result.append([r_start, c_start])
                        if len(result) == total_cells:
                            return result
                d = (d + 1) & 3

        return result