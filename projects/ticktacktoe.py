board = [" " for x in range(9)]

def printBoard():
    print("")
    print("|{}|{}|{}|".format(board[0],board[1],board[2]))
    print("|{}|{}|{}|".format(board[3],board[4],board[5]))
    print("|{}|{}|{}|".format(board[6],board[7],board[8]))
    print("")
    
printBoard()

xTurn = True

def player_move(icon):
    global xTurn
    pos = int(input("Player {} - Pick a position from 1 to {}: ".format(icon,len(board))).strip())
    if board[pos-1] == " ":
        board[pos-1] = icon
        if xTurn:
            xTurn = False
        else:
            xTurn = True
    else:
        print("That position is taken")

def gameActive(symbol):
    if (board[0]==symbol and board[1]==symbol and board[2]==symbol) or\
    (board[3]==symbol and board[4]==symbol and board[5]==symbol) or\
    (board[6]==symbol and board[7]==symbol and board[8]==symbol)or\
    (board[0]==symbol and board[3]==symbol and board[6]==symbol) or\
    (board[1]==symbol and board[4]==symbol and board[7]==symbol) or\
    (board[2]==symbol and board[5]==symbol and board[8]==symbol) or\
    (board[0]==symbol and board[4]==symbol and board[8]==symbol) or\
    (board[2]==symbol and board[4]==symbol and board[6]==symbol):
        print("")
        print(" WINNNER " + symbol)
        return False
    return True

def isDraw():
    for x in board:
        if x == " ":
            return False
    print("ITS A DRAWWWWWWWWWWWWWWWW")
    return True

while gameActive("X") and gameActive("O") and not isDraw() :
    if xTurn:
        player_move("X")
    else:
        player_move("O")
    printBoard()
