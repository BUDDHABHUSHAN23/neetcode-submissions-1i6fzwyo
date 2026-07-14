class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # V.2.0
        # Using the 2 pointers apporch 
        l , r = 0 , 1 
        maxProfit = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                Profit = prices[r] - prices[l]
                maxProfit = max(maxProfit , Profit)
            else :
                l = r 
            r += 1 
        return maxProfit