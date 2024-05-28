class Solution:
    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if is_connected[city][neighbor] and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1

        return provinces