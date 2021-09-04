
board2 = [[' 1',' 2',' 3',' 4',' 5',' 6',' 7'],
        [' 1',' 2',' 3',' 4',' 5',' 6',' 7'],
        [' 1',' 2',' 3',' 4',' 5',' 6',' 7'],
        [' 1',' 2',' 3',' 4',' 5',' 6',' 7'],
        [' 1',' 2',' 3',' 4',' 5',' 6',' 7'],
        [' 1',' 2',' 3',' 4',' 5',' 6',' 7']]

board = []
for i in range(0,6):
    board.insert(i, [' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ '])

def display_board(board):
    print('\n'*100)
    print('  1   2   3   4   5   6   7')
    for i in range(0,6):
        print('|'+board[i][0] + '|' +
            board[i][1] + '|' +
            board[i][2] + '|' +
            board[i][3] + '|' +
            board[i][4] + '|' +
            board[i][5] + '|' +
            board[i][6] + '|' )
def intro():
    print('Welcome in Connect Four game!\n')        
def pick_color():
    color = 'Y'
    print('Player 1 starts. Please, pick a color.')
    while not(color == 'X' or color == 'O'):
        color = input('enter X or O: ')[0].upper()
    return color
def validate_move():
    column = 10
    print("Enter column's number :")
    while (column > 0 and column < 8):
        column = input('enter 1-7 only: ')[0]
        if column.isalpha():
            column = 0
            print('Wrong input!')
            continue 
    return column

def check_row(board, column):
    i = 0
    for  i in range(0,6): #coin is dropping...
        if board[i][column -1] == ' _ ':
            continue
        else:
            break # until it stops.
    return i    # row

def player_move(board, color):
    column = validate_move()
    row = check_row(board, column)
    board[row][column] = color     # place coin
    display_board(board)

def you_win(board, color): #check if it is win move
    pass
    # 1.check rows 
    # 2. checks colums
    # 3. check diagonals 6 + 6
    win_color = [color,color,color,color]
    
    board_rows = []
    for  i in range(0,6): #check rows...
        board_rows.append([board[i][0]+ board[i][1]+
                         board[i][2]+ board[i][3]+ 
                         board[i][4]+ board[i][5]])
    for i in range(0,6):                      
        if board_rows[i].find(win_color) == -1:
            continue    #check next row

    board_columns = []    
    for i in range(0,8): #check columns
        board_columns.append([board[0][i]+ board[0][i]+
                         board[1][i]+ board[2][i]+ 
                         board[3][i]+ board[4][i]+
                         board[5][i]+ board[6][i]])
    for y in range(0,8):
        if board_columns.find(win_color) == -1:
            continue    #check next column
    
    #  check diagonals 6 + 6
    board_diags = []
    board_diags.append([board[3][0]+ 
                board[2][1]+
                board[1][2]+
                board[0][3]]) # diag 1
    board_diags.append([board[4][0]+ 
                board[3][1]+
                board[2][2]+
                board[1][3]+
                board[0][4]])   # diag2
    board_diags.append([board[5][0]+ 
                board[4][1]+
                board[3][2]+
                board[2][3]+
                board[1][4]+
                board[0][5]])   #diag3
    board_diags.append([board[5][1]+ 
                board[4][2]+
                board[3][3]+
                board[2][4]+
                board[1][5]+
                board[0][6]])   #diag 4
    board_diags.append([board[5][2]+ 
                board[4][3]+
                board[3][2]+
                board[2][1]+
                board[1][0]])   # diag 5
    board_diags.append([board[5][3]+ 
                board[4][1]+
                board[3][1]+
                board[2][2]+
                board[1][3]+
                board[0][4]])
    board_diags.append([board[4][0]+ 
                board[2][1]+
                board[1][2]+
                board[0][3]]) # diag 1
               
                
                

#print(pick_color())
while True:
    intro()
    p1_color = pick_color()
    if p1_color == 'X':
        p2_color = 'O'
    else:     
        p2_color = 'X'
    p1_turn = True    
    in_game = True
    while in_game:
        if p1_turn:
            p1_turn = False
            print('Player 1 move:')
            player_move( board, p1_color)


