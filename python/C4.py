
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
    for  i in range(0,6):
        if board[i][column -1] == ' _ ':
            continue
        else:
            break
    return i    # row

def player_move(board):
    column = validate_move()
    row = check_row(board, column)
    # place coin

#display_board(board)
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


