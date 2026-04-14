class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()

        maps = {i:[] for i in range(n)}
        for a, c in edges:
            maps[a].append(c)
            maps[c].append(a)

        def dfs(node, par):
            if node in visited:
                return
            visited.add(node)
            for nei in maps[node]:
                dfs(nei, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                components += 1
        return components