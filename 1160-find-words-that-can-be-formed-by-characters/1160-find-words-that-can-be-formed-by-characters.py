class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            for c in word:
                if word.count(c) > chars.count(c):
                    break
            else:
                res += len(word)
        return res