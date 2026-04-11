class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, target, path):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # optional optimization
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()
            
        dfs(0, target, [])
        return res