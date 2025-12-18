class Solution {
    public long maxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.length;
        long baseProfit = 0;
        for (int i = 0; i < n; i++) {
            baseProfit += (long) strategy[i] * prices[i];
        }
        
        // Prefix sums
        long[] prefixPrices = new long[n + 1];
        long[] prefixWeighted = new long[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefixPrices[i + 1] = prefixPrices[i] + prices[i];
            prefixWeighted[i + 1] = prefixWeighted[i] + (long) strategy[i] * prices[i];
        }
        
        int half = k / 2;
        long maxDelta = 0;
        
        // Try all possible modification windows
        for (int start = 0; start <= n - k; start++) {
            // Sum of prices in the second half of the window
            long secondHalfSum = prefixPrices[start + k] - prefixPrices[start + half];
            // Original weighted sum in the entire window
            long originalWeightedSum = prefixWeighted[start + k] - prefixWeighted[start];
            // Change in profit
            long delta = secondHalfSum - originalWeightedSum;
            
            if (delta > maxDelta) {
                maxDelta = delta;
            }
        }
        
        return baseProfit + maxDelta;
    }
}