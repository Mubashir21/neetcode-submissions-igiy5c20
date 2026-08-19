class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums) - 2
        prefix = [1] *  len(nums)
        sufix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i-1]
            sufix[r] = sufix[r + 1] * nums[r + 1]
            r -= 1
        return [prefix[i] * sufix[i] for i in range(len(nums))]