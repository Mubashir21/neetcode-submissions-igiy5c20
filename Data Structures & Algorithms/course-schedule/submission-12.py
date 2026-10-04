class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        path = set()
        def dfs(node):
            if node in path:
                return False
            if adj[node] == []:
                return True
             
            path.add(node)
             
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            adj[node] = []
            path.remove(node)
            return True
    

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True