import visual as vs
import board as bd
import chess_rules as cr
#import epaminonda21 as co
import epaminonda19_canc as co2
import human as hu
pawn = 10 
bishop = 70  
knight = 71  
tower = 90  
queen = 120   
king = 4000 
dim = 8

B = bd.BoardGen(dim)
computer1 = 'Epaminonda'
computer2 = 'Epaminonda(2)'
human1 = 'Challenger'
human2 = 'Challenger2'

white = human1 
black = computer2

rounds = 30

def player_move(color,B) :
    if color == computer1 :
        return co2.PlayerMove(B)
    elif color == computer2 :
        return co2.PlayerMove(B)
    elif color == human1 :
        return hu.PlayerMove(B)
    elif color == human2 :
        return hu.PlayerMove(B)

#---------------------------------------------------------------
#programma

vs.welcome(B)
B = bd.board_transf(B)
for turn in range(rounds):
    vs.turn_information(turn)
    if white == human1 or  white == human2  :
        print(white,' is your turn ')  
        print('')      
    test = True
    while test :
        white_move = player_move(white,B)  
        if cr.rules_check(B, white_move):
            vs.nice_info_white(white,white_move,B)
            B = bd.UpdateBoard(B, white_move)
            test = False
        else :
            if white == computer1 or  white == computer2  :
                break 
    vs.nice_board(bd.board_transf(B)) 
    print('')
    if cr.end_check(B) == 1:
        print('The winner is ',white)
        print('')
        break
    elif cr.end_check(B) == 2 :
        print('Draw')
        print('')
        break
        
    print('')
    B = bd.board_transf(B)
    if black == human1 or  black == human2  :
        print(black,' is your turn ')
        print('')
    test = True
    while test :
        #print(3)
        black_move = player_move(black,B)
       # print(55)
        if black == human1 or black == human2  :
            for i in range(2):
                black_move[0][i] = dim-1 - black_move[0][i]
                black_move[1][i] = dim-1 - black_move[1][i]
        if cr.rules_check(B, black_move):
           B2 = B*1
           B = bd.UpdateBoard(B, black_move)
           vs.nice_info_black(black,black_move,B2)
           test = False
        else :
             if black == computer1 or black == computer2 :
                 break  

    B2 = B*1
    vs.nice_board(B)
    B = bd.board_transf(B)
    print('')
    if cr.end_check(B2) == 1:
        print('The winner is ',black)
        print('')
        break
    elif cr.end_check(B2) == 2 :
        print('Draw')
        print('')
        break         

