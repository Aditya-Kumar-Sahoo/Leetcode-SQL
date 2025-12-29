from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # Build a mapping from (left, right) to list of possible tops
        patterns = defaultdict(list)
        for a in allowed:
            patterns[(a[0], a[1])].append(a[2])
        
        memo = {}
        
        def can_build(row):
            # Check memoization first
            if row in memo:
                return memo[row]
            
            # Base case: reached the top of pyramid
            if len(row) == 1:
                memo[row] = True
                return True
            
            # Generate all possible next rows
            next_rows = []
            
            # Helper function to generate next rows via backtracking
            def generate_next(idx, current):
                if idx == len(row) - 1:
                    next_rows.append(current)
                    return
                
                left, right = row[idx], row[idx + 1]
                key = (left, right)
                if key in patterns:
                    for top in patterns[key]:
                        generate_next(idx + 1, current + top)
            
            generate_next(0, "")
            
            # Try each possible next row
            for next_row in next_rows:
                if can_build(next_row):
                    memo[row] = True
                    return True
            
            memo[row] = False
            return False
        
        return can_build(bottom)