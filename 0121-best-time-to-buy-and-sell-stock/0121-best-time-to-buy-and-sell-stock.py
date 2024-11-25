class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        slow, fast = 0, 0

        while fast < len(prices):
            current_profit = prices[fast] - prices[slow]
            max_profit = max(current_profit, max_profit)
            if prices[slow] > prices[fast]:
                slow = fast
            fast += 1
        
        return max_profit