class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def count_coin_change(index: int, amount: int):

            if amount == 0:
                return 1
            if index == len(coins):
                return 0
            
            ways_to_make = 0
            if coins[index] <= amount:
                take = count_coin_change(index, amount - coins[index])
                ways_to_make += take
            
            dont_take = count_coin_change(index + 1, amount)
            ways_to_make += dont_take
            return ways_to_make
        
        return count_coin_change(0, amount)
