class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        put nums in set
        itertate through nums
        if square of number is in set, increment streak, until square of number is not in set
        return max streak
        """
        nums_set = set(nums)
        nums.sort()
        max_streak = 0
        for num in nums:
            streak = 1
            while num*num in nums_set:
                streak += 1
                num = num*num
            max_streak = max(max_streak, streak)
        return max_streak if max_streak > 1 else -1