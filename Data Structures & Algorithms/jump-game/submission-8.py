class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maps = {}

        # def dfs(cur):
        #     if cur >= len(nums) - 1:
        #         return True
        #     if nums[cur] == 0:
        #         return False
        #     if cur in maps:
        #         return maps[cur]
            
        #     can = False
        #     for i in range(1, nums[cur] + 1):
        #         if cur + i >= len(nums) - 1:      # clamp: no need to go further
        #             maps[cur] = True
        #             return True
        #         if dfs(cur + i):
        #             maps[cur] = True
        #             return True
        #     maps[cur] = False
        #     return False
        # return dfs(0)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= goal - i:
                goal = i
            
        return True if goal == 0 else False