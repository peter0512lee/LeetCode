class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # split by space
        words = sentence.split(" ")

        for i in range(len(words)):
            if words[i-1][-1] != words[i][0]:
                return False

        return True