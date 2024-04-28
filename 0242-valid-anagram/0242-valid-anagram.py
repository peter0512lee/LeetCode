class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = collections.defaultdict(int)

        for c in s:
            char_count[c] += 1

        for c in t:
            if char_count[c] == 0:
                return False
            char_count[c] -= 1
        
        return True
            