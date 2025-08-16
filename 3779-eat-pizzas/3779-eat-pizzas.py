class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:

        pizza_ct = len(pizzas) / 4 

        odd_days = math.ceil(pizza_ct / 2)
        even_days = pizza_ct // 2
        # print(f"Odd days: {odd_days}, Even days: {even_days}")
        total_weight = 0
        i = len(pizzas) - 1
        pizzas.sort()
        while i > 0:
            if odd_days != 0:
                odd_days -= 1
                # print(f"Adding {pizzas[i]} on odd turn")
                total_weight += pizzas[i]
            elif even_days != 0:
                i -= 1
                total_weight += pizzas[i]
                even_days -= 1
                # print(f"Adding {pizzas[i]} on even turn")
            i -= 1
        return total_weight

        