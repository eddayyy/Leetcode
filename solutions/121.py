class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0 
        l, r = 0, 1
        profit = maxProfit = 0 

        # Iterate through the entire list 
        while r < n:
            # Check if the transaction is profitable 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # Keep track of our maximum profit 
                maxProfit = max(maxProfit, profit) 
            else:
                # Move l up if it's greater than our right pointer 
                l = r
            # Always move our right pointer up 
            r += 1 
        return maxProfit 