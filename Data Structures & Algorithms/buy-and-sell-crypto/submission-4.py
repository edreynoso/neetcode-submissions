class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        prev = 0
        curr = 0
        while r < len(prices):
            curr = prices[r] - prices[l]
            if prices[l] >= prices[r] and r < len(prices)-1:
                l = r
                r +=1
                print(l,r)
                curr = prices[r] - prices[l]
            elif prices[l] <= prices[r] or curr < prev:
                r +=1
            else:
                break
            prev = max(curr, prev)

        return prev