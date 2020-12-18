gameover = False

player1obj = "O"
player2obj = "X"

board = {"7": " ", "8": " ", "9": " ",
         "6": " ", "5": " ", "4": " ",
         "1": " ", "2": " ", "3": " ",
         }

def main():
    printboard(board)
    while True:
        player1turn()
        printboard(board)
        if checkwin(board):
            break
        player2turn()
        printboard(board)
        if checkwin(board):
            break

def printboard(table):
    print("\n" + table["7"] + "|" + table["8"] + "|" + table["9"])
    print("-----")
    print(table["6"] + "|" + table["5"] + "|" + table["4"])
    print("-----")
    print(table["1"] + "|" + table["2"] + "|" + table["3"] + " \n")


def printorder():
    print("\n" + "7" + "|" + "8" + "|" + "9")
    print("-----")
    print("6" + "|" + "5" + "|" + "4")
    print("-----")
    print("1" + "|" + "2" + "|" + "3" + "\n")


def checkselection(selection):
    for i in selection:
        if not i.isdigit():
            return False
    if len(selection) >= 2:
        return False
    if selection == "":
        return False
    if board[selection] != " ":
        return False
    return True


def printplayerwon(key, board):
    if key == "10":
        print("Game was a draw")
        return
    elif board[key] == "O":
        print("{} won!".format(player1name))
    elif board[key] == "X":
        print("{} won!".format(player2name))


def checkwin(board, gameover = False, draw = True):
    for value in board.values():
        if value == " ":
            draw = False
    if board["1"] == board["2"] == board["3"] != " ":
        print("Game over")
        printplayerwon("1", board)
        gameover = True
    elif board["1"] == board["6"] == board["7"] != " ":
        print("Game over")
        printplayerwon("1", board)
        gameover = True
    elif board["1"] == board["5"] == board["9"] != " ":
        print("Game over")
        printplayerwon("1", board)
        gameover = True
    elif board["2"] == board["5"] == board["8"] != " ":
        print("Game over")
        printplayerwon("2", board)
        gameover = True
    elif board["3"] == board["4"] == board["9"] != " ":
        print("Game over")
        printplayerwon("3", board)
        gameover = True
    elif board["3"] == board["5"] == board["7"] != " ":
        print("Game over")
        printplayerwon("3", board)
        gameover = True
    elif board["6"] == board["5"] == board["4"] != " ":
        print("Game over")
        printplayerwon("6", board)
        gameover = True
    elif board["7"] == board["8"] == board["9"] != " ":
        print("Game over")
        printplayerwon("7", board)
        gameover = True
    elif draw:
        print("Game over")
        gameover = True
        printplayerwon("10", board)
        
    return gameover

def player1turn():
    while True:
        player1selection = input("Please select a a square, if you want to see the order please say \"order\" : \n")
        if player1selection == "order":
            printorder()
        elif checkselection(player1selection):
            board[player1selection] = player1obj
            break
        else:
            print("Invalid selection")


def player2turn():
    while True:
        player2selection = input("Please select a a square, if you want to see the order please say \"order\" : \n")
        if player2selection == "order":
            printorder()
        elif checkselection(player2selection):
            board[player2selection] = player2obj
            print("Valid selection")
            break
        else:
            print("Invalid selection")



if __name__ == '__main__':
    print("Hello, and welcome to Tic Tac Toe,\nThis is a two player game. Have fun! Player 1 is {}, and Player 2 is {} \n")

    player1name = input("Player1, Please enter in your name! ")
    player2name = input("Player2, Please enter in your name! ")
    main()
