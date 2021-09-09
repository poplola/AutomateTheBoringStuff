#! Python 3 -> shebang line
# factorialLog.py
# Debug and Calculate the factorial of a number
"""
Say you wrote a function to calculate the factorial of a number. 
In mathematics, factorial 4 is 1 × 2 × 3 × 4, or 24. 
Factorial 7 is 1 × 2 × 3 × 4 × 5 × 6 × 7, or 5,040. 
Open a new file editor tab and enter the following code. 
It has a bug in it, but you will also enter several log messages to help yourself figure out what is going wrong.
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n)) 
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total)) 
    logging.debug('End of factorial(%s)' % (n)) 
    return total

print(factorial(5)) 
logging.debug('End of program')