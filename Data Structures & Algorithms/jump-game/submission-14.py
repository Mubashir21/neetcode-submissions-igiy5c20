class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(index):
            if index >= len(nums):
                return False
            if index == len(nums) - 1:
                return True
            if index in memo:
                return memo[index]
            for i in range(1, nums[index]+1):
                if dfs(index + i):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return dfs(0)