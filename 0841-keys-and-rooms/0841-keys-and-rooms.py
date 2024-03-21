class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False] * (len(rooms) - 1)
        queue = [0]
        while queue:
            now = queue.pop()
            not_visited_rooms = [key for key in rooms[now] if not visited[key]]
            for key in not_visited_rooms:
                visited[key] = True
            queue += not_visited_rooms
        return all(visited)