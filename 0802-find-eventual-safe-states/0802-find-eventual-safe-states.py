class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n # 0: not visited, 1: visiting, 2: terminal
        result = []

        def isSafe(node):
            if visited[node] > 0:
                return visited[node] == 2

            visited[node] = 1
            for dest in graph[node]:
                if not isSafe(dest):
                    return False
            
            visited[node] = 2
            return True

        for idx in range(n):
            if isSafe(idx):
                result.append(idx)
        
        return result