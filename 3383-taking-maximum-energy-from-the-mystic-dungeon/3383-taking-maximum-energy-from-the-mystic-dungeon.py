class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        

        @cache
        def dp(i: int):
            if i >= len(energy):
                return 0
            
            return dp(i + k) + energy[i]
        

        return max(dp(i) for i in range(0, len(energy)))