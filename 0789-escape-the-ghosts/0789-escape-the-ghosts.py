class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(x - target[0]) + abs(y - target[1]) <= distance:
                return False
        return True