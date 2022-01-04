# Tic-Tac-Toe

import random, sys
import time

print('\n'*2 + '=' * 30)
print('\t' + "Tic Tac Toe")
print('=' * 30 + '\n')

def drawboard(playBoard):
    for i in range(3):
        for j in range(3):
            key = str(i) + str(j)
            print(f"   {playBoard[key]}   ", end='')
            if j == 2:
                break
            print('|', end='')      
        if i == 2:
            break
        print("\n--------------------------")
    
def CheckWinner(signPlay, playBoard):
    win = False 
    for i in range(3):
        checkPos = str(i)
        if playBoard[checkPos +'0'] == playBoard[checkPos+'1'] == playBoard[checkPos+'2'] == signPlay:
            win = True
        if playBoard['0' + checkPos] == playBoard['1' + checkPos] == playBoard['2' + checkPos] == signPlay:
            win = True
    if playBoard['00'] == playBoard['11'] == playBoard['22'] == signPlay:
        win = True
    if playBoard['02'] == playBoard['11'] == playBoard['20'] == signPlay:
        win = True
    if win:
        if signPlay == playerSign:
            winner = 'Player'
        elif signPlay == machineSign:
            winner = "Machine"

        print(f"\n\n===== {signPlay * 5} {winner} wins! {signPlay * 5} =====\n\n")
        sys.exit()

def moveTurn(flag):
    # winner = ""
    while posToUse:
        if flag:    # Player turn to play
            sign = playerSign
            flag = 0
            while True:
                position = input(f"\n\nPlease input player '{playerSign}' position : ")
                print('\n')
                if position not in posToUse:
                    print("Position is used. Please input availbe positions, include : ", posToUse)
                    continue
                else:
                    break
        else:   # Machine turn to play
            sign = machineSign
            flag = 1
            position = random.choice(posToUse)
            print(f"\n\n\nMachine '{machineSign}' choose position : {position}\n")

        board[position] = sign
        posToUse.remove(position)
        drawboard(board)
        CheckWinner(sign, board)
        # print('\n' * 2 + 'PlayBoard : ', board)
        # print("Position (key) avalible to use : ", posToUse)

board = {}
playerSign = '👻'
machineSign = '💔'
winner = ""
move = 0
turnFlag = 1    # player = 1, machine = 0

for i in range(3):
    for j in range(3):
        key = str(i) + str(j)
        board[key] = '  '

posToUse= list(board)
drawboard(board) 

while posToUse:
    turnFlag = moveTurn(turnFlag)
    time.sleep(300)

if posToUse == [] and not winner:
    print(f"{playerSign * 5} It's a tie!!! {machineSign * 5}")

print('\n' * 2)