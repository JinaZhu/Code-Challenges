# Game of Life
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

def game_of_life(board):

    def check_neighbor_helper(i, j):
        live_neighbors = 0
        
        for row_position in (-1, 0, 1):
            for col_position in (-1, 0, 1):
                if row_position == 0 and col_position == 0:
                    continue
                neighbor_i = i + row_position
                neighbor_j = j + col_position
                
                if 0 <= neighbor_i < len(board) and 0 <= neighbor_j < len(board[0]):
                    if board[neighbor_i][neighbor_j] == 1:
                        live_neighbors += 1
        return live_neighbors
    
    changes = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            total_live_neighbors = check_neighbor_helper(i, j)
            current_cell = board[i][j]
            
            if current_cell == 1:
                if total_live_neighbors < 2 or total_live_neighbors > 3:
                    changes.append([0, i, j])
            else:
                if total_live_neighbors == 3:
                    changes.append([1, i, j])
    
    for change in changes:
        board[change[1]][change[2]] = change[0]

    return board

game_of_life_testcase = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game_of_life_result = game_of_life(game_of_life_testcase)
game_of_life_game_test = game_of_life_result == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print('game_of_life_game_test', game_of_life_game_test)