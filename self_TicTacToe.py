theBoard=[" "," "," "," "," "," "," "," "," "]
def PrintBoard(theBoard):
    print("-"*13)
    print("|",theBoard[6],"|",theBoard[7],"|",theBoard[8],"|")
    print("-"*13)
    print("|",theBoard[3],"|",theBoard[4],"|",theBoard[5],"|")
    print("-"*13)
    print("|",theBoard[0],"|",theBoard[1],"|",theBoard[2],"|")
    print("-"*13)

def mainGame():
    turn="X"
    count=0
    PrintBoard(theBoard)
    for i in range(10):
        #Get player move
        print("Choose Your Place",turn," : ",end=" ")
        while True:
            try:
                move=int(input())
                break
            except ValueError:
                print("Only Enter Number : Try Again",end=" ")
            except IndexError:
                print("Only Enter Number between 1 to 9 (include 9) ",end=" ")
        theBoard[move-1]=turn                      
        PrintBoard(theBoard)
        count=count+1
        #assign board to next player
        if turn=="X":
            turn="O"
        else:
            turn="X"
        #Check Win Chance
        if count>=5:
            if theBoard[0]==theBoard[1]==theBoard[2] != " ":
                print(theBoard[0],"is Winner")
                break
            elif theBoard[3]==theBoard[4]==theBoard[5] != " ":
                print(theBoard[3],"is Winner")
                break
            elif theBoard[6]==theBoard[7]==theBoard[8] != " ":
                print(theBoard[6],"is Winner")
                break
            elif theBoard[6]==theBoard[3]==theBoard[0] != " ":
                print(theBoard[3],"is Winner")
                break
            elif theBoard[7]==theBoard[4]==theBoard[1] != " ":
                print(theBoard[7],"is Winner")
                break
            elif theBoard[8]==theBoard[2]==theBoard[5] != " ":
                print(theBoard[8],"is Winner")
                break
            elif theBoard[8]==theBoard[4]==theBoard[0] != " ":
                print(theBoard[8],"is Winner")
                break
            elif theBoard[6]==theBoard[4]==theBoard[2] != " ":
                print(theBoard[6],"is Winner")
                break
        if count==9 or count>9:
            print("This is Draw ! !")
            break
mainGame()
