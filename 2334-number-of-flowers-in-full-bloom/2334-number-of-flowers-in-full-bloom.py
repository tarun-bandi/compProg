class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        BLOOM = 0
        WILT = 2
        OBSERVE = 1

        pq = []

        for (start, end) in flowers:
            heapq.heappush(pq, (start, BLOOM, -1))
            heapq.heappush(pq, (end, WILT, -1))
        
        for i, person in enumerate(people):
            heapq.heappush(pq, (person, OBSERVE, i))
        
        flower_ct = 0
        res = [0 for _ in range(len(people))]
        while pq:
            x, event_type, idx = heapq.heappop(pq)

            if event_type == BLOOM:
                flower_ct += 1
            elif event_type == WILT:
                flower_ct -= 1
            else:
                res[idx] = (flower_ct)
        
        return res





        