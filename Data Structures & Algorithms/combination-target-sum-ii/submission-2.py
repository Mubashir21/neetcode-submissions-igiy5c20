class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, path, target):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0 or index == len(candidates):
                return

            # take this number
            path.append(candidates[index])
            dfs(index + 1, path, target - candidates[index])

            # skip this number
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            path.pop()
            dfs(next_index, path, target)
        dfs(0, [], target)
        return res