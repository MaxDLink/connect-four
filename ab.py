import numpy as np 

# import sys for early exiting when game won 
import sys 

def board(): 
    # board_size = input("Enter board size(row, col): ")
    board_size = "4, 4" 
    rows_and_col = board_size.split(',') 

    # print("rows&Col:", rows_and_col) 

    # extract the split rows and columns 
    row = int(rows_and_col[0].strip())
    col = int(rows_and_col[1].strip()) 

    # print("row:", row) 
    # print("col:", col) 
    
    # list comprehension to make a board 
    # inner list: 0 for _ in range(cols) creates a list of 0's with length col
    # outer list: for _ in range(row) wraps this list, duplicating the list row times 
    # board = [[0 for _ in range(col)] for _ in range(row)] 
    # casts to float by default, so specify int with dtype
    board = np.zeros((row, col), dtype = int)  

    # display the board 
    # print("board:\n", board)
    # return the board 
    return board

# function for min_max to determine value of nodes 
def utility(): 
    print("running utility") 
    # print("node value is...") 

def min_max(): 
    print("min_max algo running")
    utility()

def alpha_beta(): 
     print("alpha beta pruning running") 

def turn(player, board):
    # yellow is -1 
    # red is 1 
    # make a copy of board 
    new_board = board.copy() 

    if player == 1: 
        # print("Red's turn")
        # get the board length 
        n = len(new_board) 
        # print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        new_board[col][row] = 1        
    else: 
        # print("Yellow's turn")
        # get the board length 
        n = len(new_board) 
        # print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        new_board[col][row] = -1        
    # print("new board:\n", new_board) 
    return new_board

def col_checker(board): 
    # initialize state to 0 because the game by default is not won 
    state = 0 
    # get the length of the board
    # for 4x4 should be 4 becauase len takes the vertical length 
    n = len(board)
    # empty list for holding found column   
    column = [] 
    # generate comparison array of 1's 
    # dynamic array allocation with n 
    # win state changes based on player 
    # n is the amount of columns, filling each column with only a single 1 to make a 1 row 
    # np.ones makes a matrix by default so index at 0 to just get one array for our comparison  
    win_state1 = np.ones((1, n), dtype = int) 
    #print("W1: \n", win_state1[0]) 
    # negative win state
    # np.full makes a matrix by default so we must index at 0 to just get one array for our comparison 
    win_state2 = np.full((1, n), -1) 
    #print("W2:\n", win_state2[0])  
    # check every row of the board 
    # 0-3 range for row
    for col in range(len(board)):
        # print("test_set column: \n", board[col][0])
        # holds the entire column in a column string 
        # builds up as loop is iterated 
        column += [board[col][0]]
        # print("col win state: ", win_state1) 
        # print(board[col][0])
    # print found column for testing 
    print("col array: ", column) 
    # use np.array_equal to compare arrays
    if(np.array_equal(column, win_state1[0]) or np.array_equal(column, win_state2[0])): 
            # print("entered if!") 
            state = 1  
    return state 

# finds column 
# need to rename 
def row_checker(board):

    # real logic 
    # initialize state to 0 because the game by default is not won 
    state = 0 
    # get the length of the board
    # for 4x4 should be 4 becauase len takes the vertical length 
    n = len(board)
    
    # get the shape of board 
    # r is the length of the rows on the board 
    r = board.shape[1]
    # print('r:', r) 
    # generate comparison array of 1's 
    # r is for dynamic array of 1 allocation based on board size 
    # r is the amount of columns, filling them with 1's
    # np.ones defaults to making a matrix, so to get a single array we will have to index 0 
    win_state1 = np.ones((1, r), dtype = int)
    # negative win state 
    # np.full for general fill 
    # np.full defaults to making a matrix, so to get a single array we will have to index 0 
    win_state2 = np.full((1, r), -1) 
    # print("win_state:", win_state) 
    # check every row of the board 
    # 0-3 range for row 
    for row in range(n): 
        # print("this is the row being compared: \n", board[row])
        # print("win state:\n ", win_state1[0])
        # if the game is won, set state to 1 
        # compare using np.array_equal to compare each element of the arrays to each other 
        # if they are equal enter the if statement 
        # this may not be okay to compare arrays directly. 
        # if state is not one 
        if(np.array_equal(board[row], win_state1[0]) or np.array_equal(board[row], win_state2[0]) and state != 1):
            # print("state updated!") 
            state = 1 
            # print("State: ", state) 

    return state 

# diagonal check 
def diagonal_check(board, player): 
    print("checking diagonals") 
    n = len(board) 
    for row in range(n):
        # check if the row contains 1 or -1 
        if 1 or -1 in row:
            # exit the for
            print("found the first 1, exiting loop") 
            break
        row = board[row]
        print("row: \n", row) 

def state_check(board, player): 
    # starting values for terminal condition 
    # start as 0 because no one has won the game yet 
    # 1 when game won 
    state_row = 0 
    state_col = 0 
    # print("State:" , state) 
    # check if the game is won 
    # analyze all rows for four 1 or -1 
    # analyze all columns for four 1 or -1 
    # how do we do diagonals? start on a row and move in until you find 1 or -1
    # finding 1 or -1 determines which should be checked, then go to the next row 
    # on the next row, go one further than you went on the first row.... repeat until 4 hit
    # check rows - works  
    ##state_row = row_checker(board) 
    # check columns 
    ##state_col = col_checker(board)
    # check diagonal 
    diagonal_check(board, player) 

    if(state_row == 1 or state_col == 1): 
        print("player: ", player, " won! Ending game.")
        # exit the program because the game has been won 
        # sys.exit()
        print("pretend sys.exit(). Reenable sys.exit() after testing!") 
    else: 
        print("win state not reached") 

def play(player, board): 
    if(player == 1): 
        print("red is playing on board.")
        # get the board length 
        n = len(board) 
        # print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        board[col][row] = 1        

    else: 
        print("yellow is playing on board.")
        # get the board length 
        n = len(board) 
        # print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        board[col][row] = -1 
    # for testing 
    print("Updated board: \n", board)
    return board 


# test 
board = board();
print("board:\n", board)

# explanatory variables 
red = 1 
yellow = -1 

# for testing to break while loop 
count = 0 
# while loop - game logic 
while True:
    # red goes first 
    player = red 
    board = play(player, board)
    
    # check state - state_check will end the game if a disc is in four adjacent spots 
    state_check(board, player)

    # yellow goes second 
    player = yellow 
    board = play(player, board)

    # check state - state_check will end the game if a disc is in four adjacent spots 
    state_check(board, player) 
    
    # for testing break 
    if(count == 5): 
        break; 
    
    # increment count 
    count+=1

player = 1 
print("checking diagonals")
arr = [[1, 0, 0, 0],
       [0, 1, 0, 0]]
diagonal_check(arr, player); 
# test win condition here
# all encompassing check for win conditions 
# testing for rows 
'''
player = 1 
test_win = np.array([[1, 0, 0, 0], 
                     [0, 1, 0, 0]]) 
print("testing array \n: ", test_win) 
state_check(test_win, player) 

# player 2 
player = -1 
test_win = np.array([[-1, 0, 0, 0], 
            [0, 0, 0, 0]])  
print("testing array \n: ", test_win) 
state_check(test_win, player) 
'''
