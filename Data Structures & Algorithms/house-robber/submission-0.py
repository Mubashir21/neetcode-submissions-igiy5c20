class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0

        for i in range(len(nums)):
            temp = right
            right = max(left + nums[i], right)
            left = temp
        return right
        