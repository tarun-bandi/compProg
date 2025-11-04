class Solution:

    def __init__(self, w: List[int]):
        prefix_summed = [0 for _ in range(len(w))]
        total_sum = sum(w)
        previous_prob = 0
        for i, weight in enumerate(w):
            prefix_summed[i] = previous_prob + weight/total_sum 
            previous_prob = prefix_summed[i]
        print(prefix_summed)
        self.prefix_summed = prefix_summed
        

    def pickIndex(self) -> int:
        probability = random.uniform(0, 1)
        index = bisect.bisect_left(self.prefix_summed, probability)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()