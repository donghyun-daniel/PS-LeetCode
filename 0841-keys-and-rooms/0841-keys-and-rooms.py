class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {i: False for i in range(len(rooms))}
        queue = [0]
        while queue:
            now = queue.pop()
            visited[now] = True
            queue += [key for key in rooms[now] if not visited[key]]
        return all(visited.values())