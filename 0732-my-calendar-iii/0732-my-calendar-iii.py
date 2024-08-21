from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.diff = SortedDict()

    def book(self, start_time: int, end_time: int) -> int:
        self.diff[start_time] = self.diff.get(start_time, 0) + 1
        self.diff[end_time] = self.diff.get(end_time, 0) - 1
        
        current = 0
        max_booking = 0
        for cnt in self.diff.values():
            current += cnt
            max_booking = max(max_booking, current)
        
        return max_booking