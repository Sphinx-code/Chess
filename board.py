import numpy as np
import re
#np.set_printoptions(threshold=np.nan)

pawn = 10 
bishop = 70  
knight = 71  
tower = 90  
queen = 120   
king = 4000 

## BoardGen: genera una scacchiera, con re e pedoni, di dimensione data
def BoardGen(dim):
    B = np.zeros((int(dim/2), dim), dtype = np.int)
    B = classical(dim)
#    B = -conf_file(dim)
  #  B = -board_transf(B)
 #   B = np.zeros((int(dim), dim), dtype = np.int)
  #  B[0, 0] = -king
 

 #   B[2, 6] = pawn
   #B[0, int(dim/2)-1] = king
   # B[6 ,0] = queen
#    B[7,0] =  king   

    return B

## UpdateBoard
def UpdateBoard(B, PlayerMove):
    pos_in = PlayerMove[0]
    pos_fi = PlayerMove[1]
    B[pos_fi[0], pos_fi[1]] = B[pos_in[0], pos_in[1]]
    B[pos_in[0], pos_in[1]] = 0
    if pos_fi[0] == len(B) :
        if B[pos_fi[0], pos_fi[1]] == pawn :
            B[pos_fi[0], pos_fi[1]] = queen
    
    return B

def board_transf(B):
    return -np.flipud(np.fliplr(B))

def classical(dim):
    if dim == 8 :
        B = np.zeros((4, 8), dtype = np.int)
        B[1, :] = pawn
        B[0,0] = tower
        B[0,7] = tower
        B[0,1] = knight
        B[0,6] = knight
        B[0,2] = bishop
        B[0,5] = bishop
        B[0,3] = queen
        B[0,4] = king
        B = -np.concatenate((-B, np.flipud(np.fliplr(B))), axis=0)
        B[0,3] = king
        B[0,4] = queen
        
        return board_transf(B)
    else:
        return np.zeros((int(dim/2), dim), dtype = np.int)


def conf_file(dim):

   file = open('conf.txt', 'r')
   file = file.read() 
   numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
   d = 0
   B = np.zeros((8, 8), dtype = np.int)
   for i in range(dim):
       for j in range(dim):
          B[i,j]=float( numbers[d])
          d = d+1
   return B
        