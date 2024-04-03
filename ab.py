import numpy as np 

def board(): 
    board_size = input("Enter board size(row, col): ")

    rows_and_col = board_size.split(',') 

    print("rows&Col:", rows_and_col) 

    # extract the split rows and columns 
    row = int(rows_and_col[0].strip())
    col = int(rows_and_col[1].strip()) 

    print("row:", row) 
    print("col:", col) 
    
    # list comprehension to make a board 
    
    board = np.zeros((row, col))  

    # display the board 
    print("board:\n", board)
    # return the board 
    return board

def min_max(): 
    print("min_max algo running")


def alpha_beta(): 
    print("alpha beta pruning running") 

def turn(player, board):
    # yellow is -1 
    # red is 1 
    # make a copy of board 
    new_board = board.copy() 

    if player == 1: 
        print("Red's turn")
        # get the board length 
        n = len(new_board) 
        print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        new_board[col][row] = 1        
    else: 
        print("Yellow's turn")
        # get the board length 
        n = len(new_board) 
        print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        new_board[col][row] = -1        
    print("new board:\n", new_board) 
    return new_board

    


# testing 
board = board();
min_max(); 
alpha_beta(); 
red = 1 
new_board = turn(red, board);

yellow = -1 
new_board = turn(yellow, new_board); 
