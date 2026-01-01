class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Process from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set 9 to 0 and continue
        
        # If all digits were 9 (e.g., 999 -> 1000)
        return [1] + [0] * n