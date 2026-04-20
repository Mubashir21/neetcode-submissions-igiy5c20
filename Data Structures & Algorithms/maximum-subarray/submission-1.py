class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = 0
        #     for j in range(i, len(nums)):
        #         cur += nums[j]
        #         if cur > res:
        #             res = cur
        # return res

        res = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            res = max(res, cur)
        return res