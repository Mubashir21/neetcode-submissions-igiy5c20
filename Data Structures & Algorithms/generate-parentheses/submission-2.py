class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opening, closing, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if opening < n:
                path.append("(")
                dfs(opening + 1, closing, path)
                path.pop()

            if closing < opening:
                path.append(")")
                dfs(opening, closing + 1, path)
                path.pop()

        dfs(0, 0, [])
        return res