class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        isFlipped = [0] * n
        flip = 0
        flips = 0

        for i in range(n):
            if i >= k:
                flip ^= isFlipped[i - k]

            if nums[i] == flip:
                if i + k > n:
                    return -1
                flips += 1
                flip ^= 1
                if i + k < n:
                    isFlipped[i] = 1
        
        return flips