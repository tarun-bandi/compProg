class FoodRatings:
    """
    V0: Simple design where we can just have each cuisine map to a list of the foods in the cuisine. Then if we want the highest rated for that cuisine look at each of the things within the cuisine.

    V1: Make this a heap. Everytime you want an update, we can reheapify
    V2: Lazy deletion. State: food to version_num. cuisine to food_heap. Food_heap is a heap with (rating, food, version_num). If version_num != cuisine[food], pop it when we try to get the highest_rated. 
    """
    def __init__(self, foods: list[str], cuisines: List[str], ratings: List[int]):
        self.food_to_version_num: Dict[str, int] = dict()
        self.food_to_cuisine = dict()
        for food in foods:
            self.food_to_version_num[food] = 0
        
        
        self.cuisine_to_ordered_foods = dict()
        n = len(foods)

        for i in range(n):
            # initialize
            self.cuisine_to_ordered_foods[cuisines[i]] = self.cuisine_to_ordered_foods.get(cuisines[i], [])

            cuisine_heap = self.cuisine_to_ordered_foods[cuisines[i]]
            # Add to the heap
            heapq.heappush(cuisine_heap, (-ratings[i], foods[i], 0))
            self.food_to_cuisine[foods[i]] = cuisines[i]
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]

        ordered_foods = self.cuisine_to_ordered_foods[cuisine] 
        version = self.food_to_version_num[food]
        heapq.heappush(ordered_foods, (-newRating, food, version + 1))
        self.food_to_version_num[food] = version + 1
        

    def highestRated(self, cuisine: str) -> str:
        ordered_foods = self.cuisine_to_ordered_foods[cuisine] 
        
        while ordered_foods and self.food_to_version_num[ordered_foods[0][1]] != ordered_foods[0][2]:
            heapq.heappop(ordered_foods)
        
        return ordered_foods[0][1]


        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)