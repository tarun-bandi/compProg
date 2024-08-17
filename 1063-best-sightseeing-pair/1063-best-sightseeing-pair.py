class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        prev_max = values[0]
        prev_index = 0

        total_max_score = 0
        for i in range(1, len(values)):
            curr_value = values[i]

            total_max_score = max(total_max_score, prev_max + curr_value - i + prev_index)

            if curr_value > prev_max - abs(prev_index - i):
                prev_index = i
                prev_max = curr_value
        
        return total_max_score

        