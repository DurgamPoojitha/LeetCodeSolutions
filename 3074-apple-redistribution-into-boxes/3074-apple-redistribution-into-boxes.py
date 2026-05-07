class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)

        # Use largest boxes first
        capacity.sort(reverse=True)

        boxes = 0
        current_capacity = 0

        for cap in capacity:
            current_capacity += cap
            boxes += 1

            if current_capacity >= total_apples:
                return boxes