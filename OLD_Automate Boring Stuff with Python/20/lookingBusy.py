#! python3
# lookingBusy.py
# Many instant messaging programs determine whether you are idle, or away from your computer, 
# by detecting a lack of mouse movement over some period of time—say, 10 minutes. 
# Maybe you’re away from your computer but don’t want others to see your instant messenger status go into idle mode. 
# Write a script to nudge your mouse cursor slightly every 10 seconds. 
# The nudge should be small and infrequent enough so that it won’t get in the way 
# if you do happen to need to use your computer while the script is running.

import pyautogui, time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


time.sleep(1)
screenSize = pyautogui.size()


logging.debug(f'Screen Size : {screenSize}')



m = 1
while True:
    x, y = pyautogui.position()


    logging.debug(f'(x, y) : ({x}, {y})')


    pyautogui.PAUSE = 5

    n = x + m
    m = -m

    pyautogui.moveTo(n, y)



    logging.debug(f'(n, y) : ({n}, {y})')

    pyautogui.moveTo(n, y)
    



