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
