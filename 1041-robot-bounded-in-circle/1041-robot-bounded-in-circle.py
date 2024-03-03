class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        now_pos = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        for cmd in instructions:
            if cmd == 'G':
                now_pos = [x + y for x, y in zip(now_pos, directions[dir_idx])]
            elif cmd == 'L':
                dir_idx = (dir_idx - 1) % 4
            elif cmd == 'R':
                dir_idx = (dir_idx + 1) % 4
        return now_pos == [0, 0] or dir_idx != 0