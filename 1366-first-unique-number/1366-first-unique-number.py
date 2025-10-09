class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = collections.deque()
        self.counts = dict()

        for n in nums:
            self.q.append(n)
            self.counts[n] = self.counts.get(n, 0) + 1
        
        while self.q and self.counts[self.q[0]] > 1:
            self.q.popleft()

        

        

    def showFirstUnique(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q[0]
        

    def add(self, value: int) -> None:
        self.counts[value] = self.counts.get(value, 0) + 1
        self.q.append(value)
        
        while self.q and self.counts[self.q[0]] > 1:
            self.q.popleft()

        return
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)