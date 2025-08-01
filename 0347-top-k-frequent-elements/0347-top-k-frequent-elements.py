class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        
        total_len = 0
        res = []
        for i in range(len(nums), -1, -1):
            res.extend(buckets[i])
            total_len += len(buckets[i])
            if total_len == k:
                return res

            


