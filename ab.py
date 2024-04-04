import numpy as np 

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
        print("Red's turn")
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
        print("Yellow's turn")
        # get the board length 
        n = len(new_board) 
        # print("N:", n) 
        # change the board
        # rannge n: 0 - 3 because n = 4
        col = np.random.randint(0, n) 
        row = np.random.randint(0, n) 
        # change one element of board to new move 
        new_board[col][row] = -1        
    print("new board:\n", new_board) 
    return new_board

def state_check(state): 
    # print("State:" , state) 
    # check if the game is won 
    # analyze all rows for four 1 or -1 
    # analyze all columns for four 1 or -1 
    # how do we do diagonals? start on a row and move in until you find 1 or -1
    # finding 1 or -1 determines which should be checked, then go to the next row 
    # on the next row, go one further than you went on the first row.... repeat until 4 hit 
    n = len(state) 
    for col in range(n): 
        for row in range(n):
            element = state[col][row] 
            element2 = state[row][col]
            # print("s1: ", element)
            # print("s2: ", element2) 

    '''
    # grab every column, in the case of a 4x4, 0-3 
    for col in range(n): 
        for row in range(n):
            # if -1 or 1 are found on the board
            # checks down, so this checks the columns.... 
            if(state[col][row] == -1 or state[col][row] == 1): 
                print("checking all columns") 
        
            if(state[row][col] == -1 or state[row][col] == 1): 
                print("checking all rows") 
        '''

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

# testing 

# create initial state 
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

    # yellow goes second 
    player = yellow 
    board = play(player, board)
    
    # for testing break 
    if(count < 3): 
        break; 
    
    # increment count 
    count+=1 



''' old imp 
min_max(); 
alpha_beta(); 
red = 1 
new_board = turn(red, board);

yellow = -1 
new_board = turn(yellow, new_board); 

state_check(new_board) 

# win_test = [1, 1, 1, 1] 

# state_check(win_test) 

'''
