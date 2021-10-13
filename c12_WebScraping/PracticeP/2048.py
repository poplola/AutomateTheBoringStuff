#! python3
# 2048
# 2048.py
"""
2048 is a simple game where you combine tiles by sliding them up, down, left, or 
right with the arrow keys. You can actually get a fairly high score by repeatedly 
sliding in an up, right, down, and left pattern over and over again. Write a program 
that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending 
up, right, down, and left keystrokes to automatically play the game.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(messages)s')

browser = webdriver.Chrome()

browser.get('https://play2048.co')

newGame = browser.find_element_by_tag_name('body')

for i in range(150):
    newGame.send_keys(Keys.UP)
    newGame.send_keys(Keys.RIGHT)
    newGame.send_keys(Keys.DOWN)
    newGame.send_keys(Keys.LEFT)


time.sleep(15)
browser.quit()
