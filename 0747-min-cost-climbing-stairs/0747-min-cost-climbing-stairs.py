class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def find_cost_from_stair(i: int) -> int:
            if i >= len(cost):
                return 0
            
            return min(find_cost_from_stair(i + 1), find_cost_from_stair(i + 2)) + cost[i]
        
        return min(find_cost_from_stair(0), find_cost_from_stair(1))
