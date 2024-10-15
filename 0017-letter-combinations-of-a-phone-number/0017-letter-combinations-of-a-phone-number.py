class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

        n = len(digits)

        if n == 0:
            return []
            
        ans = []
        path = [''] * n
        def dfs(i):
            # 邊界條件
            if i == n:
                ans.append(''.join(path))
                return
            # 遞條件
            for c in mapping[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans