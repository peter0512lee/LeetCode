class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def is_consecutive_and_sorted(subarray):
            return all(subarray[i] + 1 == subarray[i + 1] for i in range(len(subarray) - 1))

        n = len(nums)
        res = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if is_consecutive_and_sorted(subarray):
                res.append(max(subarray))
            else:
                res.append(-1)

        return res