class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit = [-1 for _ in range(32)]
        n = len(nums)
        j, cur, res = 0, 0, float("inf")
        for i in range(n):
            cur |= nums[i]
            for b in range(32):
                if nums[i] & 1 << b: bit[b] = i
            while cur >= k and j <= i:
                res = min(res, i - j + 1)
                for b in range(32):
                    if nums[j] & 1 << b and bit[b] == j:
                        bit[b] = -1
                        cur ^= 1 << b
                j += 1     
        return res if res != float("inf") else -1