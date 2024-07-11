class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        reverse = []
        for i in range(len(s)):
            if s[i] == ')':  # pop the substring between nearest parentheses
                p = stack.pop()
                while p != '(':
                    reverse.append(p)
                    p = stack.pop()
                stack += reverse
                reverse = []
            else:
                stack.append(s[i])
        return ''.join(stack)