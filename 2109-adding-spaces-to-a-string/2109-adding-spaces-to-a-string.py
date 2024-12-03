class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        idx, size = 0, len(spaces)
        for i, c in enumerate(s):
            if idx < size and i == spaces[idx]:
                idx += 1
                res += " "
            res += c
        return res
                