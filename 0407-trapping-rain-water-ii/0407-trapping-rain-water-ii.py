from typing import List
import heapq

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        if not height_map or not height_map[0]:
            return 0

        x, y = len(height_map), len(height_map[0])
        if x < 3 or y < 3:
            return 0

        # Initialize visited array and priority queue
        visited = [[False] * y for _ in range(x)]
        heap = []

        # Add boundary cells to the heap
        for r in range(x):
            for c in range(y):
                if r == 0 or r == x-1 or c == 0 or c == y-1:
                    heapq.heappush(heap, (height_map[r][c], r, c))
                    visited[r][c] = True

        # Directions for neighboring cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        water = 0
        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < x and 0 <= new_c < y and not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    new_height = max(height, height_map[new_r][new_c])
                    water += max(0, height - height_map[new_r][new_c])
                    heapq.heappush(heap, (new_height, new_r, new_c))

        return water