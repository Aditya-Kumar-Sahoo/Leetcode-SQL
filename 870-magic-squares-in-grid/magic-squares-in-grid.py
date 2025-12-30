class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        
        def is_magic(r, c):
            # Extract numbers
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)
            if len(nums) != 9:
                return False
            
            # Check sums
            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]  # row0 sum
            # Check rows
            for i in range(3):
                if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != s:
                    return False
            # Check cols
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != s:
                    return False
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            return True
        
        count = 0
        for r in range(m - 2):
            for c in range(n - 2):
                if is_magic(r, c):
                    count += 1
        return count