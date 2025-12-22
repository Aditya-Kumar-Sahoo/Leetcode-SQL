class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        L = len(strs[0])
        dp = [1] * L
        
        for j in range(L):
            for k in range(j):
                valid = True
                # Check if column k can come before column j
                for i in range(n):
                    if strs[i][k] > strs[i][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[k] + 1)
        
        return L - max(dp)