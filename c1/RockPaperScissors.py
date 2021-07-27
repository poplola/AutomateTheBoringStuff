import random, sys

print('\n' + "=" * 50)
print("ROCK, PAPER, SCISSORS")
print("=" * 50)

win = 0
loss = 0
tie = 0
count = 0
itemList = ['ROCK', 'PAPER', 'SCISSORS']

while True:
    print(f"\n=======  {win} Wins, {loss } Losses, {tie} Ties  =======")
    count += 1
    print(f"Try {count} : Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    
    inputKey = input().upper()
    if inputKey == 'Q':
        print("You are quitting the game. Bye!\n")
        sys.exit()
    elif not (inputKey in ['R', 'P', 'S']):
        print("Please input key: r, p, s or q")
        continue

    inputItem = [itemList[i] for i in range(3) if inputKey == itemList[i][0]]
    print(f"\n{inputItem[0]} versus ...")

    guessItem = itemList[random.randint(0, 2)]
    print(guessItem)

    if guessItem in inputItem:
        tie += 1
        print('It is a tie!')
    elif inputKey == 'R' and guessItem[0] == 'S' or inputKey == 'P' and guessItem[0] == 'R' or inputKey == 'S' and guessItem[0] == 'P':
        win += 1
        print('You win!')
    else:
        loss += 1
        print('You loss!')
    
