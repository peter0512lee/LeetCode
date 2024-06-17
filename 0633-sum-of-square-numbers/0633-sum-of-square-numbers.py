class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m = int(math.sqrt(c))  # a或b可能的最大值
        for a in range(m+1):
            b = round(math.sqrt(c-a*a))
            if a*a + b*b == c:
                return True
        return False