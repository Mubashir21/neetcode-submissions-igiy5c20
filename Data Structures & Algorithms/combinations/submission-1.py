class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(index, path):
            if len(path) == k:
                res.append(path.copy())
                return
            if index > n:
                return

            path.append(index)
            dfs(index + 1, path)
            path.pop()
            dfs(index + 1, path)
        dfs(1, [])
        return res