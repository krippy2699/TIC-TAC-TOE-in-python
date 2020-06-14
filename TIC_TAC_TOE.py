Python.display import clear_output
def draw_board(board):
    clear_output()
    print('|  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2] + '  | ')
    print('|  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5] + '  | ')
    print('|  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8] + '  | ')

def user_name():
    name1 = input('Player#1 name: ')
    name2 = input('Player#2 name: ')
    return (name1,name2)

import random
def pick_XO():
    player = random.randint(1,2)
    if player==1:
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
        
    return (player1,player2)

def input_on_board(test_board,position,choice):
    test_board[position] = choice
    return test_board

def input_check(test_board,position):
    
    if test_board[position]=='_':
        available = True
    else:
        available = False
    
    return available

def winner_logic(board):
    X_won = False
    O_won = False
    neither_wins = True
    
    #horizontally 
    if board[0]=='X' and board[1]=='X' and board[2]=='X':
        X_won = True
        neither_wins = False
    elif board[3]=='X' and board[4]=='X' and board[5]=='X':
        X_won = True
        neither_wins = False
    elif board[6]=='X' and board[7]=='X' and board[8]=='X':
        X_won = True
        neither_wins = False
    #vertically
    elif board[0]=='X' and board[3]=='X' and board[6]=='X':
        X_won = True
        neither_wins = False
    elif board[1]=='X' and board[4]=='X' and board[7]=='X':
        X_won = True
        neither_wins = False
    elif board[2]=='X' and board[5]=='X' and board[8]=='X':
        X_won = True
        neither_wins = False
    #diagnolly
    elif board[0]=='X' and board[4]=='X' and board[8]=='X':
        X_won = True
        neither_wins = False
    elif board[2]=='X' and board[4]=='X' and board[6]=='X':
        X_won = True
        neither_wins = False

        
     #horizontally 
    if board[0]=='O' and board[1]=='O' and board[2]=='O':
        O_won = True
        neither_wins = False
    elif board[3]=='O' and board[4]=='O' and board[5]=='O':
        O_won = True
        neither_wins = False
    elif board[6]=='O' and board[7]=='O' and board[8]=='O':
        O_won = True
        neither_wins = False
    #vertically
    elif board[0]=='O' and board[3]=='O' and board[6]=='O':
        O_won = True
        neither_wins = False
    elif board[1]=='O' and board[4]=='O' and board[7]=='O':
        O_won = True
        neither_wins = False
    elif board[2]=='O' and board[5]=='O' and board[8]=='O':
        O_won = True
        neither_wins = False
    #diagnolly
    elif board[0]=='O' and board[4]=='O' and board[8]=='O':
        O_won = True
        neither_wins = False
    elif board[2]=='O' and board[4]=='O' and board[6]=='O':
        O_won = True
        neither_wins = False
        

    return (X_won,O_won,neither_wins)

print('--- TIC TAC TOE ---')

grid = ['_','_','_','_','_','_','_','_','_']

player1,player2 = user_name()
p1,p2 = pick_XO()
X_won = False
O_won = False
neither_won = True
i = 0
input1 = ''
input2 = ''
cell_check = False
#p1 and p2 are the values assiged to the players, whether their X or O

print(f' * {player1} is {p1}')
print(f' * {player2} is {p2}')
print(f'{player1} goes first !')


while(neither_won==True):
    X_won, O_won, neither_won = winner_logic(grid)
    #player1's input
    input1 = input(f'Enter position for {p1}: ')
    while(input1.isdigit()==False or int(input1)<0 or int(input1)>9):
        input1 = input(f'Please enter a valid position for {p1} from 0-9: ')
    
    #checking if the cell entered is occupied or vacant
    cell_check = input_check(grid,int(input1)-1)
    if cell_check==True:
        input_on_board(grid,int(input1)-1,p1)
        draw_board(grid)
    else:
        while(cell_check!=True):
            print('Cell taken. Enter another position: ')
            input1 = input(f'Enter position for {p1}: ')
            cell_check = input_check(grid,int(input1)-1)
            if cell_check==True:
                input_on_board(grid,int(input1)-1,p1)
                draw_board(grid)
                continue
    X_won,O_won,neither_won = winner_logic(grid)
    if X_won==True:
        if p1=='X':
            print(f'Congratulations {player1}, you won !')
            break
        elif p2=='O':
            print(f'Congratulations {player2}, you won !')
            break;
    i+=1
    if i==9 and neither_won==True:
        break
        
    
#player2's input
    input2 = input(f'Enter position for {p2}: ')
    while(input2.isdigit()==False or int(input2)<0 or int(input2)>9):
            input2 = input(f'Please enter a valid position for {p2} from 0-9: ')
    cell_check = input_check(grid,int(input2)-1)
    if cell_check==True:
        input_on_board(grid,int(input2)-1,p2)
        draw_board(grid)
    else:
        while(cell_check!=True):
            print('Cell taken. Enter another position: ')
            input2 = input(f'Enter position for {p2}: ')
            cell_check = input_check(grid,int(input2)-1)
            if cell_check==True:
                input_on_board(grid,int(input2)-1,p2)
                draw_board(grid)
                continue
    X_won,O_won,neither_won = winner_logic(grid)            
    if X_won==True:
        if p1=='X':
            print(f'Congratulations {player1}, you won !')
            break
        elif p2=='O':
            print(f'Congratulations {player2}, you won !')
            break;
    i+=1
    if(i==9 and neither_won==True):
        break
    
    
print(f'{player1} and {player2}, you guys are evenly matched ! A TIE !')
    








