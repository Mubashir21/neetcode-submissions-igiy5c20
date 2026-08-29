class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = {i:[] for i in range(numCourses)}
        # visited = set()
            
        for a, b in prerequisites:
            maps[a].append(b)

        def dfs(node, visited):
            if len(maps[node]) == 0:
                return True
            if node in visited:
                return False

            visited.add(node)
            for nei in maps[node]:
                if not dfs(nei, visited):
                    return False
            visited.remove(node)
            maps[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True