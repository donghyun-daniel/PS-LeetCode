class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        from collections import deque
        from math import sqrt
        
        def is_connected(idx_1, idx_2):
            x1, y1, r1 = bombs[idx_1]
            x2, y2, r2 = bombs[idx_2]
            dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            return dist <= r1

        connection = collections.defaultdict(list)
        for idx_1 in range(len(bombs)):
            for idx_2 in range(len(bombs)):
                if idx_1 != idx_2 and is_connected(idx_1, idx_2):
                    connection[idx_1].append(idx_2)

        max_cnt = 1

        for bomb_idx in range(len(bombs)):
            if connection[bomb_idx]:
                q = deque([bomb_idx])
                visited = set([bomb_idx])
                cnt = 0
                while q:
                    now = q.popleft()
                    cnt += 1
                    for child in connection[now]:
                        if child not in visited:
                            visited.add(child)
                            q.append(child)
                max_cnt = max(max_cnt, cnt)

        return max_cnt