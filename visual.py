import numpy as np

def nice_info_white(white,PlayerMove,B) :
    PlayerMove0 = PlayerMove[0]
    PlayerMove1 = PlayerMove[1]
    print('')
    if B[PlayerMove[1][0],PlayerMove[1][1]] == 0 :
        print (white,' moved ',B[PlayerMove0[0],PlayerMove0[1]],' from ',[len(B) -1 -PlayerMove0[0], len(B) -1 -PlayerMove0[1]],' to', [len(B) -1 -PlayerMove1[0], len(B) -1 -PlayerMove1[1]])
    else:
        print (white,' moved ',B[PlayerMove0[0],PlayerMove0[1]],' from ',PlayerMove0,' to', PlayerMove1,'eating',B[PlayerMove1[0],PlayerMove1[1]])
    print('')
    return 1

def nice_info_black(black,PlayerMove,B) :
    PlayerMove0 = PlayerMove[0]
    PlayerMove1 = PlayerMove[1]

    print('')
    if B[PlayerMove1[0],PlayerMove1[1]] == 0 :
        print (black,' moved ',-B[PlayerMove0[0],PlayerMove0[1]],' from ',PlayerMove[0],' to', PlayerMove[1])
    else:
        print (black,' moved ',-B[PlayerMove0[0],PlayerMove0[1]],' from ',PlayerMove0,' to', PlayerMove1,'eating',-B[PlayerMove1[0],PlayerMove1[1]])
    print('')
    return 1



def nice_board(B) :
       dim = len(B)
       C = np.zeros((int(dim)+1, dim+1), dtype = np.int)
       for i in range(len(B)) :
           for j in range(len(B)) :
               C[i+1,j+1]= B[i,j]
       for i in range(len(B)) :
          C[0, i + 1 ] = -i
          C[ i + 1, 0] = -i
       C[0,0] = 0
       print(-C)
       return 1
   
def board_transf(B):
    return -np.flipud(np.fliplr(B))

def turn_information(turn) :
    print('')
    print('----------------------------------------------------------------')
    print('TURN ',turn+1)
    print('')
    return True

def welcome(B):
    print('')
    print('Chess engine started')
    print('')
    print('           ° ° ° ° ° ° ° ° ° ° Black ° ° ° ° ° ° ° ° ° °')
    print('')
    nice_board(B)
    print('')
    print('           ° ° ° ° ° ° ° ° ° ° White ° ° ° ° ° ° ° ° ° °')
    return True