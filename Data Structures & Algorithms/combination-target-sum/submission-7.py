class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(index, path, summ):
            if summ > target:
                return
            if summ == target:
                res.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i, path, summ + nums[i])
                path.pop()
        dfs(0, [], 0)
        return res