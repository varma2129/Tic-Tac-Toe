from IPython.display import clear_output

board = [' ']*10
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-'+'-'+'-'+'-'+'-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'+'-'+'-'+'-'+'-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    
def player_marker():
    player1_marker = '_'
    while player1_marker not in ['X','O']:
        player1_marker = input('Enter the player1 marker(X or O): ')
    
    if player1_marker == 'X':
        player2_marker = 'O'
    else :
        player2_marker = 'X'
    return (player1_marker,player2_marker)
    
def player1_input():
    position = '0'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Player1 Enter the position(1-9): ')
    return int(position)
    
def player2_input():
    position = '0'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Player2 Enter the position(1-9): ')
    return int(position)
    
def replacing_values_player1(board,position):
    if board[position] == 'X' or board[position] == 'O':
        print('Sorry it is occupied already by player2')
    else:
        board[position] = 'X'
        
    return board
    
def replacing_values_player2(board,position):
    if board[position] == 'X' or board[position] == 'O':
        print('Sorry it is occupied already by player1')
    else:
        board[position] = 'O'
        
    return board
    
def check_winner(board,player1_marker,player2_marker):
    if board[1] == board[2] == board[3] == 'X' or board[4] == board[5] == board[6] == 'X' or board[7] == board[8] == board[9] == 'X' or board[1] == board[5] == board[9] == 'X' or board[3] == board[5] == board[7] == 'X' or board[1] == board[4] == board[7] == 'X' or board[3] == board[6] == board[9] == 'X' or board[5] == board[2] == board[8] == 'X':
        if player1_marker == 'X':
            print('Congratulations player1 is the winner')
            return True
        elif player2_marker == 'X':
            print('Congratulations player2 is the winner')
            return True
        else:
            return False
    elif board[1] == board[2] == board[3] == 'O' or board[4] == board[5] == board[6] == 'O' or board[7] == board[8] == board[9] == 'O' or board[1] == board[5] == board[9] == 'O' or board[3] == board[5] == board[7] == 'O' or board[1] == board[4] == board[7] == 'O' or board[3] == board[6] == board[9] == 'O' or board[5] == board[2] == board[8] == 'O':
        if player1_marker == 'O':
            print('Congratulations player1 is the winner')
            return True
        elif player2_marker == 'O':
            print('Congratulations player2 is the winner')
            return True
        else:
            return False
            
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))
    
def game_on_off():
    user_wish = '_'
    while user_wish not in ["Y","N"]:
        user_wish = input('Do You want to play again(Y or N): ')
        
    if user_wish == 'Y':
        return True
    else :
        return False
        
 def tie_check(board):
    tie = ' '
    for num in range(1,10):
        if board[num] == ' ':
            tie = False
            return False
            break
    if tie != False:
        return True
        
game_on = False

while game_on == False:
    clear_output()
    winner = False
    board =[' ']*10
    display_board(board)
    
    player1_mark,player2_mark = player_marker()
    
    while winner == False:
        
        index = player1_input()
        tie= ' '
        board = replacing_values_player1(board,index)
        display_board(board)
        winner = win_check(board,player1_mark)
        if winner == True:
            print('Congratulations player1 is the winner')
            break
        else:
            tie=tie_check(board)
            if tie == True:
                print('It is a tie game')
                break
                
              
       
        
        position = player2_input()
        board = replacing_values_player2(board,position)
        display_board(board)
        winner = win_check(board,player2_mark)
        if winner == True:
            print('Congratulations player1 is the winner')
            break
        else:
            tie=tie_check(board)
            if tie == True:
                print('It is a tie game')
                break
            
    
    
    game_on = not game_on_off()