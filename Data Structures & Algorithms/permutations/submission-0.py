class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                
                path.append(num)
                seen.add(num)

                dfs(path)

                path.pop()
                seen.remove(num)
        dfs([])
        return res