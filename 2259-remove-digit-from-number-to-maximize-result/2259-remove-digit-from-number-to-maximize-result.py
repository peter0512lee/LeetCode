class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        candidates = []

        for i in range(len(number)):
            if number[i] == digit:
                new_num = number[:i] + number[i+1:]
                candidates.append(new_num)

        return max(candidates)