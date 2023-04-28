import piece_movement as pm
import board as bd
king = bd.king


def rules_check(B, PlayerMove):
    judjement = move_check(B,PlayerMove) and king_wellness_move(B,PlayerMove)
    return judjement
    input()
    
def move_check(B,PlayerMove):
    pos_in = PlayerMove[0]
    pos_fi = PlayerMove[1]
    piece = B[pos_in[0],pos_in[1]]
    if (pos_fi in pm.possible_pos_piece(piece,pos_in, B)):
        return True
    else:
        print('')
        print("-Impossible Move")
        print('')
        return False
def king_wellness(B):
    dim = len(B)
    for minion in pm.my_piece_list(B):
        if minion[0]== king:
            pos = [minion[1],minion[2]]
            B2 = bd.board_transf(B)
            pos[0] = dim-1 - pos[0]
            pos[1] = dim-1 - pos[1]
            for enemy in pm.my_piece_list(B2):
                for new_pos in pm.possible_pos_piece(enemy[0],[enemy[1],enemy[2]],B2) :
                    if new_pos[0] == pos[0]  and  new_pos[1] == pos[1] :
                        #print('-king under attack, movement not allowed')
                        return False
                        
    return True      
    
def king_wellness_move(B,PlayerMove):
    B2 = B * 1
    B2 = move(PlayerMove[0],PlayerMove[1],B2)
    return king_wellness(B2)
    

def move(pos1,pos2,B):
    B[pos2[0],pos2[1]] = B[pos1[0],pos1[1]]
    B[pos1[0],pos1[1]] = 0
    return B

def my_minion_in_danger(B):
    minion_list = []
    pos = [0,0]
    dim = len(B)
    for minion in pm.my_piece_list(B):
        pos[0] = dim-1 -minion[1]
        pos[1] = dim-1 -minion[2]
        B2 = pm.board_transf(B)
        for enemy in pm.my_piece_list(B2):
            for new_pos in pm.possible_pos_piece(enemy[0],[enemy[1],enemy[2]],B2) :
                if new_pos == pos :
                    minion_list += [minion]
                    
    return minion_list




def end_check(B) :
    B = pm.board_transf(B)
    for piece in pm.my_piece_list(B) :
        pos = [piece[1],piece[2]]
        poss_piece = pm.possible_pos_piece(piece[0],pos, B)
        if poss_piece != []:
            for new_pos in poss_piece:
               # print(king_wellness(B),poss_piece)
                if king_wellness_move(B,[pos,new_pos]) :
                    return 0 
    if  king_wellness(B) :
         return 2
    return 1