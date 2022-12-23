
import random as rn
def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    t=f''' 
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    '''
    print(t)

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    mov = int(input('ingresa tu movimiento(1-9): '))
    pos = 0
    for i in range(len(board)):
        for j in range(len(board)):
            pos+=1
            if pos == mov:
                board[i][j] = user
    return board

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    tup=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                tup.append(tuple((i,j)))
    return tup

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign: return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign: return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign: return True
    
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign: return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign: return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign: return True
    
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: return True
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign: return True
    
    
            

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    tup = MakeListOfFreeFields(board)
    s = rn.randint(0,len(tup)-1)
    mov = tup[s]
    board[mov[0]][mov[1]] = pc
    return board
    

global user
global pc
user = input('ingresa tu letra: ')
pc = input('ingresa letra de la pc: ')
tab = [['-' for i in range(3)] for i in range(3)]
sign = pc
condicion = False
turno = False
while not condicion:
     # falso para usuario / true para pc
    DisplayBoard(tab)
    if turno: 
        tab = DrawMove(tab)
        sign = pc
        turno = not turno       
    else:
        tab = EnterMove(tab)
        sign = user
        turno = not turno
    condicion = VictoryFor(tab,sign)
if sign == pc:
    print('ha ganado PC!!!')
    DisplayBoard(tab)
else:
    print('ha ganado el usuario!!!')
    DisplayBoard(tab)
    
    