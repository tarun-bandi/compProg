class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        game_over = False
        m = len(board)
        n = len(board[0])

        number_of_touching_mines = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        mines = set()

        # Finding all the mines
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "M":
                    mines.add((i, j))
        
        # Setting up the board
        for (i, j) in mines:
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    number_of_touching_mines[x][y] += 1
        
        for x in range(m):
            for y in range(n):
                adjacent_mines = number_of_touching_mines[x][y]
                if adjacent_mines == 0:
                    number_of_touching_mines[x][y] = 'B'
                else:
                    number_of_touching_mines[x][y] = str(adjacent_mines)
        

        def uncover_adjacent_mines(i, j, seen):
            
            for dx, dy in dirs:
                x = i + dx
                y = j + dy

                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    board[x][y] = number_of_touching_mines[x][y] 
                    seen.add((x, y))
                    if board[x][y] == "B":
                        uncover_adjacent_mines(x, y, seen)

        # Simulate game
        i = 0

        while i < len(click):
            r, c = click[i], click[i + 1]
            i += 2
            if board[r][c] == "M":
                board[r][c] = "X"
                break

            board[r][c] = number_of_touching_mines[r][c]

            if board[r][c] == "B":
                uncover_adjacent_mines(r, c, {(r, c)})

        
        return board
                








        