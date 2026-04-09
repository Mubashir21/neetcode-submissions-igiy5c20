class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(index, target, path):
            if target == 0:
                res.append(path.copy())
                return
            elif target < 0:
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, target - nums[i], path)
                path.pop()
        backtrack(0, target, [])
        return res