class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        

        spell_counts = list(Counter(power).items())
        spell_counts.sort()
        @cache
        def dp(i: int):
            if i >= len(spell_counts):
                return 0
            
            power, count = spell_counts[i]
            power_change = power * count
            next_power = power + 3

            new_index = bisect.bisect(spell_counts, (next_power, 0))
            return max(dp(i + 1), power_change + dp(new_index))
        
        return dp(0)
        