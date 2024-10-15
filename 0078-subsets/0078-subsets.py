class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            # 邊界條件
            if i == n:
                ans.append(path.copy())
                return
            # 非邊界條件
            dfs(i+1)

            # 選與不選
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans