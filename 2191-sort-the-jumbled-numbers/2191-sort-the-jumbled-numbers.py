class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # List to hold tuples of the mapped value and its original index
        mapped_with_index = []
      
        # Iterate over the input numbers' list
        for index, num in enumerate(nums):
            # If the number is 0, get the mapped value for 0, else start with 0
            mapped_num = mapping[0] if num == 0 else 0
            power_of_ten = 1  # To keep track of the decimal place
          
            # Decompose the number into digits and map using the provided mapping
            while num:
                num, digit = divmod(num, 10)
                # Map the digit, adjust decimal place and add to the mapped number
                mapped_num = mapping[digit] * power_of_ten + mapped_num
                power_of_ten *= 10  # Increase the decimal place
          
            # Append the tuple of mapped number and original index to the list
            mapped_with_index.append((mapped_num, index))
      
        # Sort the list according to the mapped numbers, stable for identical values
        mapped_with_index.sort()
      
        # Reconstruct the sorted list using the original indices
        return [nums[i] for _, i in mapped_with_index]