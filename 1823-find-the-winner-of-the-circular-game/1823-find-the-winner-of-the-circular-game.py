class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 1
        for i in range(1,n):
            # here i represent number of alive people
            # p is f(i,'cac')
            p=(k+p-1)%(i+1)+1
            # p is f(i+1, 'cac')
        return p