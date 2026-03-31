class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        result = [1] * len(nums)
        prefix = 1
        postfix = 1

        for idx, n in enumerate(nums):
            result[idx] = prefix
            prefix *= n

        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
