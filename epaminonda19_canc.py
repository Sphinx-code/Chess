import numpy as np

pawn = 10 
bishop = 70  
knight = 71  
tower = 90  
queen = 120   
king = 4000 

def PlayerMove(B) :
    depth = 1
    best_piece_p = best_piece_pos(B,depth)*1    
    b_move = best_move_piece(B[best_piece_p[0],best_piece_p[1]],best_piece_p, B,depth)
    new_pos = b_move[1]
    best_move = [best_piece_p, new_pos]
    return best_move 


def best_piece_pos(B,depth):
    best_piece = -99999999
    best_pos = []
    for minion in my_piece_list(B) :
      
        piece = B[minion[1],minion[2]]
        temp_piece = best_move_piece(piece,[minion[1],minion[2]], B,depth)[0] 
        if temp_piece > best_piece :
            best_piece = temp_piece
            best_pos = [minion[1],minion[2]]
    return  best_pos


def best_move_piece(piece,pos, B,depth):
    best_movement = [-99999999, []]
    list_pos = possible_pos_piece(piece,pos,B)
    if list_pos == [[]]:
        return -999999999
    for new_pos in list_pos:
        if not king_wellness_move(B,[pos,new_pos]) :
            continue
        quality_move = 0
        quality_move = quality_move + dif_value_tot(pos,new_pos,B,depth)
        
        if quality_move > best_movement[0] :
            best_movement = [quality_move, new_pos]
            
    return best_movement

def dif_value_tot(pos1,pos2,B,depth) :
    B2 = B*1
    my_dif = dif_value_player(pos1,pos2,B2,depth)
   # B3  = B2*1
   # B3 = invert_board(B2)
   # dim = len(B)
   # pos1_inv = invert_pos(pos1,dim)
   # pos2_inv = invert_pos(pos2,dim)
   # enemy_dif = dif_value_player(pos1_inv,pos2_inv,B3,depth)
    return my_dif 


def dif_value_player(pos1,pos2,B,depth):
    val1 = value_player(B,depth)
    B2 = B*1
    B2 = move(pos1,pos2,B2)
    val2 = value_player(B2,depth)
    return val2-val1


def value_player(B,depth):
    a = 1
    b = 1
    c = 1
    d = 1
    e = 2
    value =  e*function_val(B,depth)+np.sum(B)*d + a*value_mid_control(B)+ b*value_protect(B)+ c*board_control(B)    
    return value  



def function_val(B,depth):
    dim = len(B)
    val = 0
    B1 = B*1
    B2= B1*1
    for i in range(dim):
        for j in range(dim):
            if B1[i,j] >0:
                pos = [i,j]
                B2 = invert_board(B1) 
                pos_inv = invert_pos(pos,dim)
                if direct_att_pos_depth(pos_inv,B2,depth):
                    val = val- B1[i,j]
    return val


def direct_att_pos_depth(pos,B,depth):
    if depth == 0:
        return direct_att_pos(pos,B)
    else:
        B1 = B*1
        att_list = []
        att_list= my_defensors_pos(pos,B1)
        if att_list== []:
            return False
        current_val= value_player(B1,depth-1)
        B2 = B1*1
        for att in att_list:
            move0 = [[att[1],att[2]],pos]
            if not king_wellness_move(B1,move0):
                continue
            B2= move(move0[0],move0[1],B1)
            new_val = value_player(B2,depth-1)
            if new_val> current_val:
                return True            
    return False
            
 

def direct_att_pos(pos,B):
    B1 = B*1
    dim = len(B)
    #se ho almeno un attaccante
    att_list = [] 
    att_list= my_defensors_pos(pos,B1)
    if att_list== []:
        return False
    # se c'è almeno un difensore
    B2 = B1*1
    B2 = invert_board(B1) 
    pos_inv = invert_pos(pos,dim)
    enemy_def_pos_list = []
    enemy_def_pos_list = my_defensors_pos(pos_inv,B2)
    if enemy_def_pos_list == []:
        return True
    
    for att in att_list:
        move0 = [[att[1],att[2]],pos]
        if not king_wellness_move(B1,move0):
            continue
        if att[0]+1.5 < -B1[pos[0],pos[1]]:
            return True

    return False    
    
    




def value_mid_control(B):
    value = 0
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if B[i,j] > 0 and B[i,j] != king :
                value = value + i*np.sqrt(1/((j-3.5)**2))
    return value


def value_protect(B):
    value = 0
    defence = defence_board(B)
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if defence[i,j] > 0 and B[i,j] > 0 and B[i,j] != king:
                value = value + 1
    
    return value

