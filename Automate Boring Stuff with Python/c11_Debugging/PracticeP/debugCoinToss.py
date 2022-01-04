#! Python 3 -> shebang line
# debugCoinToss.py
# Debugging Coin Toss
"""
The following program is meant to be a simple coin toss guessing game. 
The player gets two guesses (it’s an easy game). However, the program has several bugs in it. 
Run through the program a few times to find the bugs that keep the program from working correctly.

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads 
    if toss == guess:
        print('You got it!') 
    else:
        print('Nope! Guess again!') 
        guesss = input()
        if toss == guess:
            print('You got it!') 
        else:
            print('Nope. You are really bad at this game.')
"""

import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')    # Coreection ===> add logging module
logging.disable(logging.ERROR)

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails ( 0 is tails, 1 is heads ):')
    guess = input()
    toss = str(random.randint(0, 1)) # 0 is tails, 1 is heads ===> coreection: add str() 
    logging.debug(f"{toss}, {guess}")    # Coreection ===> add logging 
    if toss == guess:
        print('You got it!') 
        logging.debug(f"{toss}, {guess}")   # Coreection ===> add logging 
        # print(toss, guess) #
    else:
        print('Nope! Guess again!') 
        guess = input()
        logging.debug(f"{toss}, {guess}")   # Coreection ===> add logging 

        if toss == guess:
            print('You got it!') 
        else:
            print('Nope. You are really bad at this game.')
        # print(toss, guess)  #
        logging.debug(f"{toss}, {guess}")   # Coreection ===> add logging 
