class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sorted(d, key=d.get, reverse=True)[:k]
