
import sys, pprint, random, time

print('\n=====================================================================\n')

# # Check input is 'X' or 'O'? turn upper case, and quit game
def xoChoice():
    xoChoiceList = ('x', 'X', 'o', 'O')     # characters displayed in the game, it can be changed to other character

    while True:
        print('Please enter to choose X or O. (X goes first!)')
        xo = input()
        if xo in xoChoiceList:
            xo = xo if xo.isupper() else xo.upper()
            break
        elif xo == 'q' or xo == 'Q':
            sys.exit()

        print('\nInvalid entry! please entry X, O or Q for quite the game!\n')  

    return xo



## print and refresh the game board

def printGameBoard(gb):
    print('   |   |   ')
    # print(' ' + myGameBoard['top_L'] + ' | ' + myGameBoard['top_M'] + ' | ' + myGameBoard['top_R'])
    print(' ' + gb['top_L'] + ' | ' + gb['top_M'] + ' | ' + gb['top_R'])
    print('___|___|___')
    print('   |   |   ')
    # print(' ' + myGameBoard['mid_L'] + ' | ' + myGameBoard['mid_M'] + ' | ' + myGameBoard['mid_R'])
    print(' ' + gb['mid_L'] + ' | ' + gb['mid_M'] + ' | ' + gb['mid_R'])
    print('___|___|___')
    print('   |   |   ')
    # print(' ' + myGameBoard['low_L'] + ' | ' + myGameBoard['low_M'] + ' | ' + myGameBoard['low_R'])
    print(' ' + gb['low_L'] + ' | ' + gb['low_M'] + ' | ' + gb['low_R'])
    print('   |   |   ')
    print()


## Choose your next move, return the number of position you need to move

def yourChooseMove(numberOfnextMove, numList):
    print(numberOfnextMove)

    while True:
        print('Please enter your move!')
        num = input()

        if num not in numList:
            print('Ocupided! Please choose another number!')
            continue

        if num in numberOfnextMove.keys():
            print('You choose to move to the position of board is : ', num, numberOfnextMove[num])
            return int(num)
        else:
            for k, v in numberOfnextMove.items():
                if v == num:
                    print('You choose to move to the position of board is : ', k, v)
                    return int(k)
        
        print('Invalid input!')



## Random to choose MACHINE next move, return the number of position you need to move

def machineChooseMove(randomMove, numList):

    while True:
        num = random.choice(numList)
        if num in randomMove.keys():
            print('Machine choose to move to the position of board is : ', num, randomMove[num])
            time.sleep(2)
            return int(num)
                

# update the game board with passing 3 parameters: 
# (1) X or O choice to idetify your turn or machine turn (2) number of position to move on game board (3) myGameBoard dictionary

def updateData(c, n, gameBoard_Update):
    # print("???", c,'\n', n,'\n', gameBoard_Update)
    i=1
    for k in gameBoard_Update.keys():
        if i == n:
            gameBoard_Update[k] = c
            break
        else:
            i += 1

## Find who win the game
def gameWin(gameBoard_update):
    winL = list(gameBoard_update.values())
    # print('gameWin list : ', winL)
    # print('winL(range(3)) : ', winL[0:3], winL[3:6], winL[6:9])
    xWin = ['X', 'X', 'X']
    oWin = ['O', 'O', 'O']

    # Condition of X wins
    if (winL[0:3] == xWin) or (winL[3:6] == xWin) or (winL[6:9] == xWin):
        return 'X'
    elif winL[0] == 'X' and winL[3] == 'X' and winL[6] == 'X':
        return 'X'
    elif winL[1] == 'X' and winL[4] == 'X' and winL[7] == 'X':
        return 'X'
    elif winL[2] == 'X' and winL[5] == 'X' and winL[8] == 'X':
        return 'X'
    elif winL[2] == 'X' and winL[4] == 'X' and winL[6] == 'X':
        return 'X'
    elif winL[0] == 'X' and winL[4] == 'X' and winL[8] == 'X':
        return 'X'
    #Condition of O wins
    elif (winL[0:3] == oWin) or (winL[3:6] == oWin) or (winL[6:9] == oWin):
        return 'O'
    elif winL[0] == 'O' and winL[3] == 'O' and winL[6] == 'O':
        return 'O'
    elif winL[1] == 'O' and winL[4] == 'O' and winL[7] == 'O':
        return 'O'
    elif winL[2] == 'O' and winL[5] == 'O' and winL[8] == 'O':
        return 'O'
    elif winL[2] == 'O' and winL[4] == 'O' and winL[6] == 'O':
        return 'O'
    elif winL[0] == 'O' and winL[4] == 'O' and winL[8] == 'O':
        return 'O'


# main() function

def main():

    myGameBoard =   { 'top_L':' ', 'top_M':' ', 'top_R':' ',
                    'mid_L':' ', 'mid_M':' ', 'mid_R':' ',
                    'low_L':' ', 'low_M':' ', 'low_R':' ',
                    }
    myMove =    {   '1':'top-left',    '2':'top-middle',    '3':'top-right',
                    '4':'middle-left', '5':'middle-middle', '6':'middle-right',
                    '7':'low-left',    '8':'low-middle',    '9':'low-right'
                }
    
    # global numberMove_List 
    
    numberMove_List = list(myMove)
  

    
    # Choose X or O
    yourChoice = xoChoice()
    machineChoice = 'X' if yourChoice != 'X' else 'O'
    xChoice = 1 if yourChoice == 'X' else 0

    # Print and refresh the Game Board
    printGameBoard(myGameBoard)


    while numberMove_List:
    
        if xChoice:
            # print('numberMove_List is : ', numberMove_List)
           
            # Choose next move, return the number of position you need to move
            num = yourChooseMove(myMove, numberMove_List)
        
            numberMove_List.remove(str(num))        
            
            # update the game board with passing 3 parameters: 
            # (1) X or O choice to idetify your turn or machine turn (2) number of position to move on game board (3) myGameBoard dictionary
            updateData(yourChoice, num, myGameBoard)
            # print('numberMove_List is : ', numberMove_List)



            # Print and refresh the Game Board
            printGameBoard(myGameBoard)

            winner = gameWin(myGameBoard)

            xChoice = 0
            continue
        else:
            num = machineChooseMove(myMove, numberMove_List)
            numberMove_List.remove(str(num))        
            
            # update the game board with passing 3 parameters: 
            # (1) X or O choice to idetify your turn or machine turn (2) number of position to move on game board (3) myGameBoard dictionary
            updateData(machineChoice, num, myGameBoard)
            # print('numberMove_List is : ', numberMove_List)
            printGameBoard(myGameBoard)
            time.sleep(2)
            winner = gameWin(myGameBoard)
            xChoice = 1
        
        if winner == yourChoice:
            print('Congratulation! YOU WIN THE GAME!')
            sys.exit()
        elif winner != None:
            print('Sorry! YOU LOST THE GAME!')
            sys.exit()

    print("It's a tie!")

    if numberMove_List == 0:
        print('It\'s a tie!')
            

    # print(f'return move number : {num}')
    # print('numberMove_List is : ', numberMove_List)
 



if __name__ == "__main__": main()


print('\n=====================================================================\n')