class HitCounter:

    def __init__(self):
        self.hit_list = collections.deque()
        

    def hit(self, timestamp: int) -> None:
        self.hit_list.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hit_list and timestamp - self.hit_list[0] >= 300:
            self.hit_list.popleft()

        return len(self.hit_list)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)