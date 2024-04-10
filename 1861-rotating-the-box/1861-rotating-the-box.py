class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        new_box = [list(e) for e in zip(*box[::-1])]  # 90 degrees clockwise
        for r in new_box:
            print(r)
        (rows, cols) = (len(new_box), len(new_box[0]))
        for c in range(cols):
            target_row = rows - 1
            for r in reversed(range(rows)):
                if new_box[r][c] == '#':
                    new_box[r][c], new_box[target_row][c] = '.', '#'
                    target_row -= 1
                elif new_box[r][c] == '*':
                    target_row = r - 1
                elif new_box[r][c] == '.':
                    target_row = max(target_row, r)
        return new_box