class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        len_part = len(part)

        while (s.find(part) != -1):
            start_idx = s.find(part)
            end_idx = start_idx + len_part
            print(start_idx, end_idx)
            s = s[:start_idx] + s[end_idx:]
            print(s)

        return s