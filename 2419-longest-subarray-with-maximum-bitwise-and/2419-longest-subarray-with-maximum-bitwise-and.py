class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = 0
        max_val = 0

        for num in nums:
            max_val = max(max_val, num)

        count = 0
        for num in nums:
            if num == max_val:
                count += 1
                length = max(length, count)
            else:
                count = 0

        return length