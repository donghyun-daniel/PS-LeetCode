class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        for idx in range(n-2, 0, -2):
            result += abs(cost[idx] - cost[idx+1])
            cost[(idx//2)] += max(cost[idx:idx+2])
        return result