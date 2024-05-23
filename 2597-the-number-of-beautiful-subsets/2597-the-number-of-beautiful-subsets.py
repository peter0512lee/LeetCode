class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = {}
        def f(i: int) -> int:
            if i == len(nums): # base case
                return 1
            result = f(i + 1) # nums[i] not taken
            if not nums[i] - k in freq and not nums[i] + k in freq: # check if we can take nums[i]
                freq[nums[i]] = freq.get(nums[i], 0) + 1
                result += f(i + 1) # nums[i] taken
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            return result
        return f(0) - 1 # -1 for empty subset