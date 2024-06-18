class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        idx = 0
        res = 0
        best = 0
        for work in worker:
            while idx < len(difficulty) and work >= difficulty[idx]:
                best = max(best, profit[idx])
                idx += 1

            res += best

        return res