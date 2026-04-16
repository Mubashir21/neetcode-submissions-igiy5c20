class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = res = nums[0]

        for num in range(1, len(nums)):
            tmp = maxP * nums[num]
            maxP = max(maxP * nums[num], minP * nums[num], nums[num])
            minP = min(tmp, minP * nums[num], nums[num])
            res = max(res, maxP)
        return res