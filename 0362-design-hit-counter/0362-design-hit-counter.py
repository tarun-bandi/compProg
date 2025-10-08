class HitCounter:

    def __init__(self):
        self.hit_list = []
        

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.hit_list, timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hit_list and timestamp - self.hit_list[0] >= 300:
            heapq.heappop(self.hit_list)
        
        return len(self.hit_list)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)