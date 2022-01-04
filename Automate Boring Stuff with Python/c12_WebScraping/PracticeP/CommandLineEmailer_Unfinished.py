#! Python3
# Command Line Emailer
# CommandLineEmailer.py
"""
Write a program that takes an email address and string of text on the command 
line and then, using selenium, logs in to your email account and sends an email 
of the string to the provided address. 
(You might want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs. 
You could also write a similar program to send messages from a Facebook or Twitter account.

Command Line: 
python3 CommandLineEmailer.py seletestpy@gmail.com
"""

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# if len(sys.argv) < 3:
#     print("\nCommand Line format:\npython3 CommandLineEmailer.py <email address to be sent> <message to be sent>\n")
#     sys.exit()

# print(sys.argv)

# browser = webdriver.Safari()
browser = webdriver.Chrome()
url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
browser.get(url)

loginInput = browser.find_element_by_id('identifierId')
loginInput.send_keys("seletestpy@gmail.com")
loginInput.send_keys(Keys.RETURN)