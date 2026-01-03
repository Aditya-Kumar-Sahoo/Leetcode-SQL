class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Calculate the number of ways to paint a 3×n grid with 3 colors.
        Each 1×3 column must use exactly 3 colors (ABA or ABC patterns).
        Adjacent cells cannot have the same color.
      
        Args:
            n: Number of columns in the grid
          
        Returns:
            Number of valid painting ways modulo 10^9 + 7
        """
        MOD = 10**9 + 7
      
        # Initialize counters for the first column
        # aba_pattern_count: Number of ways to paint a column with ABA pattern (same first and last color)
        # abc_pattern_count: Number of ways to paint a column with ABC pattern (all different colors)
        # Both start with 6 ways each (3 colors × 2 permutations each)
        aba_pattern_count = 6  # Patterns like: RGR, GRG, BRB, RBR, GBG, BGB
        abc_pattern_count = 6  # Patterns like: RGB, RBG, GRB, GBR, BRG, BGR
      
        # Build up the solution column by column
        for column_index in range(n - 1):
            # Calculate valid patterns for the next column based on current column
            # From ABA pattern: can transition to 3 ABA patterns + 2 ABC patterns
            # From ABC pattern: can transition to 2 ABA patterns + 2 ABC patterns
            next_aba_count = (3 * aba_pattern_count + 2 * abc_pattern_count) % MOD
            next_abc_count = (2 * aba_pattern_count + 2 * abc_pattern_count) % MOD
          
            # Update pattern counts for the next iteration
            aba_pattern_count = next_aba_count
            abc_pattern_count = next_abc_count
      
        # Return the total number of valid ways
        return (aba_pattern_count + abc_pattern_count) % MOD
