'''
1. check input 
    a) if 'q' quit program
    b) if valid input (exclude str for example 'kk')/isnumeric?
    c) change input from str to int
    c) if range 1 -- 9
    d) check if position was taken

2. put player position on board

3. check winner & tie
    a) rows
    b) columns
    c) diagonals
    d) tie

4. switch player 

'''
########   Global variables    ########

game_continue = True

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

current_player = 'X'

winner = None

########  Functions    

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")

def check_input():
    global game_continue
    while game_continue:
        user_input = input('Enter your input (1 - 9) or press "q" to quit game :')
        if quit_game(user_input): 
            game_continue = False
            return
        if valid(user_input): continue
        user_input = int(user_input)
        if scope(user_input): continue
        else:
            user_input = user_input - 1 
        if board[user_input] == '-':
            board[user_input] = current_player
            return True
            break
        else:
            print('Position was taken!')
        
def quit_game(user_input):
    if user_input.lower() == 'q':
        print('Bye Bye')
        return True
    else:
        return False

def valid(user_input):
    if user_input.isnumeric():
        return False
    else:
        print('This is not valid number')
        return True

def scope(user_input):
    if user_input in range(1,10):
        return False
    else:
        print('Input is out of range!')
        return True

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

def rows():
    global game_continue
    row1 = board[0] == board[1] == board[2] !='-'
    row2 = board[3] == board[4] == board[5] !='-'
    row3 = board[6] == board[7] == board[8] !='-'
    if row1 or row2 or row3:
        game_continue = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    else:
        return None

def columns():
    global game_continue
    column1 = board[0] == board[3] == board[6] !='-'
    column2 = board[1] == board[4] == board[7] !='-'
    column3 = board[2] == board[5] == board[8] !='-'
    if column1 or column2 or column3:
        game_continue = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    else:
        return None

def diagonals():
    global game_continue
    diagonal1 = board[0] == board[4] == board[8] !='-'
    diagonal2 = board[2] == board[4] == board[6] !='-'
    if diagonal1 or diagonal2:
        game_continue = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    else:
        return None

def check_winner():
    global winner
    rows_winner = rows()
    columns_winner = columns()
    diagonals_winner = diagonals()
    if rows_winner:
        winner = rows_winner
    if columns_winner:
        winner = columns_winner
    if diagonals_winner:
        winner = diagonals_winner
    else:
        None

def check_if_game_over():
    check_winner()
    if winner == 'X' or winner == 'O':
        print('Winner is player', winner)
        play_again()
    else:
        check_tie()
    
def check_tie():
    if "-" not in board:
        print('Tie!')
        play_again()

def play_again():
    global game_continue
    global board
    global winner
    global current_player
    while True:
        again = input('Do you wanna play again? (y/n) ')
        if again.lower() == 'y':
            board = ['-', '-', '-',
                    '-', '-', '-',
                    '-', '-', '-']
            winner = None
            game_continue = True
            current_player = 'X'
            break
        else:
            game_continue = False
            break    

def play_game():
    display_board()
    while game_continue:
        check_input()
        display_board()
        flip_player()
        check_if_game_over()

play_game()