def board_control(B):
    dim = len(B)
    n = 0
    for i in range(dim):
        for j in range(dim):
            if B[i,j] > 0 and B[i,j] != king : 
                for pos in possible_pos_piece(B[i,j],[i,j], B):
                    n = n+1
    return n

#----------------------------------------

def move(pos1,pos2,B):
    B[pos2[0],pos2[1]] = B[pos1[0],pos1[1]]
    B[pos1[0],pos1[1]] = 0
    return B

def invert_board(B):
    return -np.flipud(np.fliplr(B))

def invert_pos(pos,dim):
    return [dim-1-pos[0], dim-1-pos[1]]


def my_piece_list(B):      
    allied_piece_list = []
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if B[i,j] > 0 :
                allied_piece_list += [[B[i,j],i,j]]            
    return allied_piece_list
    

def my_defensors_pos(pos,B):
        B2 = B*1
        target = B2[pos[0],pos[1]]
        if target == 0 or target > 0 :
            B2[pos[0],pos[1]] = -1
        B3 = B2*1
        defensors_list = []
        for defensor in my_piece_list(B3) :
                for new_pos in possible_pos_piece(defensor[0],[defensor[1],defensor[2]], B3):                 
                    if pos == new_pos   :
                        defensors_list +=  [defensor]
        return defensors_list
        
                           
def enemy_defensors_pos(pos,B) :
         B2 = B * 1
         B2 = invert_board(B)
         invaders_list = []
         invaders_list2 = []
         pos2 = [0,0]
         dim = len(B)
         pos2[0] = (dim-1)-pos[0]*1
         pos2[1] = (dim-1)-pos[1]*1
         invaders_list = my_defensors_pos(pos2,B2)
         for minion in invaders_list:
             minion[1] = (dim-1) - minion[1]
             minion[2] = (dim-1) - minion[2]
             invaders_list2 += [minion]
         return invaders_list2
  

def king_wellness(B):
    dim = len(B)
    for minion in my_piece_list(B):
        if minion[0]== king:
            pos = [minion[1],minion[2]]
            B2 = invert_board(B)
            pos[0] = dim-1 - pos[0]
            pos[1] = dim-1 - pos[1]
            for enemy in my_piece_list(B2):
                for new_pos in possible_pos_piece(enemy[0],[enemy[1],enemy[2]],B2) :
                    if new_pos[0] == pos[0]  and  new_pos[1] == pos[1] :
                        return False
    return True      

 
def king_wellness_move(B,PlayerMove):
    B2 = B * 1
    B2 = move(PlayerMove[0],PlayerMove[1],B2)
    return king_wellness(B2)
    
def defence_board(B) :
    dim = len(B)
    def_field = np.zeros((int(dim), dim), dtype = np.int)
    for minion in my_piece_list(B):
        if minion[0] == pawn :
             if minion[1] < dim-1 :
                    if minion[2] > 0 :
                        def_field[minion[1]+1,minion[2]-1] += 1
                    if minion[2] < dim-1 :
                        def_field[minion[1]+1,minion[2]+1] += 1
        else :
            for pos in possible_pos_piece(minion[0],[minion[1],minion[2]],B) :
                def_field[pos[0],pos[1]] += 1
        
    return  def_field    
    

def value_piece(B) :
    value = 0
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if B[i,j] > 0  :
                value = value + B[i,j]*100
    return value


def value_partial_in_danger(B) :
    value = 0
    for minion in my_piece_list(B):
        [piece,pos] = minion
        if enemy_defensors_pos(pos,B) != []:
            value = value -piece
            
    return value
        

def value_def_my_king(B) :
    pos_king = [0,0]
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if B[i,j] == king :
                pos_king = [i,j]
    if enemy_defensors_pos(pos_king,B) == []:
        return 0
    else :
        return -1
def list_separated(minion_out,minion_list):
    new_minion_list = []
    for minion in minion_list:
        if minion != minion_out:
            new_minion_list += [minion]
    return new_minion_list


def end_check(B) :
    B = invert_board(B)
    for piece in my_piece_list(B) :
        pos = [piece[1],piece[2]]
        poss_piece = possible_pos_piece(piece[0],pos, B)
        if poss_piece != []:
            for new_pos in poss_piece:    
                if king_wellness_move(B,[pos,new_pos]) :
                    return 0 
    if  king_wellness(B) :
        if -value_piece(B) < -value_piece(-B) :
            return 0.5
        else:
            return -0.5
    return 1

    
#_____________________________________________________________

