#6.3
#Tic Tac Toe'like
"""
Принцы Пы
1 X O
2 random
3 5
"""
import random

board = [["-" for j in range(3)] for i in range(3)]
Humanturn = [2,4,6,8]
AIturn = [1,3,5,7,9]

def board_paint():
    print("_"*13)
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end = " | ")

        print(" ", )
    print("‾"*13)

def rule_print():
    print("Выбирайте координату\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")

def game_move(movement,s:str):
    m = movement -1
    board[m//3][m%3] = s
    return None

def valid(movement:int):
    if movement >0 and movement < 10:
        movement -=1
        return board[movement//3][movement%3] == "-"
    else:
        return False



def AIlol():
    ch = []
    for i in range(1,10):
        if valid(i):
            ch.append(i)
    return random.choice(ch)

def check_H():
    w = False
    for x in range(3):
        if board[x][0]==board[x][1]==board[x][2] =="X" or \
            board[x][0]==board[x][1]==board[x][2] =="O":
            w = True
    return w

def check_V():
    w = False
    for y in range(3):
        if board[0][y]==board[1][y]==board[2][y] =="O" or \
            board[0][y]==board[1][y]==board[2][y] =="X":
            w = True
    return w

def check_D():
    w = False
    if board[0][0]==board[1][1]==board[2][2] =="O" or \
        board[0][0]==board[1][1]==board[2][2] =="X":
        w = True
    if board[0][2]==board[1][1]==board[2][0] =="O" or\
        board[0][2]==board[1][1]==board[2][0] =="X":
        w = True
    return w

def win(turn):
    if turn in Humanturn:
        print("Вы победили! ")
    if turn in AIturn:
        print("Слава роботам! ")

def check_bord():
    if check_H() or check_V() or check_D:
        return True
    
def gameloop(turn:int):
    move = 0
    sign = "-"
    if turn in Humanturn:
        sign = "O"
        move = int(input("Ход O  "))
        if valid(move):
            game_move(move,sign)
        else:
            print("Невозможный ход")
            gameloop(turn)

    if turn in AIturn:
        sign = "X"
        if turn > 1:
            move = AIlol()            
        else:
            move=5
        game_move(move,sign)

def main():
    print("Начало игры")
    print("Поле")
    board_paint()
    print("Вы ноль")
    print("Ход Х")
    rule_print()
    for turn in range(1,10):
        gameloop(turn)
        board_paint()

        if turn > 5:
            if check_bord():
                win(turn)
                break
