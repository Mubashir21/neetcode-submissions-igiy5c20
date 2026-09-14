class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1]
        back = [1]
        i = 0
        r = len(nums) - 1
        while i < len(nums):
            front.append(front[i] * nums[i])
            back.append(back[i] * nums[r])
            i += 1
            r -= 1
        back.reverse()
        
        res = []
        for i in range(len(nums)):
            res.append(front[i] * back[i + 1])
        return res