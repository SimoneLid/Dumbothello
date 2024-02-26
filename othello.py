import time
import images
import keyboard
import random
casella=(128,128,128)
bianco=(255,255,255)
nero=(0,0,0)
marrone=(90,60,12)
sleep_time=0.3

def cattura(board,y,x,mossa_attuale):
    diz={0:(-1,-1),1:(1,1),2:(1,0),3:(1,-1),4:(0,1),5:(0,-1),6:(-1,1),7:(-1,0)}
    for i in range(8):
        if fuori(board,y+diz[i][0],x+diz[i][1])==False:
            if mossa_attuale=="bianco" and board[y+diz[i][0]][x+diz[i][1]]==nero:
                    board[y+diz[i][0]][x+diz[i][1]]=bianco
            elif mossa_attuale=="nero" and board[y+diz[i][0]][x+diz[i][1]]==bianco:
                    board[y+diz[i][0]][x+diz[i][1]]=nero
    return board
                


def fuori(board,y,x):
    if y>=len(board) or y<0 or x >= len(board[0]) or x<0:
        return True
    return False
        

def intorno_casella(board,y,x,mossa_attuale,mosse):
    diz={0:(-1,-1),1:(1,1),2:(1,0),3:(1,-1),4:(0,1),5:(0,-1),6:(-1,1),7:(-1,0)}
    for i in range(8):
        if fuori(board,y+diz[i][0],x+diz[i][1])==False:
            if mossa_attuale=="nero" and board[y+diz[i][0]][x+diz[i][1]]==bianco:
                mosse.add((y,x))
                break
            elif mossa_attuale=="bianco" and board[y+diz[i][0]][x+diz[i][1]]==nero:
                mosse.add((y,x))
                break
    return mosse


def conta_mossa(board,mossa_attuale):
    mosse=set(())
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]==casella:
                mosse=intorno_casella(board, y, x, mossa_attuale, mosse)
    mosse=list(mosse)
    mosse.sort()
    return mosse
        
         
def cambio_mossa(mossa_attuale,board):
    lenght=len(board)
    if mossa_attuale=="bianco":
        mossa_attuale="nero"
        ultima_mossa="bianco"
        for i in range(lenght):
            for j in range(lenght):
                if i==0 or i==lenght-1 or j==0 or j==lenght-1:
                    board[i][j]=nero
    else:
        mossa_attuale="bianco"
        ultima_mossa="nero"
        for i in range(lenght):
            for j in range(lenght):
                if i==0 or i==lenght-1 or j==0 or j==lenght-1:
                    board[i][j]=bianco
    return  board,ultima_mossa, mossa_attuale
    

