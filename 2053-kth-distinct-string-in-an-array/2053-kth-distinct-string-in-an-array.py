class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = defaultdict(int)
        for s in arr:
            str_dict[s] += 1

        for s in arr:
            if str_dict[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""