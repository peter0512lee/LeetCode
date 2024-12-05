class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Check initial conditions
        if (len(start) != len(target)
            or start.count('_') != target.count('_')): return False

        n, i, j = len(start), 0, 0

        while i < n or j < n:
            # Move i and j to the next non-underscore character
            while i < n and start[i]  == '_': i += 1
            while j < n and target[j] == '_': j += 1

            # If both indices are out of bounds, we are done
            if i == n and j == n: return True

            # If one index is out of bounds or characters differ, return False
            if i == n or j == n or start[i] != target[j]: return False

            # Check if the transformation is valid
            if start[i] == 'L' and i < j: return False
            if start[i] == 'R' and i > j: return False

            # Move to the next character
            i += 1
            j += 1

        return True