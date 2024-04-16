class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [0] * 4
        for idx in reversed(range(0, n-1)):
            if obstacles[idx] == 0 or obstacles[idx] == obstacles[idx-1]:
                continue
            dp[obstacles[idx]] = min(
                dp[lane] for lane in range(1, 4) if obstacles[idx] != lane and obstacles[idx-1] != lane
            ) + 1
            
        return dp[2]
    