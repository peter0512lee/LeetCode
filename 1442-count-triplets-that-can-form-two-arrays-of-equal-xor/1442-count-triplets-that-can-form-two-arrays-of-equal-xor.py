class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        A.insert(0, 0)
        n = len(A)
        for i in xrange(n - 1):
            A[i + 1] ^= A[i]
        res = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if A[i] == A[j]:
                    res += j - i - 1
        return res