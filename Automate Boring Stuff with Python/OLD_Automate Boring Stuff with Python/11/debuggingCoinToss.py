# python3
# Debugging Coin Toss
# The following program is meant to be a simple coin toss guessing game. 
# The player gets two guesses (it’s an easy game). However, the program has several bugs in it. 
# Run through the program a few times to find the bugs that keep the program from working correctly.

import random
import logging
logging.basicConfig(filename='debuggingCoinTossLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL)

guess = ''
while guess not in ('heads', 'tails'):

    logging.debug('start of the program')

    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f'guess ======= {guess} ========')
# toss = random.choice('tails', 'heads')   # <=== WRONG CODE ===>

toss = random.choice(['tails', 'heads'])  # 0 is tails, 1 is heads
logging.debug(f'toss ======== {toss} =========')



if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guesss = input()   # <=== WRONG CODE ===>
    guess2 = input()

    logging.debug(f'guess 2 ======= {guess2} ========')
    logging.debug(f'toss 2 ======== {toss} =========')

    # if toss == guess:   # <=== WRONG CODE ===>
    if toss == guess2:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


logging.debug('End of the program\n')

