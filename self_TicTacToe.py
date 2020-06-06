#to assign turns (board score layout)
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' , '1': ' ' , '2': ' ' , '3': ' ' }
#function to print tic tac toe board every time
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
#function for main game
def mainGame():
    count=0
    turn="X"
    for i in range(10):   #10 times possibility in board
        printBoard(theBoard)
        print("Your Move ",turn," : " )
        move=input()
        theBoard[move]=turn
        count=count+1

        #assign Board to next player
        if turn=="X":
            turn="O"
        else:
            turn="X"
        
        #Win Chances
        if count>=5:
            # row wise
            if theBoard["1"]==theBoard["2"]==theBoard["3"] !=" ":
                printBoard(theBoard)
                print(theBoard["1"],"is won !")
                break
            elif theBoard["4"]==theBoard["5"]==theBoard["6"]!=" ":
                printBoard(theBoard)
                print(theBoard["4"],"is won !")
                break
            elif theBoard["7"]==theBoard["8"]==theBoard["9"]!=" ":
                printBoard(theBoard)
                print(theBoard["7"],"is won !")
                break
            #column wise
            elif theBoard["7"]==theBoard["4"]==theBoard["1"]!=" ":
                printBoard(theBoard)
                print(theBoard["7"],"is won !")
                break
            elif theBoard["8"]==theBoard["5"]==theBoard["2"]!=" ":
                printBoard(theBoard)
                print(theBoard["8"],"is won !")
                break
            elif theBoard["9"]==theBoard["6"]==theBoard["3"]!=" ":
                printBoard(theBoard)
                print(theBoard["9"],"is won !")
                break
            #diagonal wise
            elif theBoard["7"]==theBoard["5"]==theBoard["3"]!=" ":
                printBoard(theBoard)
                print(theBoard["7"],"is won !")
                break
            elif theBoard["1"]==theBoard["5"]==theBoard["9"]!=" ":
                printBoard(theBoard)
                print(theBoard["1"],"is won !")
                break
        if count>9 :
            printBoard(theBoard)
            print("It is Draw")
            break
mainGame()