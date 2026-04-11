class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        brackets = ["(", ")"]

        def dfs(opening, closing, path):
            if len(path) == (2*n) and closing == opening:
                res.append("".join(path))
                return
            if closing > opening or len(path) >  (2 * n):
                return
            
            for bracket in brackets:
                path.append(bracket)
                if bracket == "(":
                    dfs(opening + 1, closing, path)
                else:
                    dfs(opening, closing + 1, path)
                path.pop()
        
        dfs(0, 0, [])
        return res
            
