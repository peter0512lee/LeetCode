class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s = list(reversed(s))
        t = list(reversed(t))
        while s and t:
            if s[-1] == t[-1]:
                t.pop()
            s.pop()
        return len(t)