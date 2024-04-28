class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        current_length = 1
        longest_length = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] - nums[i - 1] == 1:
                    current_length += 1
                else: 
                    longest_length = max(current_length, longest_length)
                    current_length = 1
            
        return max(current_length, longest_length)


