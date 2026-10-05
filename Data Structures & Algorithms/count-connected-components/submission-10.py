
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = []
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count
