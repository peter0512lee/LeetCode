class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place = sorted(score, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            list(map(str, range(4, len(score) + 1)))
        d = dict(zip(place, rank))
        return [d[s] for s in score]