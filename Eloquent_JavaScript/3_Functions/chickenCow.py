
def zeroPad(number, width):
    strNumber = str(number)
    while(len(strNumber)< width):
        strNumber = '0' + strNumber
    return strNumber    

def printFarmInventory(cows, chickens, pigs):
    size = 3
    print(f"{zeroPad(cows, size)} cows".upper())
    print(f"{zeroPad(chickens, size)} chickens")
    print(f"{zeroPad(pigs, size)} pigs")

printFarmInventory(7, 16, 3)