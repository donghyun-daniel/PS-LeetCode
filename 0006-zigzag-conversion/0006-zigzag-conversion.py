class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        row_arr = [""] * num_rows
        row_idx = 0
        dir = -1
        for ch in s:
            row_arr[row_idx] += ch
            if row_idx == num_rows-1 or row_idx == 0:
               dir *= -1 
            row_idx += dir
        return "".join(row_arr)