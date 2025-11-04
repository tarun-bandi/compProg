class Solution:
    def update_cell(board_copy, x, y):

        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        live_neighbor_count = 0
        dead_neigbor_count = 0
        for dx, dy in deltas:
            if 0 <= x + dx < len(board_copy) and 0 <= y + dy < len(board_copy[0]):
                if board_copy[x + dx][y + dy]:
                    live_neighbor_count += 1
                else:
                    dead_neigbor_count += 1
        if board_copy[x][y] == 1 and live_neighbor_count == 2 or live_neighbor_count == 3:
            return 1
        if board_copy[x][y] == 1:
            return 0
        if board_copy[x][y] == 0 and live_neighbor_count == 3:
            return 1
        
        return 0
            


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] = Solution.update_cell(board_copy, i, j)
        
        return board
        

        