class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize a counter for the first 'k' elements
        num_counter = Counter(nums[:k])
      
        # Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])
      
        # If the number of unique elements equals 'k', assign sum to 'max_sum', else 0
        max_sum = current_sum if len(num_counter) == k else 0
      
        # Iterate over the rest of the elements, starting from the 'k'th element
        for i in range(k, len(nums)):
            # Add the new element to the counter and sum
            num_counter[nums[i]] += 1
            current_sum += nums[i]
          
            # Remove the (i-k)'th element from the counter and sum
            num_counter[nums[i - k]] -= 1
            current_sum -= nums[i - k]
          
            # If there's no more instances of the (i-k)'th element, remove it from the counter
            if num_counter[nums[i - k]] == 0:
                del num_counter[nums[i - k]]
          
            # Update 'max_sum' if the number of unique elements in the window equals 'k'
            if len(num_counter) == k:
                max_sum = max(max_sum, current_sum)
      
        # Return the maximum sum found that matches the unique count condition
        return max_sum