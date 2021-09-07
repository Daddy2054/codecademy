

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
    return ' ' + color + ' '

def validate_move():
    column = 10
    print("Enter column's number :")
    while (column < 1 or column > 7):
        column1 = input('enter 1-7 only: ')[0]
        if column1.isdigit():
            column = int(column1)
        else:    
            column = 0
            print('Wrong input!')
            #continue 
    return column

def check_row(board, column):
    for  i in range(0,6): #coin is dropping...
        if board[i][column -1] == ' _ ':
            continue
        else:
            if i == 0:
                print('Wrong input! The column {column} is full.'.format(column=column))
                #column = validate_move()
                #continue
                return -1
            else:
                i -= 1
                break # until it stops.
    return i    # row

def player_move(board, color):
    row = -1
    while row < 0:
        column = validate_move()
        row = check_row(board, column)
    
    board[row][column - 1] = color     # place coin
    display_board(board)

def you_win(board, color): #check if it is win move
    # 1.check rows 
    # 2. checks colums
    # 3. check diagonals 6 + 6
    win_color = color+color+color+color
    win_color = win_color.replace(' ','')
    board_rows = []
    for  i in range(0,6): #check rows...
        board_rows.append([board[i][0]+ board[i][1]+
                         board[i][2]+ board[i][3]+ 
                         board[i][4]+ board[i][5]+
                         board[i][6]])
    for i in range(0,6):  
        str1 = ''.join(board_rows[i]).replace(' ','')                    
        if str1.find(win_color) >= 0:
            return True

    board_columns = []    
    for i in range(0,7): #check columns
        board_columns.append([board[0][i]+ board[1][i]+
                         board[2][i]+ board[3][i]+ 
                         board[4][i]+ board[5][i]])
    for y in range(0,7):
        str1 = ''.join(board_columns[i]).replace(' ','')                    
        if str1.find(win_color) >= 0:
            return True

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
                board[3][4]+
                board[2][5]+
                board[1][6]])   # diag 5
    board_diags.append([board[5][3]+ 
                board[4][4]+
                board[3][5]+
                board[2][6]])   # diag 6
    board_diags.append([board[3][6]+ 
                board[2][5]+
                board[1][4]+
                board[0][3]]) # diag 1
    board_diags.append([board[4][6]+ 
                board[3][5]+
                board[2][4]+
                board[1][3]+
                board[0][2]])   # diag 2
    board_diags.append([board[5][6]+ 
                board[4][5]+
                board[3][4]+
                board[2][3]+
                board[1][2]+
                board[0][1]])   #diag3
    board_diags.append([board[5][5]+ 
                board[4][4]+
                board[3][3]+
                board[2][2]+
                board[1][1]+
                board[0][0]])   #diag 4
    board_diags.append([board[5][4]+ 
                board[4][3]+
                board[3][2]+
                board[2][1]+
                board[1][0]])   # diag 5
    board_diags.append([board[5][3]+ 
                board[4][2]+
                board[3][1]+
                board[2][0]])   # diag 6

    for y in range(0,13):
        str1 = ''.join(board_diags[i]).replace(' ','')                    
        if str1.find(win_color) >= 0:
            return True               
    return False                

def full_check(board):
    str1=board[0][0]+board[0][1]+board[0][2]+board[0][3]+board[0][4]+board[0][5]+board[0][6]
    if str1.find(' _ ') == -1:
        return True
    return False    

def again(): #replay again
    replay = '1'
    print('One more time?')
    while not(replay == 'Y' or replay == 'N'):
        replay = input('enter Y or N: ')[0].upper()
    if replay == 'Y':
        return True
    return False    

#print(pick_color())
while True:
    intro()
    p1_color = pick_color()
    if p1_color == ' X ':
        p2_color = ' O '
    else:     
        p2_color = ' X '
    p1_turn = True    
    in_game = True
    while in_game:
        if p1_turn:
            p1_turn = False
            display_board(board)
            print('Player 1 move:')
            player_move( board, p1_color)
            if you_win(board, p1_color):
                print('Player 1 WON!')
                break
        else:
            p1_turn = True
            display_board(board)
            print('Player 2 move:')
            player_move( board, p2_color)
            if you_win(board, p2_color):
                print('Player 2 WON!')
                break
        if full_check(board):
            print("It's tie!") 
            in_game = False

    if not again():
        print('Thank You for playing.')
        break

