# Best time to buy and sell stock {Google}
# Solution-1 Easy and optimized solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 # left =buy, right =sell
        maxp=0
        while r < len(prices):
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                maxp = max(maxp, profit)
            else:
                l=r
            r+=1
        return maxp            
        
