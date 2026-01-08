from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # Find maximum single pair product (for all negatives case)
        max_single = float('-inf')
        for a in nums1:
            for b in nums2:
                max_single = max(max_single, a * b)
        
        # DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]
                # Three choices:
                # 1. Skip nums1[i-1] -> dp[i-1][j]
                # 2. Skip nums2[j-1] -> dp[i][j-1]
                # 3. Take the pair, either extending previous subsequence or starting new
                extend = max(dp[i - 1][j - 1], 0) + product
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], extend)
        
        # If final result is positive, return it
        # Otherwise, we must take at least one pair (the best single pair)
        return dp[n][m] if dp[n][m] > 0 else max_single