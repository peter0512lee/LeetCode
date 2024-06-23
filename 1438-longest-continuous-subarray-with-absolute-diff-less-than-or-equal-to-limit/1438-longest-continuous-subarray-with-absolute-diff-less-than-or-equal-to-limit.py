from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Initialize a SortedList which allows us to maintain a sorted collection of numbers
        sorted_list = SortedList()
      
        # Initialize variables for the answer and the start index of the window
        max_length = 0
        window_start = 0

        # Iterate through the array with index and value
        for window_end, value in enumerate(nums):
            # Add the current value to the sorted list
            sorted_list.add(value)

            # Shrink the window from the left if the condition is violated
            # The condition being if the absolute difference between the max and min values in the window exceeds the limit
            while sorted_list[-1] - sorted_list[0] > limit:
                # Remove the leftmost value from the sorted list as we're shrinking the window
                sorted_list.remove(nums[window_start])
                # Move the start of the window to the right
                window_start += 1

            # Calculate the length of the current window and compare with the max
            # Update the max_length as needed
            max_length = max(max_length, window_end - window_start + 1)

        # Return the length of the longest subarray after examining all windows
        return max_length