# PIECE MOVEMENT (uguale a piece_movement)

     
def possible_pos_piece(piece,pos, B):
        poss_pos_list = []
        if piece == pawn   :
            poss_pos_list = possible_pos_pawn(pos,B)
            
        if piece == tower :
            poss_pos_list = possible_pos_tower(pos,B)
            
        if piece == king :
            poss_pos_list = possible_pos_king(pos,B)
            
        if piece == bishop :   
            poss_pos_list = possible_pos_bishop(pos,B)
        
        if piece == queen :   
            poss_pos_list = possible_pos_queen(pos,B)   
            
        if piece == knight :   
            poss_pos_list = possible_pos_knight(pos,B)
                
            
        return poss_pos_list

def possible_pos_pawn(pos,B) :
        r = pos[0]
        c = pos[1]
        poss_pos_list = []
        dim = len(B)
        if r ==  1 :
           if B[r + 1, c] == 0 and B[r + 2, c] ==0  :
               #move = [pos,[r + 2, c]]
               #if king_wellness(B,move) :
                    poss_pos_list += [[r + 2, c]]
        if r < dim-1:  
            #mangia a sx          
            if c > 0:
                if B[r + 1, c - 1] < 0:
                   # move = [pos,[r + 1, c - 1]]
                   # if king_wellness(B,move) :
                        poss_pos_list += [[r + 1, c - 1]]
            #mangia a dx        
            if c < dim-1:
                if B[r + 1, c + 1] < 0:
                    poss_pos_list += [[r + 1, c + 1]]
            #muovi avanti       
            if B[r + 1, c] == 0:
                poss_pos_list += [[r + 1, c]]
        return poss_pos_list
    
def possible_pos_tower(pos,B):
        r = pos[0]
        c = pos[1]
        poss_pos_list = []    
        check_down = True
        check_up = True 
        check_right = True
        check_left = True
        dim = len(B)
        for j in range(dim-1):
            #print(2)  
            i = j + 1
            if r + i < dim  :
               # print(3)
                if B[r + i, c] == 0 and check_down :
                   poss_pos_list += [[r + i, c]]
                elif B[r + i, c] < 0 and check_down :
                  # print('EHI')
                   poss_pos_list += [[r + i, c]]   
                   check_down = False
                elif B[r + i, c] > 0 and check_down:
                     check_down = False
            
            if -1 < r - i : 
                if B[r - i, c] == 0 and check_up :
                   poss_pos_list += [[r - i, c]]
                elif B[r - i, c] < 0 and check_up :
                   poss_pos_list += [[r - i, c]] 
                   check_up = False
                else:
                     check_up = False

            
            if c + i < dim :
                if B[r , c + i] == 0 and check_right :
                   poss_pos_list += [[r , c + i]]
                elif B[r , c + i] < 0 and check_right :
                   poss_pos_list += [[r , c + i]]   
                   check_right = False
                else:
                     check_right = False
     
            if -1 < c - i : 
                if B[r , c - i] == 0 and check_left :
                   poss_pos_list += [[r , c - i]]
                elif B[r , c - i] < 0 and check_left :
                   poss_pos_list += [[r , c - i]]
                   check_left = False
                else:
                    check_left = False
       # print('pos list',poss_pos_list)
        
        return poss_pos_list
        
        
def possible_pos_bishop(pos,B):
        r = pos[0]
        c = pos[1]
        poss_pos_list = []  
        
        check_dr = True
        check_dl = True 
        check_ur = True
        check_ul = True
        dim = len(B)
        for j in range(dim-1):
            i = j + 1
            
            if r + i < dim and c + i < dim :
                if  B[r + i, c + i] == 0 and check_dr :
                    poss_pos_list += [[r + i , c + i]]
                elif B[r + i, c + i] < 0 and check_dr :
                    poss_pos_list += [[r + i , c + i]]
                    check_dr = False
                else:
                    check_dr = False
                             
            if r + i < dim and -1 < c - i :
                if  B[r + i, c - i] == 0 and check_dl :
                    poss_pos_list += [[r + i , c - i]]
                elif B[r + i, c - i] < 0 and check_dl :
                    poss_pos_list += [[r + i , c - i]]
                    check_dl = False
                else:
                    check_dl = False
                    
            if -1 < r - i  and  c + i < dim :
                if  B[r - i, c + i] == 0 and check_ur :
                    poss_pos_list += [[r - i , c + i]]
                elif B[r - i, c + i] < 0 and check_ur :
                    poss_pos_list += [[r - i , c + i]]
                    check_ur = False
                else:
                    check_ur = False 
                    
            if -1 < r - i and -1 < c - i :
                if  B[r - i, c - i] == 0 and check_ul :
                    poss_pos_list += [[r - i , c - i]]
                elif B[r - i, c - i] < 0 and check_ul :
                    poss_pos_list += [[r - i , c - i]]
                    check_ul = False
                else:
                    check_ul = False
                    
        return  poss_pos_list
                    
    
