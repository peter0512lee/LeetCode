class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[right] == -nums[left]:
                return nums[right]
            elif nums[right] > -nums[left]:
                right -= 1
            else:
                left += 1

        return -1