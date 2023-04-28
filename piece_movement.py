import numpy as np
pawn = 10 
bishop = 70  
knight = 71  
tower = 90  
queen = 120   
king = 4000 

  



     
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
    
def board_transf(B):
    return -np.flipud(np.fliplr(B))

def my_piece_list(B):       
    allied_piece_list = []
    dim = len(B)
    for i in range(dim):
        for j in range(dim):
            if B[i,j] > 0 :
                allied_piece_list += [[B[i,j],i,j]]
                
    return allied_piece_list
    
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
         B2 = board_transf(B)*1
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
                    
                
        
        
        
        
        
        
        
        
        
        