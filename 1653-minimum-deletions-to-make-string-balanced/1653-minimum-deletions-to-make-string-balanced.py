class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = 0
        for c in s:
            a_count_right += 1 if c == "a" else 0

        b_count_left = 0
        res = len(s)
        for i, c in enumerate(s):
            if c == "a":
                a_count_right -= 1
            res = min(res, b_count_left + a_count_right)
            if c == "b":
                b_count_left += 1
        
        return res