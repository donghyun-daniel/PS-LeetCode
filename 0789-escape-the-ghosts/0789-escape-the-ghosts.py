class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        target_x, target_y = target
        for x, y in ghosts:
            if abs(x - target_x) + abs(y - target_y) <= distance:
                return False
        return True