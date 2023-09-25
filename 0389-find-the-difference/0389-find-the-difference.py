class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for char in t_count:
            if s_count[char] != t_count[char]:
                return char