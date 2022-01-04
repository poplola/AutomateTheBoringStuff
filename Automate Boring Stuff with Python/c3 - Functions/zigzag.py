
import time, sys

c = '*'
num = 8
flag = -1

def printStar():
    print(f"{c}" * 8, end='')

def drawWave():
    global num
    global flag
    for i in range(num+1):
        print(' ', end='')

    printStar()

    for j in range(8 - num):
        print(' ', end='')        
    
    num += flag

    if num < 0 or num > 8:
        flag = -flag

try:
    while True:
        for m in range(3):
            drawWave()
            print(" " * 8, end='')
        print('\n')
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()