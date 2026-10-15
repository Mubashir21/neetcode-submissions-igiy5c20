class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            prevMax = curMax
            prevMin = curMin

            curMax = max(prevMax * nums[i], nums[i], prevMin * nums[i])
            curMin = min(prevMax * nums[i], nums[i], prevMin * nums[i])
            res = max(res, curMax)
        return res