def fai_mosse(board,ultima_mossa,mossa_attuale):
    mosse_possibili=conta_mossa(board, mossa_attuale)
    if len(mosse_possibili)>0:
        puntatore=list(mosse_possibili[0])
        board[puntatore[0]][puntatore[1]]=(0,255,0)
        prev_pos=(128,128,128)
        images.save(board,"board.png")
        while True:
            if keyboard.is_pressed("down") or keyboard.is_pressed("s"):
                if fuori(board,puntatore[0]+1,puntatore[1])==False:
                    board[puntatore[0]][puntatore[1]]=prev_pos
                    puntatore[0]+=1
                    prev_pos=board[puntatore[0]][puntatore[1]]
                    if tuple(puntatore) in mosse_possibili:
                        board[puntatore[0]][puntatore[1]]=(0,255,0)
                    else:
                        board[puntatore[0]][puntatore[1]]=(128,0,0)
                    images.save(board,"board.png")
                    time.sleep(sleep_time)
            if keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                if fuori(board,puntatore[0],puntatore[1]+1)==False:
                    board[puntatore[0]][puntatore[1]]=prev_pos
                    puntatore[1]+=1
                    prev_pos=board[puntatore[0]][puntatore[1]]
                    if tuple(puntatore) in mosse_possibili:
                        board[puntatore[0]][puntatore[1]]=(0,255,0)
                    else:
                        board[puntatore[0]][puntatore[1]]=(128,0,0)
                    images.save(board,"board.png")
                    time.sleep(sleep_time)
            if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                if fuori(board,puntatore[0],puntatore[1]-1)==False:
                    board[puntatore[0]][puntatore[1]]=prev_pos
                    puntatore[1]-=1
                    prev_pos=board[puntatore[0]][puntatore[1]]
                    if tuple(puntatore) in mosse_possibili:
                        board[puntatore[0]][puntatore[1]]=(0,255,0)
                    else:
                        board[puntatore[0]][puntatore[1]]=(128,0,0)
                    images.save(board,"board.png")
                    time.sleep(sleep_time)
            if keyboard.is_pressed("up") or keyboard.is_pressed("w"):
                if fuori(board,puntatore[0]-1,puntatore[1])==False:
                    board[puntatore[0]][puntatore[1]]=prev_pos
                    puntatore[0]-=1
                    prev_pos=board[puntatore[0]][puntatore[1]]
                    if tuple(puntatore) in mosse_possibili:
                        board[puntatore[0]][puntatore[1]]=(0,255,0)
                    else:
                        board[puntatore[0]][puntatore[1]]=(128,0,0)
                    images.save(board,"board.png")
                    time.sleep(sleep_time)
            if keyboard.is_pressed("space") or keyboard.is_pressed("enter"):
                if tuple(puntatore) in mosse_possibili:
                    board[puntatore[0]][puntatore[1]]=prev_pos
                    time.sleep(sleep_time)
                    break
                time.sleep(sleep_time)
        if mossa_attuale=="bianco":
            board[puntatore[0]][puntatore[1]]=bianco
        elif mossa_attuale=="nero":
            board[puntatore[0]][puntatore[1]]=nero
        board=cattura(board, puntatore[0], puntatore[1], mossa_attuale)
        board,ultima_mossa,mossa_attuale=cambio_mossa(mossa_attuale,board)
        images.save(board,"board.png")
        fai_mosse(board, ultima_mossa, mossa_attuale)
    else:
        bianchi=0
        neri=0
        for riga in range(2,len(board)-2):
            for casella in range(2,len(board)-2):
                if board[riga][casella]==bianco:
                    bianchi+=1
                elif board[riga][casella]==nero:
                    neri+=1
        print("Bianchi:",bianchi,"  Neri:",neri)
        if neri>bianchi:
            print("Vince il nero \n")
        elif bianchi>neri:
            print("Vince il bianco \n")
        else:
            print("Pari \n")


def create_random(lenght):
    board_random=[[] for i in range(lenght+4)]
    for i in range(lenght+4):
        for j in range(lenght+4):
            if i==0 or i==lenght+3 or j==0 or j==lenght+3:
                board_random[i].append(nero)
            elif i==1 or i==lenght+2 or j==1 or j==lenght+2:
                board_random[i].append(marrone)
            else:
                casella_random=random.randint(1,3)
                if casella_random==1:
                    board_random[i].append(casella)
                elif casella_random==2:
                    board_random[i].append(bianco)
                elif casella_random==3:
                    board_random[i].append(nero)
    return board_random


def create_board(lenght):
    board=[[] for i in range(lenght+4)]
    for i in range(lenght+4):
        for j in range(lenght+4):
            if i==0 or i==lenght+3 or j==0 or j==lenght+3:
                board[i].append(nero)
            elif i==1 or i==lenght+2 or j==1 or j==lenght+2:
                board[i].append(marrone)
            elif (i==(lenght+4)/2 and j==(lenght+4)/2) or (i==((lenght+4)/2)-1 and j==((lenght+4)/2)-1):
                board[i].append(nero)
            elif (i==(lenght+4)/2 and j==((lenght+4)/2)-1) or (i==((lenght+4)/2)-1 and j==((lenght+4)/2)):
                board[i].append(bianco)
            else:
                board[i].append(casella)
    return board

def dumbothello(lenght=8,board="base"):
    if board=="random":
        board=create_random(lenght)
    else:
        if lenght%2!=0:
            print("Impossibile creare una board base di grandezza",lenght)
            print("La grandezza deve essere pari")
            return
        board=create_board(lenght)
    images.save(board,"board.png")
    ultima_mossa="bianco"
    mossa_attuale="nero"
    fai_mosse(board,ultima_mossa,mossa_attuale)


if __name__ == "__main__":
    #dumbothello(9,"random")
    #dumbothello(10)
    #dumbothello(12,"fgjhhio")
    #dumbothello(4,"base")
    #dumbothello()
    pass