class SeatManager:
    def __init__(self, n: int):
        self.smallest = 1
        self.avail_seats = []
        
    def reserve(self) -> int:
        if self.avail_seats:
            return heapq.heappop(self.avail_seats)
        else:
            reserved = self.smallest
            self.smallest += 1
            return reserved

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.avail_seats, seat_number)