class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(index, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            if index >= len(nums):
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                dfs(i, path)
                path.pop()
                used.remove(nums[i])
        dfs(0, [])
        return res