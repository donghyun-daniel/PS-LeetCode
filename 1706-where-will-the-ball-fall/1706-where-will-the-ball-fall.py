class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        balls = [i for i in range(len(grid[0]))]
        num_of_balls = len(balls)
        for row in grid:
            for idx, pos in enumerate(balls):
                if pos == -1:
                    continue
                direction = row[pos]
                if (pos + direction in (-1, num_of_balls)) or (
                    direction + row[pos + direction] == 0
                ):  # get stucked
                    balls[idx] = -1
                else:
                    balls[idx] += direction
        return balls