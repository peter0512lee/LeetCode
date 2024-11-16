class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        
        # For each possible subarray of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            is_sorted = all(subarray[j] < subarray[j + 1] for j in range(len(subarray) - 1))
            
            is_consecutive = False
            if is_sorted:
                is_consecutive = all(subarray[j + 1] - subarray[j] == 1 for j in range(len(subarray) - 1))
            
            if is_sorted and is_consecutive:
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results
