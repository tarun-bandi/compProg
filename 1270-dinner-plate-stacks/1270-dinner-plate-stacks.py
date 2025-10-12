class DinnerPlates:

    def __init__(self, capacity: int):
        self.queue = []
        self.c = capacity
        self.emp = [] #non-full stacks, if the same index appears twice, that means it has two empty positions in this stack.

    def push(self, val: int) -> None:
        if self.emp:
            l = heapq.heappop(self.emp)
            if l < len(self.queue): #in some cases, the pop is called too many times, and the queue is shorter than the index
                self.queue[l] += [val]
                return
            else: self.emp = []
        if len(self.queue)>0 and len(self.queue[-1]) < self.c:
            self.queue[-1] += [val]
            return
        self.queue += [[val]]
        #print(self.queue)

    def pop(self) -> int:
        while len(self.queue) > 0 and not self.queue[-1]:
            self.queue.pop()
        if self.queue:
            res = self.queue[-1][-1]
            self.queue[-1].pop()
            return res
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.queue) and len(self.queue[index]) > 0:
            res = self.queue[index][-1]
            self.queue[index].pop()
            heapq.heappush(self.emp,index)
            return res
        return -1