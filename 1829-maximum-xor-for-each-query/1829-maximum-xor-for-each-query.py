class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Intialize an empty list to store the answers
        answers = []
      
        # Perform XOR on all elements in nums to get the initial xor_sum
        xor_sum = reduce(xor, nums)
      
        # Create a mask which will have ones for the number of maximumBit bits
        mask = (1 << maximumBit) - 1
      
        # Iterate over the nums list in reverse order
        for num in reversed(nums):
            # Calculate k as XOR of xor_sum with mask to get the maximum XOR value
            k = xor_sum ^ mask
            # Append the resultant k to the answers list
            answers.append(k)
            # Update the xor_sum by XORing it with the current number
            xor_sum ^= num
          
        # Return the list of answers
        return answers