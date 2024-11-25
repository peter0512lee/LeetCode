class Solution:
    def isValid(self, s: str) -> bool:
        """
        利用 stack 解決這題
        將 input 輸入到 stack
        並且與 top 比較
        如果剛好是相對應的括號，pop
        """

        matching_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for bracket in s:
            if bracket not in matching_brackets:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != matching_brackets[bracket]:
                    return False

        return not stack