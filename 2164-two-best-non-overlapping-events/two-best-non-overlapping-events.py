class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        n = len(events)
        
        # Create an array to store the maximum value of events ending at or before each time
        # dp[i] = maximum value of an event ending at or before events[i].end
        dp = [0] * n
        dp[0] = events[0][2]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1], events[i][2])
        
        # Helper function to find the rightmost event that ends before start time
        def binary_search(start_time):
            left, right = 0, n - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if events[mid][1] < start_time:
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        max_sum = 0
        
        # Consider taking only one event
        for i in range(n):
            max_sum = max(max_sum, events[i][2])
        
        # Consider taking two events
        for i in range(n):
            # Current event
            current_value = events[i][2]
            
            # Find the best event that ends before current event starts
            idx = binary_search(events[i][0])
            
            if idx != -1:
                max_sum = max(max_sum, current_value + dp[idx])
        
        return max_sum