import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by their original start time
        meetings.sort()
        
        # Min heap for available rooms (stores room numbers)
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # Min heap for busy rooms: (end_time, room_number)
        busy = []
        
        # Min heap for waiting meetings: (original_start_time, duration)
        waiting = []
        
        # Count meetings per room
        counts = [0] * n
        
        time = 0
        i = 0
        total_meetings = len(meetings)
        
        while i < total_meetings or waiting:
            # Add all meetings that should have started by current time to waiting queue
            while i < total_meetings and meetings[i][0] <= time:
                start, end = meetings[i]
                heapq.heappush(waiting, (start, end - start))
                i += 1
            
            # Free up all rooms that have finished by current time
            while busy and busy[0][0] <= time:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)
            
            # Assign waiting meetings to available rooms
            while waiting and free_rooms:
                original_start, duration = heapq.heappop(waiting)
                room = heapq.heappop(free_rooms)
                counts[room] += 1
                heapq.heappush(busy, (time + duration, room))
            
            # If there are no waiting meetings but still future meetings
            if not waiting and i < total_meetings:
                # Jump to the start time of the next meeting
                time = meetings[i][0]
            # If there are waiting meetings but no free rooms
            elif waiting and not free_rooms:
                # Jump to when the next room becomes free
                next_free_time, next_free_room = heapq.heappop(busy)
                heapq.heappush(free_rooms, next_free_room)
                time = next_free_time
            # If no waiting and no future meetings, we're done
            else:
                if not waiting and i >= total_meetings:
                    break
        
        # Find the room with the maximum number of meetings
        max_count = max(counts)
        for room in range(n):
            if counts[room] == max_count:
                return room
        return 0