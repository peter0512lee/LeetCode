class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        window_ones = max_window_ones = 0
        l = 0
        N = len(nums)
        for r in range(2 * N):
            if nums[r % N] == 1:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % N]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones 