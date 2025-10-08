class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        
    
    def check_row(self, row):
        board_row = self.board[row]
        first = board_row[0]
        
        if first == 0:  # Bug fix: check if first cell is empty
            return None

        for b in board_row:
            if first != b:
                return None
            
        return first

    def check_col(self, col):
        first = self.board[0][col]
        
        if first == 0:  # Bug fix: check if first cell is empty
            return None

        for i in range(len(self.board)):
            if first != self.board[i][col]:
                return None
            
        return first

    def check_diag(self):
        first = self.board[0][0]
        
        if first == 0:  # Bug fix: check if first cell is empty
            return None
            
        for i in range(len(self.board)):
            if first != self.board[i][i]:
                return None
    
        return first

    def check_anti(self):
        n = len(self.board)
        first = self.board[0][n - 1]  # Bug fix: was n - 1 instead of n
        
        if first == 0:  # Bug fix: check if first cell is empty
            return None
            
        for i in range(len(self.board)):
            anti = n - 1 - i
            if first != self.board[i][anti]:
                return None
    
        return first



    def check_board(self, row, col):
        res_row = self.check_row(row)
        if res_row:
            return res_row
        
        res_col = self.check_col(col)
        if res_col:
            return res_col


        diagonal = self.check_diag()
        if diagonal:
            return diagonal
        
        anti_diag = self.check_anti()
        return anti_diag


    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        result = self.check_board(row, col)
        return result if result else 0  # Bug fix: return 0 if no winner