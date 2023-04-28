import Epaminonda_1 as co

def PlayerMove(B):
    pos = [0,0,0,0]
    d = len(B)
    print('Insert your move')
    str_arr = input().split(' ')
    pos = [int(num) for num in str_arr]
    best_move = [[d-1-pos[0],d-1-pos[1]],[d-1-pos[2],d-1-pos[3]]]
    B1=B*1
    B2= co.move(best_move[0],best_move[1],B1)
    co.nice_info(B,B2,1)
    return best_move