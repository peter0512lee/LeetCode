class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Find XOR of the two elements that appear only once
        x = 0
        for num in nums:
            x ^= num

        # Step 2: Find the rightmost set bit in the XOR result
        mask = x & -x
        
        # Step 3: Separate the elements into two groups
        group1, group2 = 0, 0
        for num in nums:
            if num & mask:
                group1 ^= num
            else:
                group2 ^= num
        
        # Step 4: XOR all the elements in each group separately
        return [group1, group2]