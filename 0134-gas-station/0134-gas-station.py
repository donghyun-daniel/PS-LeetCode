class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        tank = 0
        start_idx = 0
        for idx in range(len(gas)):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                start_idx = idx + 1
                tank = 0
        return start_idx