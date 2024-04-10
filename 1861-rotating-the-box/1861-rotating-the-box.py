class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def rotate(mat: List[List[str]]):
            return [list(e) for e in zip(*mat[::-1])]
        def apply_gravity(mat):
            rows, cols = len(mat), len(mat[0])
            for c in range(cols):
                for r in reversed(range(rows)):
                    if mat[r][c] == '#':
                        target_row = None
                        for empty_row in range(r+1, rows):
                            if mat[empty_row][c] == '.':
                                target_row = empty_row
                            else: break
                        if target_row:
                            mat[r][c], mat[target_row][c] = mat[target_row][c], mat[r][c]
            return mat

        rotated_box = rotate(box)
        return apply_gravity(rotated_box)