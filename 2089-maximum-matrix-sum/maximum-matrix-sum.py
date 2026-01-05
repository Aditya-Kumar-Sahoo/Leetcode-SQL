from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0
        
        for row in matrix:
            for num in row:
                total_sum += abs(num)
                min_abs = min(min_abs, abs(num))
                if num < 0:
                    negative_count += 1
        
        # If odd number of negatives, we need to subtract 2*min_abs
        # (converting the smallest absolute value to negative)
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs
        
        return total_sum