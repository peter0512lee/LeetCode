class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accum = 1
        final_lst = [1]
        # left
        for i in range(1, len(nums)):
            accum *= nums[i-1]
            final_lst.append(accum)
        accum = 1
        # right
        for i in range(len(nums)-1, 0, -1):
            accum *= nums[i]
            final_lst[i-1] *= accum
        return final_lst