
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
    board_rows = [[board[0][0]+ board[0][1]+ board[0][2]+
                  board[0][3]+ board[0][4]+ board[0][5]+ board[0][6]],
                [board[1][0]+ board[1][1]+ board[1][2]+
                  board[1][3]+ board[1][4]+ board[1][5]+ board[1][6]],
                [board[0][0], board[0][1], board[0][2],
                  board[0][3], board[0][4], board[0][5], board[0][6]],
                [board[0][0], board[0][1], board[0][2],
                  board[0][3], board[0][4], board[0][5], board[0][6]],
                [board[0][0], board[0][1], board[0][2],
                  board[0][3], board[0][4], board[0][5], board[0][6]],
                [board[0][0], board[0][1], board[0][2],
                  board[0][3], board[0][4], board[0][5], board[0][6]],
                
                ]
    for  i in range(0,6): #check rows...
        if board[i].find(win_color) == -1:
            continue    #check next row

    for i in range(0,8): #check columns
        board_column = []    
        for y in range(0,6):
            board_column.append(board[y][i])
        if board_column.find(win_color) == -1:
            continue    #check next column
    
    #  check diagonals 6 + 6
    board_diag = [board[3][0], 
                board[2][1], 
                board[1][2],
                board[0][3]]  

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


