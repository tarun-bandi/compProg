class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake = collections.deque([(0, 0)])
        self.food = collections.deque(food)
        self.score = 0
    def move(self, direction: str) -> int:
        match direction:
            case "R":
                dx, dy = (0, 1)
            case "L":
                dx, dy = (0, -1)
            case "D":
                dx, dy = (1, 0)
            case "U":
                dx, dy = (-1, 0)
        

        # Move snake
        x, y = self.snake[0]
        new_head = (x + dx, y + dy)
        self.snake.appendleft(new_head)
        
        if len(self.food)!= 0 and self.snake[0] == tuple(self.food[0]):
            self.score += 1 # Use a variable for modularity (Might not be len in future)
            self.food.popleft()
        else:
            self.snake.pop()


        head_x, head_y = self.snake[0]
        # Out of bounds check
        if head_x < 0 or head_x >= self.height or head_y < 0 or head_y >= self.width:
            return -1
        
        # Check if head in body

        if len(self.snake) != len(set(self.snake)): # Can be optimized
            return -1
        
        return self.score




        

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)