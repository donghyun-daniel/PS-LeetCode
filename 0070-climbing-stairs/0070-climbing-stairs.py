class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        small, big = 1, 2
        for _ in range(2, n):
            small, big = big, small+big
        return big