class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)-1):
            j = i+1

            while j < len(prices):
                profit = max(prices[j] -prices[i], profit)
                j +=1
        return profit