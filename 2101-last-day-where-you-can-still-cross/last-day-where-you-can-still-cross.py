from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            
            # Flood cells for given day
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # water
            
            q = deque()
            visited = [[False] * col for _ in range(row)]
            
            # Start BFS from top row land cells
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    visited[0][c] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                r, c = q.popleft()
                
                # Reached bottom row
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            
            return False
        
        left, right = 0, row * col
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
