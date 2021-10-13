# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import pyperclip
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from pynput.keyboard import Key, Controller

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

browser = webdriver.Chrome()


# logging.debug(f'type of browser ======= {type(browser)} =======')

browser.get('https://www.google.com/gmail')
# print(browser.title)





inputEmail = browser.find_element_by_id('identifierId')
logging.debug(f'type of input Email ============= {type(inputEmail)} ==============')
logging.debug(f'input Email ============= {inputEmail} ==============')
inputEmail.send_keys('seletestpy@gmail.com')
inputEmail.send_keys(Keys.RETURN)
# html = browser.page_source
# print(html)
logging.debug(f'http address ============= {browser.current_url } ==============')
# browserP = browser.get(str(browser.current_url))



# inputPwd = browser.find_elements_by_name("password")
# if inputPwd == []:
#     print('============== inputPwd == [] =================')
time.sleep(1)
inputEmail = browser.find_element_by_name('password')
inputEmail.send_keys('fdsaqwer')
inputEmail.send_keys(Keys.RETURN)


logging.debug(f'type of inputPwd element ============= {type(inputEmail)} ==============')
logging.debug(f'inputPwd ============= {inputEmail} ==============')
# inputPwd.send_keys('fdsaqwer')
# inputPwd.send_keys(Keys.RETURN)

time.sleep(2)
composeEmail = browser.find_element_by_tag_name('div[class="T-I T-I-KE L3"]')
logging.debug(f'type of composeEmailt ============= {type(composeEmail)} ==============')
logging.debug(f'composeEmail ============= {composeEmail} ==============')

composeEmail.click()
time.sleep(1)
writeEmailSend = browser.find_element_by_name('to')
writeEmailSend.send_keys('flaviolj@comcast.net')
# writeEmailSend.Send.send_keys(Keys.RETURN)
# writeEmailSend.Send.send_keys(Keys.TAB)

writeEmailSubject = browser.find_element_by_name('subjectbox')


writeEmailSubject.send_keys('test')
# writeEmailSubject.send_keys(Keys.RETURN)
# writeEmailSubject.send_keys(Keys.TAB)

writeEmailContent = browser.find_element_by_tag_name('div[aria-label="Message Body"]')
writeEmailContent.click()
writeEmailContent.send_keys(Keys.COMMAND, 'v') #paste
writeEmailContent.click()

# keyboard = Controller()
# with keyboard.pressed(Keys.COMMAND):
#     keyboard.press('v')
#     keyboard.release('v')
time.sleep(3)
# writeEmailContent.send_keys(f'{pyperclip.paste()}')
# writeEmailContent.send_keys('I love you papa and mama!')
# writeEmailContent.send_keys(Keys.TAB)

# insertPhoto = browser.find_element_by_tag_name('div[aria-label="Insert photo"]')
# insertPhoto.click()


# writeEmailSendButton = browser.find_element_by_id(':88')
# writeEmailSendButton = browser.find_element_by_tag_name('div[class="T-I J-J5-Ji aoO v7 T-I-atl L3 T-I-Zf-aw2"]')



writeEmailSendButton = browser.find_element_by_tag_name('div[aria-label="Send ‪(⌘Enter)‬"]')
writeEmailSendButton.click()

time.sleep(15)
browser.quit()



