class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                path.append(nums[i])
                dfs(path)
                path.pop()
                seen.remove(i)
            
        dfs([])
        return res
            