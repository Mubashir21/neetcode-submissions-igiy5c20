class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, summ, path):
            if summ == target:
                res.append(path.copy())
                return
            if index == len(nums) or summ > target:
                return 
            
            path.append(nums[index])
            dfs(index, summ + nums[index], path)
            path.pop()
            dfs(index + 1, summ, path)
        dfs(0, 0, [])
        return res