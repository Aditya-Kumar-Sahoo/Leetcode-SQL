class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        selected_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            selected_capacity += cap
            boxes_used += 1
            if selected_capacity >= total_apples:
                break
        
        return boxes_used