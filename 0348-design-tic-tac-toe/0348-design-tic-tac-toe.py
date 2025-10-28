class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 2 else -1

        self.rows[row] += current_player
        self.cols[col] += current_player

        if (row == col):
            self.diagonal += current_player
        
        if (col + row == (len(self.cols) - 1)):
            self.anti_diagonal += current_player
        
        if (abs(self.rows[row])== len(self.cols) or abs(self.cols[col]) == len(self.cols) or 
        abs(self.diagonal) == len(self.cols) or abs(self.anti_diagonal) == len(self.cols)):
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)