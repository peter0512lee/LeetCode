class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        answer = 0
        happiness.sort(reverse=True)

        for idx, val in enumerate(happiness[:k]):
            val -= idx
            answer += max(val, 0)

        return answer