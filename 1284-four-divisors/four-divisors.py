from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        
        for num in nums:
            divisor_count = 0
            divisor_sum = 0
            
            # Check divisors up to sqrt(num)
            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisor_count += 1
                    divisor_sum += i
                    
                    # If i and num/i are different
                    if i != num // i:
                        divisor_count += 1
                        divisor_sum += num // i
                    
                    # Early exit if we already have more than 4 divisors
                    if divisor_count > 4:
                        break
                i += 1
            
            if divisor_count == 4:
                total_sum += divisor_sum
        
        return total_sum