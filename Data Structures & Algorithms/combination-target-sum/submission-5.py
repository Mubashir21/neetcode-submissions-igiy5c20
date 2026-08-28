class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, path, target):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i, path, target-nums[i])
                path.pop()
        dfs(0, [], target)
        return res