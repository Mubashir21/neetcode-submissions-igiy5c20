class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [[-1] * (len(nums)+1) for _ in range(len(nums))]
        def dfs(i, j):
            if i == len(nums):
                return 0
            if mem[i][j+1] != -1:
                return mem[i][j+1]
            LIS = dfs(i + 1, j)
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i))
            mem[i][j+1] = LIS
            return LIS
        return dfs(0, -1)