class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        
        # Limit k to maximum possible transactions
        k = min(k, n // 2)
        
        # Initialize DP arrays
        dp_prev = [0] * n
        
        for _ in range(k):
            dp_curr = [0] * n
            best_buy = -prices[0]
            best_sell = prices[0]
            
            for i in range(1, n):
                # Maximum profit by day i
                dp_curr[i] = max(
                    dp_curr[i - 1],
                    best_buy + prices[i],
                    best_sell - prices[i]
                )
                
                # Update for next iteration
                prev = dp_prev[i - 1]
                best_buy = max(best_buy, prev - prices[i])
                best_sell = max(best_sell, prev + prices[i])
            
            dp_prev = dp_curr
        
        return dp_prev[-1]