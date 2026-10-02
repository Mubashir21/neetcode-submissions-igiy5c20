class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            if index == len(nums):
                res.append(path.copy())
                return

            # include nums[index]
            path.append(nums[index])
            dfs(index + 1, path)

            # undo
            path.pop()

            # exclude nums[index]
            dfs(index + 1, path)

        dfs(0, [])
        return res