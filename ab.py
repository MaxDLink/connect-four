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
    print(board)
    # return the board 
    return board

def min_max(): 
    print("min_max algo running")


def alpha_beta(): 
    print("alpha beta pruning running") 

def turn(player, board):
    # yellow is -1 
    # red is 1 
    if player == 1: 
        print("Red's turn") 
    else: 
        print("Yellow's turn") 
    


# testing 
board = board();
min_max(); 
alpha_beta(); 
red = 1 
turn(red, board); 
