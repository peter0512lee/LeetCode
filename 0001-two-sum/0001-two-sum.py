class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        建立一個 num -> idx 的 hashmap，如果剩餘的數有在 map 裡的話，就是答案
        否則把當前的 num 跟 idx 記錄在 map
        """
        num_idx_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_idx_map:
                return [num_idx_map[complement], i]
            num_idx_map[num] = i