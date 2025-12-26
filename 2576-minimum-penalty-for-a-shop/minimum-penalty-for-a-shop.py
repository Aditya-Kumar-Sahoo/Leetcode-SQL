class Solution:
    def bestClosingTime(self, customers):
        n = len(customers)
        total_Y = customers.count('Y')
        
        min_penalty = total_Y
        best_hour = 0
        prefix_Y = 0
        
        for j in range(1, n + 1):
            if customers[j - 1] == 'Y':
                prefix_Y += 1
            penalty = j + total_Y - 2 * prefix_Y
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j
        
        return best_hour