class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize a variable to keep track of the changes needed.
        changes_needed = 0

        # Iterate over the string starting from the second character until the end
        # and consider only odd indices (Python uses 0-based indexing).
        for i in range(1, len(s), 2):

            # Check if the current character is different from the previous one.
            # If so, this is not a change we are interested in, so continue.
            # We are interested in pairs of characters that are the same and
            # as given alternate characters should be different in a "nice" s.
            if s[i] == s[i - 1]:
                changes_needed += 1  # Increment the changes needed.

        # Return the total number of changes needed to have no two consecutive characters
        # being the same at odd indices, making the string "nice" as per the defined condition.
        return changes_needed