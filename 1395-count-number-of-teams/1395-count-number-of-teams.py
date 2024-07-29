class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = []
        sr = sorted(rating)
        low = {}

        for idx,r in enumerate(sr):
            low[r] = idx

        res = 0
        n = len(rating)

        for idx,r in enumerate(rating):
            i = bisect.bisect(l, r)
            l.insert(i,r)
            j = low[r] - i
            res+=i*(n-1-idx-j)+j*(idx-i)

        return res