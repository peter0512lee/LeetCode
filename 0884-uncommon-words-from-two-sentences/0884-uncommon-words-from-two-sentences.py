class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        s = s1 + s2
        
        word_count = Counter(s)

        return [word for word in word_count if word_count[word] == 1]