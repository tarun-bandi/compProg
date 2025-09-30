import random

class RandomizedSet:

    def __init__(self):
        self.to_indexes = dict()
        self.items = []
        

    def insert(self, val: int) -> bool:
        if val in self.to_indexes:
            return False
        self.to_indexes[val] = len(self.items)
        self.items.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.to_indexes:
            return False
        index = self.to_indexes[val]
        last_item = self.items[len(self.items) - 1]
        self.items[index] = self.items[len(self.items) - 1]

        self.items.pop()
        self.to_indexes[last_item] = index
        del self.to_indexes[val]
        return True

    def getRandom(self) -> int:

        random_idx = random.randint(0, len(self.items) - 1)

        return self.items[random_idx]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()