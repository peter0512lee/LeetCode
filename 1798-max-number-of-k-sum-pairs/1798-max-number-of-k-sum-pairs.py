class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res, d = 0, Counter(nums)
        for val1, cnt in d.items():
            val2 = k - val1
            if val2 < val1 or val2 not in d: continue
            res += min(cnt, d[val2]) if val1 != val2 else cnt // 2
        
        return res