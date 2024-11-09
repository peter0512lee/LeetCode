class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        b = 1
        for i in range(64):
            if b & x == 0:
                x |= (n & 1) * b
                n >>= 1
            b <<= 1
        return x