def possible_pos_queen(pos,B) :
    
    poss_pos_list = []
    list1 = []
    list2 = []
    list1 = possible_pos_tower(pos,B)
    list2 = possible_pos_bishop(pos,B)
    poss_pos_list = list1 + list2
    
    return poss_pos_list
        
def possible_pos_knight(pos,B) :
        poss_pos_list = []
        dim = len(B)
        r = pos[0]
        c = pos[1]
        
        x = r - 1
        y = c + 2
        if -1 < x and y < dim  :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]
                
        x = r - 2
        y = c + 1
        if -1 < x and y < dim  :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]
        
        x = r - 2
        y = c - 1      
        if -1 < x and -1 < y   :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]
           
        x = r - 1
        y = c - 2
        if -1 < x and -1 < y   :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]

        x = r + 1
        y = c - 2                   
        if  x < dim and -1 < y   :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]
        
        x = r + 2
        y = c - 1                
        if  x < dim and -1 < y   :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]

        x = r + 2
        y = c + 1                
        if  x < dim and  y < dim  :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]
                
        x = r + 1
        y = c + 2                
        if  x < dim and  y < dim  :
            if B[ x , y ] <= 0 :
                poss_pos_list += [[x , y]]         
                 
        return poss_pos_list 
    

    
def my_defensors_pos_special(pos,B):

        defensors_list = []
        B2 = B*1
        B2[pos[0],pos[1]] = -B2[pos[0],pos[1]]
        for defensor in my_piece_list(B2) :
                if defensor[0] != king :
                    for new_pos in possible_pos_piece(defensor[0],[defensor[1],defensor[2]], B2):
                            if pos == new_pos  :
                               defensors_list +=  [defensor]                         
        return defensors_list
def enemy_defensors_pos_special(pos,B) :
         r = pos[0]
         c = pos[1]
         B2 = invert_board(B)*1
         invaders_list = []
         pos2 = [r,c]
         dim = len(B)
         pos2[0] = (dim-1)-r
         pos2[1] = (dim-1)-c
         if B2[pos2[0],pos2[1]] == 0:
             B2[pos2[0],pos2[1]] = 1
         invaders_list = my_defensors_pos_special(pos2,B2)         
         for i in range(3) :    
              if r - 1 + i < dim and -1 < r - 1 + i :
                   if c - 1 > -1 :
                       if B[r - 1 + i,c - 1] == -king:
                           invaders_list += [[-pawn,0,0]] 
                   if c + 1 < dim:
                      if B[r - 1 + i,c + 1] == -king :
                           invaders_list += [[-pawn,0,0]] 
          
         if r - 1 > -1 :
              if B[r - 1,c] == -king :
                  invaders_list += [[-pawn,0,0]]
                        
         if r + 1 < dim :
              if B[r + 1,c] == -king :
                  invaders_list += [[-pawn,0,0]]
                    
         return invaders_list
    
def possible_pos_king(pos,B) :
        poss_pos_list = []
        r = pos[0]
        c = pos[1]
        dim = len(B)
        
        y = c + 1
        if y < dim :
           
            x = r            
            if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == [] :
                poss_pos_list += [[x,y]]
            
            x = r + 1
            if x < dim and enemy_defensors_pos_special([x,y],B) == [] :
                if B[x,y] <= 0:
                    poss_pos_list += [[x,y]] 
            
            x = r - 1
            if -1 < x and enemy_defensors_pos_special([x,y],B) == [] :
                if B[x,y] <= 0:
                    poss_pos_list += [[x,y]]
        
        y = c - 1            
        if -1 < y :
            
            x = r
            if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == []:
                poss_pos_list += [[x,y]]
            
            x = r + 1
            if r + 1 < dim  :
                if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == []:
                    poss_pos_list += [[x,y]] 
            x = r- 1        
            if -1 < r - 1  :
                if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == [] :
                    poss_pos_list += [[x,y]]
        y = c
        x = r + 1            
        if r + 1 <  dim :
            if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == []:
                poss_pos_list += [[x,y]]
        x = r - 1    
        if -1 < r - 1  :
            if B[x,y] <= 0 and enemy_defensors_pos_special([x,y],B) == []:
                poss_pos_list += [[x,y]]

        return poss_pos_list