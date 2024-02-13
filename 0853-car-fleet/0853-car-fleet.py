class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev, result = 0, 0
        for p, s in sorted(list(zip(position, speed)), reverse=True):
            hours = (target - p) / s
            if prev < hours:
                result += 1
                prev = hours
        return result
        