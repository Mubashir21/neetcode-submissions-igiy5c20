class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums) - 1):
            temp = right
            right = max(left + nums[i], right)
            left = temp
        first = right

        left, right = 0, 0

        for i in range(1, len(nums)):
            tmp = right
            right = max(left + nums[i], right)
            left = tmp
        return max(first, right)