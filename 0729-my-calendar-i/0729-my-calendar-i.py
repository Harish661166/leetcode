from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.start_events = SortedList()
        self.end_events = SortedList()

    def book(self, start: int, end: int) -> bool:
        left = bisect_right(self.end_events, start)
        right = bisect_left(self.start_events, end)
        if left == right:
            # add book
            self.start_events.add(start)
            self.end_events.add(end)
            return True
        else: return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)