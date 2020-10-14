# 841. Keys and Rooms
# BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        while queue:
            num = queue.pop(0)
            visited.add(num)
            room = rooms[num]
            for key in room:
                if key not in visited:
                    queue.append(key)
        return len(visited) == len(rooms)

# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(num):
            if num in visited:
                return
            visited.add(num)
            for key in rooms[num]:
                dfs(key)
        dfs(0)
        return len(visited) == len(rooms)
