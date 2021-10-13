import random

print('===========================================================')
print('ROCK, PAPER, SCISSORS')


def main():
    wins = 0
    losses = 0
    ties = 0
    myDict = {'r' : 'ROCK', 'p' : "PAPER", 's' : "SCISSORS"}

    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        print('===========================================================')
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uit')
        n = input()
     
        if n == 'q':
            break
        elif n in myDict.keys():
            print(myDict.get(n), 'versus...')
        else:
            print('Invalid input! please enter letter r, s, p or q!')
            continue

        m = random.choice(list(myDict.keys()))
        print(myDict.get(m))

# Input VS. Random
        if n == m:
            ties += 1
            print("It is a tie!")
        elif (n == 'r' and m =='p') or (n == 'p' and m == 's') or (n == 's' and m == 'r'):
            losses += 1
            print('You lost!')
        elif (n =='r' and m == 's') or (n == 'p' and m == 'r') or (n == 's' and m == 'p'):
            wins += 1
            print('You win!')
        # elif :
        #     wins += 1
        #     print('You win!') 
        # elif :
        #     losses += 1
        #     print('You lost!')
        # elif :
        #     losses += 1
        #     print('You lost!')      
        # elif :
        #     wins += 1
        #     print('You win!') 



if __name__ == "__main__": main()

