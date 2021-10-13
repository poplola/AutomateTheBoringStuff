import time, sys

def printStar(n):
    print(' '*n + '********')
    time.sleep(0.1)

def main():
    print('===================================')
    j = 10      # Print 10 lines
    m = 6       # How many empty space
    try:
        while j:
            j -= 1
            for i in range(m, 0, -1):
                printStar(i)  
            for i in range(m):
                printStar(i)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__": main()